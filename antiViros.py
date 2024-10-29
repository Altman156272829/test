import requests

url = "https://www.virustotal.com/api/v3/files"

files = { "file": ("%D7%90%D7%A0%D7%98%D7%99%D7%92%D7%9F.pdf", open("%D7%90%D7%A0%D7%98%D7%99%D7%92%D7%9F.pdf", "rb"), "application/pdf") }
headers = {
    "accept": "application/json",
    "x-apikey": "<your API key>"
}

response = requests.post(url, files=files, headers=headers)

print(response.text)