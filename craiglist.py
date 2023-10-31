import requests
from bs4 import BeautifulSoup
import pandas as pd

payload = {
   'source': 'universal',
   'url': 'https://sfbay.craigslist.org/search/fua?hasPic=1',
   'render': 'html'
}

response = requests.request(
   'POST',
   'https://realtime.oxylabs.io/v1/queries',
   auth=('caroarriaga', 'N3wPassword'),
   json=payload,

)
print(response.json())
result = response.json()['results']
htmlContent = result[0]['content']

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(htmlContent, 'html.parser')

# Extract prices, titles, and descriptions from Craigslist listings
listings = soup.find_all('li', class_='cl-search-result cl-search-view-mode-gallery')

df = pd.DataFrame(columns=["Product Title", "Description", "Price"
                           , "Image Source"
                           ])

for listing in listings[:300]:
   # Extract price
   p = listing.find('span', class_='priceinfo')
   if p:
       price = p.text
   else:
       price = ""


   # Extract title
   title = listing.find('a', class_='cl-app-anchor text-only posting-title').text
   url = listing.find('a', class_='cl-app-anchor text-only posting-title').get('href')


   detailResp = requests.get(url).text

   detailSoup = BeautifulSoup(detailResp, 'html.parser')
   
   description_element = detailSoup.find('section', id='postingbody')
   description = ''.join(description_element.find_all(string=True, recursive=False))

   image_element = detailSoup.find('div', class_="swipe-wrap")
   image_source= image_element.find('img').get('src')

   df = pd.concat(
       [pd.DataFrame([[title, description.strip(), price, image_source]], columns=df.columns), df],
       ignore_index=True,
   )

df.to_csv("craigslistproject/craiglist_results.csv", index=False)
df.to_json("craigslistproject/craiglist_results.json", orient="split", index=False)