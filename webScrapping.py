from bs4 import BeautifulSoup
import requests
import time

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text


#print(html_text)

soup = BeautifulSoup(html_text,'lxml')
#jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# here we are only selecting the first result , remember that you can use it as an object
#job = soup.find('li', class_='clearfix job-bx wht-shd-bx')

# printing the list of jobs

#print(job)

# instead of use soup, this time we will use job because is where we want to focus
#company_name = job.find('h3', class_='joblist-comp-name').text.replace(" ","")
#skills = job.find('span',class_='srp-skills').text.replace(" ","")
#job_date = job.find('span', class_='sim-posted').span.text

#print(company_name)
#print(skills)

#print(f'''
#Company Name: {company_name} - skills: {skills} - Date: {job_date}
# ''')

#print(job_date)

##########################################

# Now doing exactly the same but with all the jobs, creating a for loop to display each result

def find_jobs():
    print("Write unfamiliar skills to filter between different jobs")
    unfamiliar_skill = input(">")
    print("filtering results")

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        job_date = job.find('span', class_='sim-posted').span.text

        if "few" in job_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(" ","")
            skills = job.find('span',class_='srp-skills').text.replace(" ","")
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                print(f'Company Name: {company_name.strip()}') # strip is the same that trim()
                print(f'skills: {skills.strip()}')
                print(f'more info: {more_info}\n')
                print("")

    
        


#find_jobs()

if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait*60) # 10 min

 
