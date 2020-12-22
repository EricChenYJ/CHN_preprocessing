# coding=utf-8
from types import FunctionType
import PIL
import os
import sys
import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import time

    
def all_white_pixels(image):
    '''
        Returns True if all white pixels or False if not all white
        check if pixel are all white
    '''
    H, W = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    pixels = cv2.countNonZero(thresh)
    return True if pixels == (H * W) else False



'''
create a char corresponding to a img
'''

if __name__ == '__main__':
    file_path = './check_char_font/'
    files = os.listdir(file_path)

    # Read dictionary
    with open( 'data/chars/chn.txt', 'r' ,encoding='utf-8') as input:
        print ('file opened')
        all_lines = input.readlines()
        # generate one-word image
        for info in os.listdir('./data/fonts/chn/'):
            num = 1
            for char in all_lines:
                # white background
                image = Image.new("RGB",(50,50),"white")
                draw_table = ImageDraw.Draw(im=image)
                draw_table.text(xy=(0, 0), text= char, fill='#000000', font=ImageFont.truetype('data/fonts/chn/'+str(info), 50))
                # save into img
                image.save(os.path.join('check_char_font/',os.path.basename(info + '_' + str(num) +'.png')))
                num +=1
            print('font'+str(info)+'finished.')

    with open('output/wrong_font.txt','w',encoding = 'utf-8') as wrong_font:
        # output wrong text with font
        for img in files:
            image = cv2.imread(file_path + str(img))
            if all_white_pixels(image):
                print('something wrong.'+ img)
                # access char index 
                num = img.split('_')[-1]
                index = num.split('.')[0]
                # access font
                font_name = img.split('.TT')[0]
                wrong_font.write(font_name +' '+ all_lines[int(index)-1] +'\n')
        print('check done.')
    wrong_font.close()
        
    count = 0 
    dict_temp = {}
    # use dictionary to record  a font that appends char can't be append 
    with open('output/wrong_font.txt','r',encoding = 'utf-8') as wrong_font:
        with open('output/final_result.txt','w',encoding='utf-8') as final:
            for line in  wrong_font.readlines():
                count += 1 
                temp = line.replace('\n','')
                key = temp.split(' ')[0]
                val = temp.split(' ')[-1]
                if key in dict_temp:
                    dict_temp[key].append(val)
                else:    
                    dict_temp[key] = [val]
                    
            for k,v in dict_temp.items():
                count +=1
                final.write(str(k)+' ')
                for item in v:
                    final.write(str(item)+' ')
                final.write('\n')
    wrong_font.close()
    final.close()
