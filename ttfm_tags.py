import os
import pydicom

ds = pydicom.dcmread("ttfm.dcm")

ab = str(ds)

tag_list = []

word=''

for letter in ab:
    if letter == '(':
        word = '('
    elif letter == ')':
        word = word + letter
        tag_list.append(word)
        word = ''
    elif word != '':
        word = word + letter
    

for element in tag_list:
    if len(element) < 5:
        tag_list.remove(element)
        

file = open("ttfm_tags.txt","w+")

for element in tag_list:
        file.write(element)
        file.write('\n')

file.close()
