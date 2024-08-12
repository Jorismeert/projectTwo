import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents
import io, json

# import ssl

# ssl._create_default_https_context = ssl._create_stdlib_context

url = "https://en.wikipedia.org/wiki/100_great_paintings_from_Duccio_to_Picasso"
# get the response in the form of html

table_class="wikitable sortable jquery-tablesorter"
response=requests.get(url)
print(response.status_code)

# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})
print(type(indiatable))

df=pd.read_html(io.StringIO(str(indiatable)))
# convert list to dataframe
df=pd.DataFrame(df[0])
print(df.head(2))


df1 = df[[ 'Article','Painter',]]
print(df1)

paintings = dict(zip(df1.iloc[:, 0], df1.iloc[:, 1]))
# elements = df.set_index('Naam')[['symbool', 'Atoom­nummer']].apply(tuple, axis=1).to_dict()
print(paintings)

with open("jsonFiles/famousPaintings.json", "w") as outfile: 
        json.dump(paintings, outfile, indent = 4)

