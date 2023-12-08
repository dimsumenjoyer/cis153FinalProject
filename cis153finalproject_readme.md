Victor Van
00319912
CIS153: Final Project
11/28/2023, Due: 12/17/2023

Instructions to use project:
Download the relevant dataset, which is listed below.
Also download matplotlib.pyplot and pandas. These libraries don't come with python by default.
https://pandas.pydata.org/
https://matplotlib.org/stable/users/installing/index.html

Future Work:
I'd like to use live COVID-19 data, my data is outdated and cannot be regularly updated. I'd have to use an API.

This is where I got my datasets:
https://www.kaggle.com/datasets/imdevskp/corona-virus-report

This is the specific dataset that I used:
usa_county_wise.csv

Libraries used:
-matplotlib.pyplot
-pandas

External Resources:
https://matplotlib.org/stable/users/index.html
https://pandas.pydata.org/docs/user_guide/index.html#user-guide
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sum.html

I used usa_county_wise.csv as my dataset, which has 15 columns and 627,921 rows.
I also defined a new column of data called "recoveries", so I was working with 16 columns.
Therefore, I worked with 10,046,736 pieces of data.

I basically just plotted infections, deaths, and recoveries in America overtime. This project is just a graph with extra steps.

The covid_dataframe opens up the file with the pandas library, where I would be able to pick any columns needed.

The functions of covid_data_dates, covid_data_infected, covid_data_deaths, covid_data_recovered defines what data is used.

In that csv file, it contains data on COVID-19 cases in every county in America everyday from about Janurary 2020 to August 2020.
Because of that, there are duplicate dates. I stored the dates into the variable unordered_dates which is a set which eliminates duplicated items. Then it gets stored in the variable dates which is a list via a list comprehension and sorts it.

The function plot_covid_data plots the data. In the file meant for in-class submission, the function main plots the data depending on what option the user chooses.

I also made two files: cis153finalproject.py and covid_data_visualization.py.
For the class submission, I needed to meet some arbitrary requirements so I had to add a while loop and if statement.
For my purposes, plotting all of the data is fine.