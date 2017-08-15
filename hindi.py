import xml.etree.ElementTree as etree
import sys
import time
import os
import re
from collections import *
#reload(sys)
#sys.setdefaultencoding('utf8')

fileHindi = 'hiwiki-20170801-pages-meta-current.xml'

def strip_tag_name(t):
    t = elem.tag
    idx = k = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t

title = None
co = 0
wordFrequency = defaultdict(int)
#wordPageCount = defaultdict(int)

for event, elem in etree.iterparse(fileHindi, events=('start', 'end')):
    tname = strip_tag_name(elem.tag)
    # co += 1
    # if co > 5000:
    #     break
    if tname == 'text':
        title = elem.text
        try :
            title = re.split(r"[\x00-\x7f]+", title)
            # flag = defaultdict(bool)
            for t in title:
                if t :
                    wordFrequency[t] += 1
            #         if not flag[t] :
            #             flag[t] = True
            #             wordPageCount[t] += 1
            # flag.clear()
        except :
            pass

    elem.clear()
#print co
#elapsed_time = time.time() - start_time
#print(len(wordFrequency))
s = Counter(wordFrequency)
co = 0
topWordsNumber = 100
maxLen = 4
# for word in wordPageCount:
#     wordPageCount[word] *= wordFrequency[word]
for k,v in s.most_common(100):
    if(len(k)<=maxLen):
        print(k)
        co += 1
    if co==topWordsNumber:
        break
# s = Counter(wordPageCount)
# print("2nd one :")
# for k,v in s.most_common(50):
#     if(len(k)<maxLen):
#         print(k,v,len(k))
#         co += 1
    # if co==topWordsNumber:
    #     break

#print("Elapsed time: {}".format(hms_string(elapsed_time)))
# # Nicely formatted time string
# def hms_string(sec_elapsed):
#     h = int(sec_elapsed / (60 * 60))
#     m = int((sec_elapsed % (60 * 60)) / 60)
#     s = sec_elapsed % 60
#     return "{}:{:>02}:{:>05.2f}".format(h, m, s)
#
#
