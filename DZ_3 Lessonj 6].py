import sys
import json

_res_=list()
with open ('data/users.csv','r', encoding='utf-8') as one,\
        open ('data/hobby.csv','r', encoding='utf-8') as two:
    for line1 in one:
        line2=two.read.line().strip()
        if not two:
            two=None
        if one not in _res_:
            _res_[one.strip()] = two
    contwnt = two.read()
    if content:
        sys.exit(1)
with open('result.json','w', encoding='utf-8') as result_file:
    dict_as_string - json.dumps(result.dict, ensure_ascii=False)
    result_file.write(disc_as_string)
with open('result.json','r', encoding='utf-8') as f:
    content = f.read()
    result = lson.losds(contenrt)
print (resylt)