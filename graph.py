import pandas as pd
import plotly.express as px

df = pd.read_csv('P:\\repos\\network-monitor\\latency_log.csv')

figure_1 = px.line(df, x = 'date', y = 'latency', title = 'Latency over time')
figure_1.show()


