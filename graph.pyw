import pandas as pd
import plotly.express as px
from paramiko import SSHClient
import socket

# init SSH client and log into server
client = SSHClient()
client.load_system_host_keys()
client.connect('10.0.0.53', username='ubuntu', password='password')

local_machine = socket.gethostname()

remote_path = '/home/ubuntu/net-log/' + local_machine + '.csv'
local_path = '' + local_machine + '.csv'

# init SFTP for file transfer, save to script's location
sftp_client = client.open_sftp()
remote_file = sftp_client.get(remote_path, local_path)

# read and interpret CSV, output scatterplot to localhost
df = pd.read_csv(local_path)
df['date'] = df['date'].map(lambda x: pd.Timestamp(x, unit='s', tz='US/Central'))
figure_1 = px.scatter(df,x = 'date', y = 'latency', title = 'Network Latency')
figure_1.show()




