import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np

file='Product.xlsx'
df= pd.read_excel(file)
#print(df.head())
barc=df['Barcode']
#print(barc[9])

arr=[]
for i in range(26):
  url = 'https://www.google.co.in/search?q='+str(barc[i])+'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj9oe3E8c3aAhVFMo8KHe_hC1oQ_AUIDCgD&biw=1229&bih=587'
#  print(url)
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  images = soup.findAll('img')
  for image in images:
    link = image.get('src')

    #if link:
     # print(link)
    arr.append(link)

    break

print(arr)
df2 = pd.DataFrame(data=arr)


writer = pd.ExcelWriter('output.xlsx')
df.to_excel(writer,'sheet1')
df2.to_excel(writer,'sheet2')
writer.save()