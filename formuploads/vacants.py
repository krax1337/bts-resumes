import html
import json
import operator
import os
import string
import unicodedata
import urllib
import urllib.request
from xml.etree import ElementTree as ET

import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

from langdetect import detect

from .io_utils import read_pdf_and_docx
from .vacants_en import get_vacants_en
from .vacants_ru import get_vacants_ru

requestURL = "https://www.enbek.kz/ru/xml/jooble"

name = ""
root = ET.parse(urllib.request.urlopen(requestURL)).getroot()


def stop_words_kk():
    stop_words_kk = []
    with open('./stop.txt', 'rb') as f:
        lines = f.readlines()
        stop_words_kk.append(lines[0])
    return stop_words_kk


stop_words = stopwords.words('russian')
stop_words_k = stop_words_kk()
for word in stopwords.words('russian'):
    stop_words.append(word.upper())


numbers = ['(', ')', '—', ';', ':', '[', ']', ',', '»', '«', 'Январь', 'Февраль',
           'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
           'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'года', 'месяцев', 'мастер', 'of', 'p',
           '/p', 'lt', 'li', '/li', 'gt', '/ul', 'amp', 'nbsp', 'ul', '/strong']

jobs = dict()


for job in root.iter('job'):
    job_id = job.attrib.get('id')

    name = job.find('name').text
    names = word_tokenize(name)
    names = [
        wor for wor in names if not wor in stop_words and not wor in string.punctuation]
    names = [
        word for word in names if not word in stop_words_k and not word in numbers]
    jobs[job_id] = names

    description = job.find('description').text
    if(description != None):
        descriptions = word_tokenize(description)
        descriptions = [
            wor for wor in descriptions if not wor in stop_words and not wor in string.punctuation]
        descriptions = [
            word for word in descriptions if not word in stop_words_k and not word in numbers]
        jobs[job_id].extend(descriptions)


def get_vacants(fname, pages=None):
    l = read_pdf_and_docx(fname)
    cnt_en = 0
    cnt_ru = 0
    for line in l:
        try:
            print(line)
            if detect(line) == 'en':
                cnt_en += 1
            if detect(line) == 'ru':
                cnt_ru += 1
        except:
            continue
    if cnt_ru > cnt_en:
        cv_summary = get_vacants_ru(l)
    else:
        cv_summary = get_vacants_en(l)
    recomend = {}
    for key in jobs:
        for word in jobs[key]:
            for key_1 in cv_summary:
                if(key_1 == "position" or key_1 == "skills"):
                    for word_1 in cv_summary[key_1]:
                        if(word == word_1):
                            if key not in recomend.keys():
                                recomend[key] = 1
                            else:
                                recomend[key] += 1

    recomend_sorted_list = sorted(
        recomend.items(), key=lambda x: x[1], reverse=True)

    recomend_sorted_dict = dict(recomend_sorted_list)

    res_dict = {}

    counter = -1
    for key in recomend_sorted_dict:
        counter += 1
        if(counter > 20):
            break
        else:
            res_dict[key] = recomend_sorted_dict[key]

    return res_dict.keys(), cv_summary
