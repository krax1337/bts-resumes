import urllib.request
from xml.etree import ElementTree as ET

def analyse_file(all_vacants_info, vacants_ids):
    requestURL = "https://www.enbek.kz/ru/xml/jooble"
    root = ET.parse(urllib.request.urlopen(requestURL)).getroot()
    for key in vacants_ids:
        for job in root.iter('job'):
            if(job.attrib.get('id') == key):
                all_vacants_info.append({

                    'job_name': str(job.find('name').text).replace(", ", "", 1),
                    'job_region': str(job.find('region').text),
                    "job_salary": str(job.find('salary').text),
                    "job_description": str(job.find('description').text).replace("p&gt;", " ")
                                .replace("li", " ").replace("ul", " ")
                                .replace("/", " ").replace("&gt;", " ")
                                .replace("&lt;", " ").replace("ul&gt;", " ")
                                .replace("/li&gt;", " ").replace("li&gt;", " ")
                                .replace("-&amp;", " ").replace("nbsp;", " ")
                                .replace("&amp;", " ").replace("quot;", " ")
                                .replace("br", " ").replace("strong", " ")
                                .replace("strong", " ").replace("ol", " "),
                    "job_email": str(job.find('email').text),
                    "job_phone": str(job.find('phone').text),
                    "job_link": str(job.find('link').text),

                })
    return all_vacants_info

def all_jobs():
    all_jobs=[{}]
    requestURL = "https://www.enbek.kz/ru/xml/jooble"
    root = ET.parse(urllib.request.urlopen(requestURL)).getroot()
    for job in root.iter('job'):
        all_jobs.append({

                        'job_name': str(job.find('name').text).replace(", ", "", 1),
                        'job_region': str(job.find('region').text),
                        "job_salary": str(job.find('salary').text),
                        "job_description": str(job.find('description').text).replace("p&gt;", " ")
                                    .replace("li", " ").replace("ul", " ")
                                    .replace("/", " ").replace("&gt;", " ")
                                    .replace("&lt;", " ").replace("ul&gt;", " ")
                                    .replace("/li&gt;", " ").replace("li&gt;", " ")
                                    .replace("-&amp;", " ").replace("nbsp;", " ")
                                    .replace("&amp;", " ").replace("quot;", " ")
                                    .replace("br", " ").replace("strong", " ")
                                    .replace("strong", " ").replace("ol", " "),
                        "job_email": str(job.find('email').text),
                        "job_phone": str(job.find('phone').text),
                        "job_link": str(job.find('link').text),

                    })
    return all_jobs   