from requests import get

websites = (
  "google.com",
  "airbnb.com",
  "https://twitter.com",
  "facebook.com",
  "http://tiktok.com"
)

results = {}

# or 쓸 때 묶어줘야 하더라...
"""
for website in websites:
  if not (website.startswith("https://") or website.startswith("http://")):
    website = f"https://{website}"
  print(website)    
"""

# 웹사이트 응답 받기 200 == 정상
# results dict에 값 집어넣기
# 200번'대'가 정상인걸로 코드 만들기
for website in websites:
  if not (website.startswith("https://") or website.startswith("http://")):
    website = f"https://{website}"
  response = get(website)
  status = response.status_code
  if status >= 200 and status < 300:
    results[website] = ["OK"]
  elif status >= 300 and status < 400:
    results[website] = ["Redirection"]
  elif status >= 400 and status < 500:
    results[website] = ["Client Error"]
  else:
    results[website] = ["not OK"]
print(results)

