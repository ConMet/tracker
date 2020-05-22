from django.shortcuts import render
from django.http import HttpResponse
from scrape.models import WebScrape

import pandas as pd
import matplotlib

import plotly.offline as py
import plotly.graph_objs as go
import plotly.express as px


# This function exists to avoid redundancy in writing different views that have a similar purpose.
def createdf():
    # Instantiate WebScrape model, taking live values from database
    # and putting them back into a pandas dataframe.
    df = pd.DataFrame(list(WebScrape.objects.all().values()))

    # Use to_numberic and to_datetime pandas methods for coercing cases, deaths,
    # and date values to their proper data types (for use in plotting and analysis).
    df[['cases', 'deaths']] = df[['cases', 'deaths']].apply(pd.to_numeric)
    df[['date']] = df[['date']].apply(pd.to_datetime)

    # Homogenizing rows with daily totals.
    df['counties'] = df['counties'].replace({'GrandTotal': 'Totals'})

    return df


# This view renders the default graph when on the website homepage.
def homepage(request):
    df = createdf()

    # Makes a data frame consisting exclusively of daily totals.
    totals = df.loc[df['counties'] == 'Totals']

    plot = px.line(totals, x='date', y='cases')

    graph = plot.to_html(
        full_html=False, default_height=500, default_width=800)
    context = {'graph': graph}
    response = render(request, 'homepage.html', context)

    return response


# This view renders a graph of deaths over time.
def deathview(request):
    df = createdf()

    # Makes a data frame consisting of daily death totals.
    death_totals = df.loc[df['counties'] == 'Totals']

    plot = px.line(death_totals, x='date', y='deaths')

    graph = plot.to_html(
        full_html=False, default_height=500, default_width=800)
    context = {'deathgraph': deathgraph}
    response = render(request, 'homepage.html', context)

    return response
