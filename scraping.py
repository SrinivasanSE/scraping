from bs4 import BeautifulSoup
import requests
import time


def get_jobs():
    html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=").content
    soup = BeautifulSoup(html_text, "html.parser")
    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")

    for index,job in enumerate(jobs):
        added_at = job.find("span", class_ = "sim-posted").span.text.replace(" ","")
        if "few" in added_at:
            company_name = job.find(class_ = "joblist-comp-name").text 
            ul = job.find("ul", class_ = "list-job-dtl clearfix")
            li  = ul.find_all("li")[0]
            job_description = li.get_text().replace(" ","")
            skills = ul.find("span",class_="srp-skills").get_text().replace(" ","")
            added_at = job.find("span", class_ = "sim-posted").span.text.replace(" ","")
            more_info = job.header.h2.a['href']
            with open(f'jobs/{index}.txt', 'w') as f:
                f.write(f'Company Name: {company_name} \n')
                f.write(f'{job_description} \n')
                f.write(f'Skills : {skills} \n')
                f.write(f'Published at: {added_at} \n')
                f.write(f'More Info: {more_info} \n')
                print('File saved', index)

if __name__ == "__main__":
    while True:
        get_jobs()
        time_wait = 5
        time.sleep(time_wait*60)
