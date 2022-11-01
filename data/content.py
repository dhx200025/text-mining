import urllib.request

url = 'https://www.gutenberg.org/files/76/76-0.txt'
with urllib.request.urlopen(url) as f:
    response = urllib.request.urlopen(url)
    data = response.read()  # a `bytes` object
    text = data.decode('utf-8')
    print(text) # for testing