import re
from jsonpath import jsonpath
from lxml import etree



class Pathz(object):
    def __init__(self):
        pass

    def find(self, data, **kwargs):
        _xpath = kwargs.get('xpath')
        _css = kwargs.get('css')
        _re = kwargs.get('re')
        _jsonpath = kwargs.get('jsonpath')
        default = kwargs.get('default', [])

        if _xpath:
            if isinstance(data, str):
                root = etree.HTML(data)
                return root.xpath(_xpath) or default

        if _re:
            if isinstance(data, str):
                return re.findall(_re, data) or default
        if _jsonpath:
            if isinstance(data, (dict, tuple, list)):   # todo 兼容鸭子类型
                return jsonpath(data, _jsonpath) or default

path = Pathz()


if __name__ == '__main__':
    r = path.find('010-12345678', re='\d{3,4}-\d{7,8}')
    print(r)
    r = path.find({'code': 0, 'data': {'a': 1, 'b': 2}}, jsonpath='$.data.a')
    print(r)
    data = '''<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
    </div>'''
    r = path.find(data, xpath='//li')
    print(r[0].attrib)

