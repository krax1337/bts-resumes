import urllib.request
from xml.etree import ElementTree as ET

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



def search(search_type="job_name",search_text="программист 1с"):
    all_jobs_array=all_jobs()
    
    found_job=[{}]
    
    for value in all_jobs_array:
        for key in value:
            if key == search_type and search_text in value[key]:
                found_job.append(value)
                    


    return found_job  
x=search("job_name", "продовец")
