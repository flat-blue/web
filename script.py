# coding=utf-8

import os
import random

file1 = open("script.txt","w")


created = []

types = os.listdir('img/gallery/')
for t in types:
    if t == '.DS_Store' or t == 'logo.png':
        continue
    entries = os.listdir('img/gallery/'+ t)
    front = "<div class=\"gallery-item " + t + "\"><img src=\"img/gallery/"
    back = "\" alt=\"\"><div class=\"hover-links\"><a href=\"/gallery-single.html\" class=\"site-btn sb-light\">자세히</a></div></div>" 
    for entry in entries:
        curr = ""
        curr = front + t + "/" + entry + back + "\n"
        created.append(curr)
        # print(curr)
        # break

random.shuffle(created)
for c in created: 
    file1.write(c)
# print(created)