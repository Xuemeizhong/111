#encoding: utf-8

import re
import  json

def findAndReplace(before,after):
    '''
    param: before
    param: after
    '''

    pattern = re.compile(r'\${(.+?)}')
    items =re.finditer(pattern,after)
    for item in items:
        after = after.replace(item.group(),str(before[item.group(1)]))
    return json.loads(after)


if __name__ == "__main__":
    before = {'login':'xxx','pwd':'xxx','language':'zh-hans'}
    after = {'login':'${login}','pwd':'${pwd}','name':'lonel','language':'zh-hans'}
    print(f"after:{type(after)}  brfore:{type(before)}")
    data = findAndReplace(before,json.dumps(after))


    