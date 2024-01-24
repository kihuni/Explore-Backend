import urllib.request

url = "https://www.example.com"
response = urllib.request.urlopen(url)
data = response.read()

print(data)
