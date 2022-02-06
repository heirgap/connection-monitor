import pandas as pd
import plotly.express as px
import datetime


df = pd.read_csv('latency_log.csv')
df['date '] = df['date '].map(lambda x: pd.Timestamp(x, unit='s', tz='US/Central'))
figure_1 = px.scatter(df,x = 'date ', y = 'latency', title = 'Network Latency')
figure_1.show()




