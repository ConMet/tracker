import pandas as pd
from scrape import *
import datetime


# ***Need to schedule scrape to call on a daily basis.***

# Call scrape function to populate our columns
date, county, cases, deaths = scrape()

# Create data frame
df = pd.DataFrame(
    {'Date': date,
     'Counties': county,
     'Cases': cases,
     'Deaths': deaths
     })

print(df)
