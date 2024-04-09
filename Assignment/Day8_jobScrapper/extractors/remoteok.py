from bs4 import BeautifulSoup
import requests


def extract_remoteok_jobs(keyword):
  #term = 'python'
  url = f"https://remoteok.com/remote-{keyword}-jobs"
  request = requests.get(url, headers={"User-Agent": "Kimchi"})

  results = []

  if request.status_code == 200:
    soup = BeautifulSoup(request.text, "html.parser")
    jobs = soup.find_all('tr', class_="job")
    for job in jobs:
      company = job.find("h3", itemprop="name")
      position = job.find("h2", itemprop="title")
      region = job.find("div", class_="location")
      anchors = job.find_all('a')
      anchor = anchors[1]
      link = anchor['href']
      #print(link)

      #print(company, position, region,"\n")

      if company:
        company = company.string.strip()
      if position:
        position = position.string.strip()
      if region:
        region = region.string.strip()
      if company and position and region:
        job = {
            'link': f"https://remoteok.com/{link}",
            'company': company,
            'region': region,
            'position': position
        }
        results.append(job)
      else:
        print("Can't get jobs")
      return results

