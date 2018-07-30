import json
import requests
import unicodedata
import operator
import urllib
import urllib.request
from xml.etree import ElementTree as ET
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string 
import html
import os
from .io_utils import read_pdf_and_docx
requestURL="https://www.enbek.kz/ru/xml/jooble"


name=""
root = ET.parse(urllib.request.urlopen(requestURL)).getroot()

def stop_words_kk():        
    stop_words_kk=[]
    with open('./stop.txt','rb') as f:
        lines = f.readlines()
        stop_words_kk.append(lines[0])
    return stop_words_kk




stop_words = stopwords.words('russian')
for word in stopwords.words('russian'):
    stop_words.append(word.upper())
stop_words_k=stop_words_kk()


punctuations = ['(', ')' ,'—' ,';',':','[',']',',','»', '«', 'Январь','Февраль',
                 'Март','Апрель', 'Май', 'Июнь', 'Июль',
                 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', '1','2','3','4','5','6','7','8','9','года','месяцев','мастер','of','p',
                 '/p','lt','li','/li','gt','/ul','amp','nbsp','ul','/strong']
numbers = ['(', ')' ,'—' ,';',':','[',']',',','»', '«', 'Январь','Февраль',
                 'Март','Апрель', 'Май', 'Июнь', 'Июль',
                 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', '1','2','3','4','5','6','7','8','9','года','месяцев','мастер','of','p',
                 '/p','lt','li','/li','gt','/ul','amp','nbsp','ul','/strong']
jobs=dict()



for job in root.iter('job'):
    job_id = job.attrib.get('id')    
    name=job.find('name').text
    names=word_tokenize(name)
    names = [wor for wor in names if not wor in stop_words and  not wor in string.punctuation]
    names = [word for word in names if not word in stop_words_k and  not word in numbers]
    jobs[job_id]= names
    description=job.find('description').text
    if(description != None):
        descriptions=word_tokenize(description)
        descriptions = [wor for wor in descriptions if not wor in stop_words and  not wor in string.punctuation]
        descriptions = [word for word in descriptions if not word in stop_words_k and  not word in numbers]
        jobs[job_id].extend(descriptions)
    

def get_vacants(fname, pages=None):
    l = read_pdf_and_docx(fname)
    cv_summary = {}
    
    counter = -1
    for line in l:
        counter+= 1
        
        if "Желаемая должность и зарплата" in line:
            cv_summary["position"] = l[counter+1]
            counter_l = counter + 3
            
            while("•" in l[counter_l]):
                cv_summary["position"] += " " + l[counter_l]
                counter_l += 1
        
        if "Навыки" in line:
            cv_summary["skills"] = l[counter+1]
            counter_l = counter+2
            
            while True:
                cv_summary["skills"] += " " + l[counter_l]
                counter_l += 1
                if("Опыт вождения" or "Дополнительная информация" in l[counter_l]):
                    break
        
        # if "Образование" in line:
        #     cv_summary["education"] = l[counter+1]
        #     counter_l = counter+2
            
        #     while True:
        #         if("Резюме обновлено" not in l[counter_l]):
        #             if("Ключевые навыки" in l[counter_l]):
        #                 break
        #             cv_summary["education"] += " " + l[counter_l]
                
        #         counter_l += 1
        
        # if "Опыт работы" in line:
        #     cv_summary["work"] = l[counter+1]
        #     counter_l = counter+2
            
        #     while True:
        #         if("Резюме обновлено" not in l[counter_l]):
        #             if("Образование" in l[counter_l]):
        #                 break
        #             cv_summary["work"] += " " + l[counter_l]
                
        #         counter_l += 1  
                

        
    for key in cv_summary:
        cv_summary[key] = cv_summary[key].replace('.', '').replace(',', '').split()

        cv_summary[key] = [a for a in cv_summary[key] if not a in stop_words and  not a in string.punctuation]
        cv_summary[key] = [ab for ab in cv_summary[key] if not ab in stop_words_k and  not ab in numbers]
    if 'position' in cv_summary:
        key_pos = [x for x in cv_summary["position"]  if x != "•"]
        cv_summary['position'] = key_pos
    
    recomend = {}

    for key in jobs:
        for word in jobs[key]:
            for key_1 in cv_summary:
                for word_1 in cv_summary[key_1]:
                    if(word == word_1):
                        if key not in recomend.keys():
                            recomend[key] = 1
                        else:
                            recomend[key] += 1

    recomend_sorted_list = sorted(recomend.items(), key=lambda x: x[1],reverse=True)

    recomend_sorted_dict = dict(recomend_sorted_list)

    print(recomend_sorted_dict)

    # vacants = {}

    # for key_1 in recomend_sorted_dict:
    #     vacants[key_1] = jobs[key_1]

    return recomend_sorted_dict.keys(),cv_summary

    # sorted(recomend.items(), key=lambda x: x[1])