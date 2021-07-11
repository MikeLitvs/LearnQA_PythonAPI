import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
if response.history:
    for resp in response.history:
        print(resp.url)
    print(response.url)
else:
    print("Request was not redirected")