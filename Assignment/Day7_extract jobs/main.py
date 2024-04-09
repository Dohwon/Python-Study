from bs4 import BeautifulSoup
import requests

def extract_jobs(term):
  url = f"https://remoteok.com/remote-{term}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})

  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    results = []
    jobs = soup.find_all('td', class_= "company position company_and_position")
    # ★ There's no <div>, <class = "jobs">. so I used it.
    job_posts = []

    for job_section in jobs:
      job_posts += job_section.find_all('a')
      #jobs_location += job_section.find_all('span')
      # ★ I want to plus 'region' also, but it tags are diffrent. So I couldn't deal with it.
      for post in job_posts:
        link = post['href']
        company = post.text
        # ★ There's a 'Since today hiring' section, but it is changeable. so Idk how to do handle it.
        # ★ There's no title in post.
      #print(link, company, "/////////////////")
        job_data = {
        'company' : company.strip("\n"),
        'link' : f"https://remoteok.com{link}"
      }
      results.append(job_data)
    results.pop(0)   # ★ except 'Since today hiring'
    for result in results:
      print(result)
      print("/////////////////")

  else:
    print("Can't get jobs.")


extract_jobs("rust")
