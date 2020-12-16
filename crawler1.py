#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm


def get_content(target):
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().split('\xa0'*4)
    return content

if __name__ == '__main__':
    # #target = 'https://www.sbiquge.com/0_736/440692.html'   ###这一部分是读取具体某一章
    # target='https://www.xsbiquge.com/15_15338/8549128.html'
    # req = requests.get(url=target)
    # req.encoding = 'utf-8'
    # html=req.text
    # #print(req.text)
    # bf=BeautifulSoup(html,'html.parser')
    # #print(bf)
    # texts=bf.find_all('div',id='content')
    # print(texts[0].text.split('\xa0'*4))

    # catalog='https://www.xsbiquge.com/15_15338/'
    # req_catalog = requests.get(url=catalog)
    # req_catalog.encoding = 'utf-8'
    # html_catalog = req_catalog.text
    # bf_catalog = BeautifulSoup(html_catalog, 'lxml')
    # chapters = bf_catalog.find_all('div', id='list')
    # #print(chapters)
    # chapters = chapters[0].find_all('a')
    # for chapter in chapters:
    #      url=chapter.get('href')
    #      print(chapter.string)
    #      print('https://www.xsbiquge.com'+url)



    server = 'https://www.xsbiquge.com'
    book_name = '诡秘之主.txt'
    target = 'https://www.xsbiquge.com/15_15338/'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', id='list')
    #print(chapters)
    chapters = chapters.find_all('a')

    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')