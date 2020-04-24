import pandas as pd
from scrape import *

# Call scrape function to populate our columns
county, cases, deaths = scrape()

# Create data frame
df = pd.DataFrame(
    {'Counties': county,
     'Cases': cases,
     'Deaths': deaths
     })

print(df)
