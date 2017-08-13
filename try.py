# from xml.dom.minidom import parse
# import xml.dom.minidom
#
# domTree = xml.dom.minidom.parse("hiwiki-20170801-flow.xml")
#
# collection = domTree.documentElement
#
# hindis = collection.getElementByTagName("page")
#
# for hindi in hindis :
#     da = hindi.getElementByTagName("comment").firstChild.data
#     da = da.decode("utf-8")
#     print da

# Simple example of streaming a Wikipedia
# Copyright 2017 by Jeff Heaton, released under the The GNU Lesser General Public License (LGPL).
# http://www.heatonresearch.com
# -----------------------------
import xml.etree.ElementTree as etree
import codecs
import csv
import time
import os
import re

# http://www.ibm.com/developerworks/xml/library/x-hiperfparse/

PATH_WIKI_XML = ''
FILENAME_WIKI = 'hiwiki-20170801-pages-meta-current.xml'
FILENAME_ARTICLES = 'articles.csv'
FILENAME_REDIRECT = 'articles_redirect.csv'
FILENAME_TEMPLATE = 'articles_template.csv'
ENCODING = "utf-8"


# Nicely formatted time string
def hms_string(sec_elapsed):
    h = int(sec_elapsed / (60 * 60))
    m = int((sec_elapsed % (60 * 60)) / 60)
    s = sec_elapsed % 60
    return "{}:{:>02}:{:>05.2f}".format(h, m, s)


def strip_tag_name(t):
    t = elem.tag
    idx = k = t.rfind("}")
    if idx != -1:
        t = t[idx + 1:]
    return t


pathWikiXML = os.path.join(PATH_WIKI_XML, FILENAME_WIKI)
pathArticles = os.path.join(PATH_WIKI_XML, FILENAME_ARTICLES)
pathArticlesRedirect = os.path.join(PATH_WIKI_XML, FILENAME_REDIRECT)
pathTemplateRedirect = os.path.join(PATH_WIKI_XML, FILENAME_TEMPLATE)

totalCount = 0
articleCount = 0
redirectCount = 0
templateCount = 0
title = None
#daTa = None
start_time = time.time()
co = 0

for event, elem in etree.iterparse(pathWikiXML, events=('start', 'end')):
    tname = strip_tag_name(elem.tag)

    if event == 'start':
        co += 1
        if tname == 'page':
            title = ''
            id = -1
            redirect = ''
            #daTa = ''
            inrevision = False
            ns = 0
        elif tname == 'revision':
            # Do not pick up on revision id's
            inrevision = True
    else:
        #print co
        if co > 1000:
            break
        if tname == 'text':
            title = elem.text
            try :
                #title = re.split('\[|\]| |\n|=|<|>|\*|\w|\/',title)
                title = re.split(r"[\x00-\x7f]+", title)
                for t in title:
                    t = t.encode('utf-8')
                    if t:
                        print t
                #print title
            except :
                print "error"
        # elif tname == 'id' and not inrevision:
        #     id = int(elem.text)
        # elif tname == 'redirect':
        #     redirect = elem.attrib['title']
        # # elif tname == 'text':
        # #     daTa = elem.text
        # elif tname == 'ns':
        #     ns = int(elem.text)
        # elif tname == 'page':
        #     totalCount += 1
        #
        #     if ns == 10:
        #         templateCount += 1
        #         templateWriter.writerow([id, title])
        #     elif len(redirect) > 0:
        #         articleCount += 1
        #         articlesWriter.writerow([id, title,redirect])
        #     else:
        #         redirectCount += 1
        #         redirectWriter.writerow([id, title, redirect])

            # if totalCount > 100000:
            #  break

            # if totalCount > 1 and (totalCount % 100000) == 0:
            #     print("{:,}".format(totalCount))

        elem.clear()


# with codecs.open(pathArticles, "w", ENCODING) as articlesFH, \
#         codecs.open(pathArticlesRedirect, "w", ENCODING) as redirectFH, \
#         codecs.open(pathTemplateRedirect, "w", ENCODING) as templateFH:
#     articlesWriter = csv.writer(articlesFH, quoting=csv.QUOTE_MINIMAL)
#     redirectWriter = csv.writer(redirectFH, quoting=csv.QUOTE_MINIMAL)
#     templateWriter = csv.writer(templateFH, quoting=csv.QUOTE_MINIMAL)
#
#     articlesWriter.writerow(['id', 'title','daTa', 'redirect'])
#     redirectWriter.writerow(['id', 'title', 'redirect'])
#     templateWriter.writerow(['id', 'title'])
#
#     for event, elem in etree.iterparse(pathWikiXML, events=('start', 'end')):
#         tname = strip_tag_name(elem.tag)
#
#         if event == 'start':
#             if tname == 'page':
#                 title = ''
#                 id = -1
#                 redirect = ''
#                 #daTa = ''
#                 inrevision = False
#                 ns = 0
#             elif tname == 'revision':
#                 # Do not pick up on revision id's
#                 inrevision = True
#         else:
#             if tname == 'title':
#                 title = elem.text
#                 title = u' '.join(title).encode('utf-8')
#             elif tname == 'id' and not inrevision:
#                 id = int(elem.text)
#             elif tname == 'redirect':
#                 redirect = elem.attrib['title']
#             # elif tname == 'text':
#             #     daTa = elem.text
#             elif tname == 'ns':
#                 ns = int(elem.text)
#             elif tname == 'page':
#                 totalCount += 1
#
#                 if ns == 10:
#                     templateCount += 1
#                     templateWriter.writerow([id, title])
#                 elif len(redirect) > 0:
#                     articleCount += 1
#                     articlesWriter.writerow([id, title,redirect])
#                 else:
#                     redirectCount += 1
#                     redirectWriter.writerow([id, title, redirect])
#
#                 # if totalCount > 100000:
#                 #  break
#
#                 if totalCount > 1 and (totalCount % 100000) == 0:
#                     print("{:,}".format(totalCount))
#
#             elem.clear()

elapsed_time = time.time() - start_time

print("Total pages: {:,}".format(totalCount))
print("Template pages: {:,}".format(templateCount))
print("Article pages: {:,}".format(articleCount))
print("Redirect pages: {:,}".format(redirectCount))
print("Elapsed time: {}".format(hms_string(elapsed_time)))
