#!/usr/bin/python
import urllib.request

site = urllib.request.urlopen("http://businesscorp.com.br/")

siteRead = site.read()
siteCode = site.getcode()
siteURL = site.geturl()
siteInfos = site.info()


print("Informações do site:")
print(siteInfos)
print("Status code do site:")
print(siteCode)
print("URL do site:")
print(siteURL)
print("HTML do site:")
print(siteRead)
print("Server do site:")
print(siteInfos["Server"])