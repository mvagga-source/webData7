import requests

url = "https://www.melon.com/"

res = requests.get(url)
res.raise_for_status()

# print(res.status_code)
# print(requests.codes.not_found) # ok, not_found, not_modified

print(res.text)