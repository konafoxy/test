import streamlit as st
import time
import random
import plotly.express as px
import pandas as pd


placeholder = st.empty()
start_button = st.empty()

def bar_chart():  
    hours = []
    data = []

    for x in range(24):
        hours.append(x)
        data.append(random.randint(199019238,8237920874))

    df = pd.DataFrame({'hour': hours, 'hits': data})
    fig = px.bar(df, x='hour', y='hits')
    # fig.show()
    placeholder.write(fig)

if start_button.button('Start',key='start'):
    start_button.empty()
    if st.button('Stop',key='stop'):
        pass
    while True:
        bar_chart()
        time.sleep(0.5)