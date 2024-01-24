import urllib.request

url = "https://www.example.com"
response = urllib.request.urlopen(url)
data = response.read()

decoded_data = data.decode('utf-8')
print(decoded_data)