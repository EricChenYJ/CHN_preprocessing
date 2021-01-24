# encofing='utf-8'

import os 
import sys
import pynlpir
from re import compile as _Re

dictionary_path='./corpus/picked.txt'
pure_dictionary='chn.txt'


'''
chinese data pre-processing
    
    create clean dictionary .txt

'''


_unicode_chr_splitter = _Re( '(?s)((?:[\ud800-\udbff][\udc00-\udfff])|.)' ).split




def split_unicode_chrs( text ):
    return [ chr for chr in _unicode_chr_splitter( text ) if chr ]

# create no repate item list
def deleteDuplicatedElementFromList2(list):
    resultList = []
    for item in list:
        if not item in resultList:
            resultList.append(item)
    return resultList

if __name__=='__main__':
    # READ word txt file
    with open(dictionary_path,'r',encoding='utf-8') as f:
        words=f.readlines()


# words = map(lambda s: s.strip(), words)
# words=split_unicode_chrs()

    # delete duplicate items
    result=deleteDuplicatedElementFromList2(words)



    # create clean dicitonary  
    with open(pure_dictionary,'w',encoding='utf-8') as test:
        for i in result:
            oh=str(i)
            test.write(str(oh))

