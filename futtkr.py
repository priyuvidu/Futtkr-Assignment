from google_images_download import google_images_download   #importing the library
import pandas as pd
response = google_images_download.googleimagesdownload()   #class instantiation

file='Product.xlsx'
df= pd.read_excel(file)
print(df.head())
barc=df['Barcode']
print(barc[9])




arguments = {"keywords":barc[],"limit":1,"print_urls":True}   #creating list of arguments
response.download(arguments)


