# author: hcjohn463
#!/usr/bin/env python
# coding: utf-8
from args import *
from download import download
from movies import movieLinks
# In[2]:

parser = get_parser()
args = parser.parse_args()

if(len(args.url) != 0):
    url = args.url
    download(url, args.destination)
elif(args.random == True):
    url = av_recommand()
    download(url, args.destination)
elif(args.all_urls != ""):
    all_urls = args.all_urls
    urls = movieLinks(all_urls)
    for url in urls:
        download(url, args.destination)
else:
    # 使用者輸入Jable網址
    url = input('輸入jable網址:')
    download(url)
