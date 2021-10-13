import urllib.request

try:
    url = urllib.request.urlopen("https://www.iaeste.de/en/about-iaeste/iaeste-germany/the-local-committees/")
    content = url.read()
    url.close()
except urllib.error.HTTPError:
    print("The web page is not found")
    exit()

f = open("udemy.html", "wb")
f.write(content)
f.close()