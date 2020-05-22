# coding=utf-8

import os
import random

file1 = open("script_type.txt","w")

image_type = 'food'
images = os.listdir('img/gallery/' + image_type)
    
created = []
for image in images:
    print(image[len(image)-5])
    if image[len(image)-5] == '1' or image[len(image)-5] == '2' or image[len(image)-5] == '3' or image[len(image)-5] == '4':
        continue
    front = "<div class=\"gallery-item " + image_type + "\"><img src=\"img/gallery/"
    back = "\" alt=\"\"><div class=\"hover-links\"><a href=\"/gallery-single.html\" class=\"site-btn sb-light\">자세히</a></div></div>" 
    curr = ""
    curr = front + image_type + "/" + image + back + "\n"
    created.append(curr)
    # print(curr)
    # break

random.shuffle(created)
for c in created: 
    file1.write(c)
# print(created)