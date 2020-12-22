# coding=UTF-8
import re
import os



# multi-files version
def main():
    
    pat_block = u'[^\u4e00-\u9fff0-9a-zA-Z]+'
    # 、 ： ；\n
    # pat_block =u'[、 ： ；]'
    # pat_block = '\"'
    pattern = u'([0-9]+{0}[0-9]+)|{0}'.format(pat_block) 
    text_path =  "data/newsgroup/"
    files = os.listdir(text_path)
    files = files[:]
    # print(files)
    for f_name in files:
        with open(text_path + f_name ,'r',encoding='utf8') as f:
            text = f.read()        
            res = re.sub(pattern,lambda x: x.group(1) if x.group(1) else u" ",text)
            with open(text_path + f_name,'w',encoding='utf8') as w:
                w.write(str(res))
            w.close()
        f.close()
    print('remove'+ '<' + str(pat_block) + '>'+'done')
    
if __name__=='__main__':
    main()


#---------------------------------------------------------------------------------------------------------------------


# def main():
#     pat_block = u'[^\u4e00-\u9fff0-9a-zA-Z]+'
#     # pat_block =u'\n'
#     pattern = u'([0-9]+{0}[0-9]+)|{0}'.format(pat_block) 

#     text_path =  "data/newsgroup/ee.txt"
#     text_list = []
#     basepath = 'data/newsgroup/'



#     # for path in text_list:
#     # with open(text_path + path ,'r') as f:
#     with open(text_path ,'r',encoding='utf8') as f:
#         text = f.read()        
#         res = re.sub(pattern,lambda x: x.group(1) if x.group(1) else u" ",text)
#         # result = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "",result)
#         # with open(text_path + path,'w') as w:
#         with open(text_path ,'w',encoding='utf8') as w:
#             w.write(str(res))




# if __name__=='__main__':
#     main()




#---------------------------------------------------------------------------------------------------------------------
    # pat_block =u'\n'
    # pattern = u'([0-9]+{0}[0-9]+)|{0}'.format(pat_block) 
    # res = re.sub(pattern,lambda x: x.group(1) if x.group(1) else u"",text)
