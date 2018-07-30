import json
import requests
import unicodedata
import operator
import urllib
import urllib.request
import string 
import html
import os
from xml.etree import ElementTree as ET
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
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
stop_words_k=stop_words_kk()
for word in stopwords.words('russian'):
    stop_words.append(word.upper())



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

    head_hunter = False
    
    for line in l:
        if "Резюме обновлено" in line:
            head_hunter = True
            break



    if(head_hunter):
        cv_summary = {}
        counter = -1
        for line in l:
            counter+= 1
            
            if "Желаемая должность и зарплата" in line:
                cv_summary["position"] = l[counter+1]
                cv_summary["position"] += " " + l[counter+2]
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
            
            if "Образование" in line:
                cv_summary["education"] = l[counter+1]
                counter_l = counter+2
                
                while True:
                    if("Резюме обновлено" not in l[counter_l]):
                        if("Ключевые навыки" in l[counter_l]):
                            break
                        cv_summary["education"] += " " + l[counter_l]
                    
                    counter_l += 1
            
            if "Опыт работы" in line:
                cv_summary["experince"] = l[counter+1]
                counter_l = counter+2
                
                while True:
                    if("Резюме обновлено" not in l[counter_l]):
                        if("Образование" in l[counter_l]):
                            break
                        cv_summary["experince"] += " " + l[counter_l]
                    
                    counter_l += 1  
        
        for key in cv_summary:
            cv_summary[key] = cv_summary[key].replace('.', ' ').replace(',', ' ').split()

            cv_summary[key] = [a for a in cv_summary[key] if not a in stop_words and  not a in string.punctuation]
            cv_summary[key] = [ab for ab in cv_summary[key] if not ab in stop_words_k and  not ab in numbers]

        if 'position' in cv_summary:
            key_pos = [x for x in cv_summary["position"]  if x != "•"]
            cv_summary['position'] = key_pos
    
    else:
        
        key_words = {
        "education": ["Образование:", "Квалификация", "квалификация", "Квалификации", "квалификации",
        "Курсы", "курсы", ], 
        "position": ["Специальность", "специальность","цель", "Цель"], 
        "skills": [ "навыки", "Навыки", "Дополнительна информация", "дополнительна информация",
        "Компьютерная грамотность","компьютерная грамотность", "качества", "Качества" ], 
        "experince": [ "Опыт работы:"],
        "language" : ["Языки", "языки", "языков", "язык"]
        } 
    
        cv_summary = {"education": "", "position": "", 
        "skills": "", "experince": "", "language": ""}
    
        counter_l = -1
        for line in l:
            counter_l += 1
            for key in key_words:
                for word in key_words[key]:
                    if word in line: 
                        check = True
                        counter_2 = counter_l+1
                        while(check):
                            if(counter_2 >= len(l)-1):
                                check = False
                                counter_2 = 0
                                break
                            else:
                                cv_summary[key] += " " + l[counter_2]
                                counter_2 += 1
                            

                            
                            for key_1 in key_words:
                                for word_1 in key_words[key_1]:
                                    if word_1 in l[counter_2]:
                                        check = False
                                        counter_2 = 0
        
        for key in cv_summary:
            cv_summary[key] = cv_summary[key].replace('.', ' ').replace(',', ' ').split()

            cv_summary[key] = [a for a in cv_summary[key] if not a in stop_words and  not a in string.punctuation]
            cv_summary[key] = [ab for ab in cv_summary[key] if not ab in stop_words_k and  not ab in numbers]
    
    
    print(cv_summary)

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

    recomend_sorted_list = sorted(recomend.items(), key=lambda x: x[1],reverse=True)

    recomend_sorted_dict = dict(recomend_sorted_list)

    res_dict = {}

    counter = -1
    for key in recomend_sorted_dict:
        counter += 1
        if(counter > 20):
            break
        else:
            res_dict[key] = recomend_sorted_dict[key]
            
    print(res_dict)

    return res_dict.keys(),cv_summary

