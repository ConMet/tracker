import requests
import re
import datetime
import pandas as pd
from bs4 import BeautifulSoup


class Scrape():

    def __init__(self, date, county, cases, deaths):
        self.date()
        self.county()
        self.cases()
        self.deaths()

    def scrapedata():
        # Collect and parse page, make soup object.
        page_url = 'https://www.michigan.gov/coronavirus/0,9753,7-406-98163_98173---,00.html'
        page = requests.get(page_url)
        soup = BeautifulSoup(page.text, 'html.parser')

        # Sift through soup object for proper data containing div.
        # Loop through our new soup object for table contents.
        # Regex for cleaning out unnecessary spacing.
        soup2 = soup.find('div', {'class': 'fullContent'})
        for item in soup2.findAll('tbody'):
            data = re.sub(r'\n\s*\n', r'\n\n',
                          item.get_text().strip(), flags=re.M)

        # Regex for all table data placed in an ordered list:
        # Removing spaces (ex. St Clair --> StClair) due to string method difficulty in future loop.
        dataList = re.findall(r"^\w*.+[a-zA-Z+]|\d+", data, re.MULTILINE)
        newDataList = [y.replace(' ', '') for y in dataList]

        date, county, cases, deaths = [], [], [], []
        # Create index alongside the listed data created above.
        # Loop through and populate lists corresponding to the column they belong in.
        for index, x in enumerate(newDataList):
            if x.isalpha():
                county.append(x)
                if newDataList[index-1].isnumeric() and newDataList[index-2].isalpha():
                    deaths.append('0')
            if x.isnumeric():
                if newDataList[index-1].isnumeric():
                    deaths.append(x)
                elif newDataList[index-1].isalpha():
                    cases.append(x)

        # Loop for populating date column with date the data was scraped.
        dateobj = datetime.datetime.now()
        for z in county:
            date.append(dateobj.strftime('%m/%d/%Y'))
        return date, county, cases, deaths

    # Function that returns a data structure more easily iterable and saved to a database.
    def clean_scrape():
        list_of_tuples = Scrape.scrapedata()
        list_of_lists = [list(elem) for elem in list_of_tuples]

        # Zipping data together into tuples for easier database entry.
        output = list(
            zip(list_of_lists[0], list_of_lists[1], list_of_lists[2], list_of_lists[3]))

        return output

    # Function that returns a data frame of the data that was only just now scraped. Largely unused.
    def pandadata():
        date, county, cases, deaths = Scrape.scrapedata()
        # Create data frame
        df = pd.DataFrame(
            {'Date': date,
             'Counties': county,
             'Cases': cases,
             'Deaths': deaths
             })
        return df
