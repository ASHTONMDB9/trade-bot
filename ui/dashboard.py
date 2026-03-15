import streamlit as st
import pandas as pd
from bot import get_prices

st.title("Crypto Arbitrage Bot")

st.write("Live Market Data")

prices = get_prices()

df = pd.DataFrame(
    list(prices.items()),
    columns=["Pair", "Price"]
)

st.dataframe(df)

st.write("Bot Status")

if st.button("Start Bot"):
    st.write("Bot Running")

if st.button("Stop Bot"):
    st.write("Bot Stopped")