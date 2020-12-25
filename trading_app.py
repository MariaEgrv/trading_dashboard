import streamlit as st
import pandas as pd
import numpy as np
import requests
from pandas import json_normalize
import matplotlib.pyplot as plt
import plotly.express as px
import json

st.title('Earnings data')


token = "Tpk_6deca100bca34e349bfcee233e99d66a"

def get_symbols():
    symbols = requests.get("https://sandbox.iexapis.com/stable/ref-data/symbols",
                            params={
                            "token": token,
                            }
                        )
    return symbols.json()

raw_symbols = get_symbols()

symbols = [symbol['symbol'] for symbol in raw_symbols]

#st.write(type(symbols))

option = st.selectbox('What is the symbol of the stock?', symbols)
#st.write('You selected:', option)

api_key = "MTR40FAMHPUR84HF"


# def get_data():
#     data = requests.get("https://www.alphavantage.co/query",
#                             params={
#                             "function": 'EARNINGS',
#                             "symbol": option,
#                             "apikey": api_key,
#                             }
#                         )
#     return data.json()

def get_data():
    data = requests.get(f"https://sandbox.iexapis.com/stable/stock/{option}/earnings",
                            params={
                            'last' : '4',
                            "token": token,
                            }
                        )
    return data.json()


raw_df = get_data()
df_earnings = json_normalize(raw_df['earnings'])

df_earnings_sorted = df_earnings.sort_values(by='EPSReportDate')

fig = px.bar(x=df_earnings_sorted['EPSReportDate'], y=df_earnings_sorted['actualEPS'])

st.write(df_earnings_sorted)

st.write(fig)

