import requests
from bs4 import BeautifulSoup
import re

# Collect and parse page, make soup object.
page_url = 'https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html'
page = requests.get(page_url)
soup = BeautifulSoup(page.text, 'html.parser')

# Sift through soup object for proper data containing div.
# Loop through our new soup object for table contents.
# Regex for cleaning out unnecessary spacing.
soup2 = soup.find('div', {'class': 'fullContent'})
for item in soup2.findAll('tbody'):
    data = re.sub(r'\n\s*\n', r'\n\n', item.get_text().strip(), flags=re.M)


# Create lists corresponding to data above.
county = re.findall(r"([A-Z+][a-z+].+)$", data)

confirmed = []
deaths = []

# regex for county names from cleaned data
# r"(\w*[A-Z]\w*[A-Z]\w*\*+)|([A-Z+][a-z+].+)$", i)

print(county)
