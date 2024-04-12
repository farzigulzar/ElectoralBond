import pandas as pd
import numpy as np
from pathlib import Path
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import seaborn as  sns
import datetime as dt
import streamlit as st
# from streamlit_echarts import st_echarts

st. set_page_config(layout="wide")

filepath = Path('Cleaned_merged_data\\electoral.csv')
df = pd.read_csv(filepath)

# def plot_pie_chart(denom_):
#     # denom_
#     # denom_.index
#     options = {
#         "tooltip": {"trigger": "item"},
#         "legend": {"orient":"vertical", "type":"scroll","left": "left"},
#         # "grid": {"right": "10%", "containLabel": False}, 
#         "series": [
#             {
#                 "name": "Pie chart",
#                 "type": "pie",
#                 "radius": ["40%", "70%"],
#                 "avoidLabelOverlap": False,
#                 "itemStyle": {
#                     "borderRadius": 10,
#                     "borderColor": "#fff",
#                     "borderWidth": 2,
#                 },
#                 "label": {"show": False, "position": "center"},
#                 "emphasis": {
#                     "label": {"show": True, "fontSize": "20", "fontWeight": "bold"}
#                 },
#                 "labelLine": {"show": False},
#                 "data": denom_.to_dict('records'),
#             }
#         ],
#     }


#     st_echarts(
#         options=options, height="600px", width="1500px"
#     )



denom_ = df[['Name of the Political Party', 'Denominations']].groupby('Name of the Political Party').sum().sort_values(by='Denominations',ascending=False)
denom_['Percentage'] = (100*denom_['Denominations']/denom_['Denominations'].sum())
denom_ = denom_.reset_index().drop('Percentage', axis=1).set_axis(['name', 'value'], axis=1)
denom_
# plot_pie_chart(denom_)

with st.container(height=600, ):
    use_container_width=True
    # plot_pie_chart(denom_)
st.write("ASD")