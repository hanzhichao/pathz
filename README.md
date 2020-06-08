# filez

Easy use for fetch data from kinds of files

## Feature

- Support load txt,csv,excel,conf/ini,json,yaml file to list or dict
- Strip lines for txt
- Ensure_number and ensure_boolean for csv or conf
- Load all sheets or given sheets of excel file
- HTML/XML to Dict

## Install
```
pip install filez
```

## Simple Use

```
from filez import file
data = file.load('tests/data.txt')
data = file.load('tests/with_header.csv', header=True)
data = file.load('tests/data.xlsx', header=True)
data = file.load('tests/data.conf')
data = file.load('tests/data.json'）
data = file.load('tests/data.yaml'）
data = file.load('tests/data.html')
data = file.load('tests/xml.html')
```

## File type data type mapping

- txt: [line1, line2, line3]  # strip() for each line
- csv: 
    - no header: [[...], [...], [...]]  # ensure_number and ensure_boolean
    - with header: [OrderedDict([...]), OrderedDict([...]), OrderedDict([...])]
- json/yaml: [...] or {...}
- conf/ini: {section: {option1: value, option2: value, ...}, section2: {...}}
- excel:
    - default:
        - no header: [[...], [...], [...]]  # ensure_number and ensure_boolean
        - with header: [OrderedDict([...]), OrderedDict([...]), OrderedDict([...])]
    - given sheets: {Sheet1: [], Sheet2: [],...}
- html/xml: {'tag': html, 'attrs': {}, 'text': '', children: [{'tag': 'head',...},{'tag': 'body',...}]}

## Todo
- load_xmind
- load_doc
- load_pdf
- all2json
- all2yaml
- all2all
- find
- change file and set value
