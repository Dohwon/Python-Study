import requests
from bs4 import BeautifulSoup


def extract_wwr_jobs(keyword):
  base_url = "https://weworkremotely.com/remote-jobs/search?term="

  response = requests.get(f"{base_url}{keyword}")
  if response.status_code != 200:  #홈페이지를 긁어올 수 없을 때는 문구를 출력함
    print("Can't request website")
  else:
    results = []  # 결과값을 저장하기 위한 새로운 변수
    soup = BeautifulSoup(response.text, "html.parser")
    #print(response.text)  # .text는 홈페이지를 HTML text로 보여줌
    #print(soup.find_all('section', class_="jobs"))  # 잘 나오나 프린트 해봄
    jobs = soup.find_all('section', class_="jobs")  # section 내에 jobs만 출력
    # class에 _가 붙은 이유는 파이썬에서 이미 class를 사용하고 있기 때문에 변수로 활용할 수 없어서임
    #print(len(jobs))   # len함수 소개
    for job_section in jobs:
      #print(job_section.find_all('li'))  # 잘 나오나 프린트 해봄
      job_posts = job_section.find_all('li')  # jobs 내의 리스트만 출력
      job_posts.pop(-1)  # 마지막에 view_all 이 있어서 지워줌
      for post in job_posts:
        #print(post)   # 포스트만 보길 원함
        #print("/////////////////////////")  # 포스트를 분리해서 보기 위함
        anchors = post.find_all('a')
        anchor = anchors[1]
        link = anchor['href']  # <a href>만 가져오기 위
        company, kind, region = anchor.find_all(
            'span', class_="company")  # company가 3개라 변수명 바꿔줌
        #print(company, kind, region)  #잘 나오나 출력해봄
        title = anchor.find('span', class_="title")  # 타이틀을 붙여줌
        #print(company, kind, region, title)  #잘 나오나 출력해봄
        #print(company.string, kind.string, region.string, title.string)  # 잘 나오나 출력해봄, .string은 태그 빼고 문자만 보여
        job_data = {
            'link': f"https://weworkremotely.com/{link}",
            'company': company.string,
            'region': region.string,
            'position': title.string
        }
        results.append(job_data)
    #print(result)  # 잘 나오나 출력해봄
    #for result in results:    # 구분자 추가하기 위해 for문 추가 사용
    #print(result)
    #print("/////////////////////")
    return results
