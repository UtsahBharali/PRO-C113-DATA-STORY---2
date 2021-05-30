import pandas as pd
import csv
import statistics
import plotly.express as px
import plotly.graph_objects as go

#Uploading the csv
from google.colab import files
data_to_load = files.upload()

#Plotting the graph
df = pd.read_csv("savings_data_final.csv")
fig = px.scatter(df, y="quant_saved", color="rem_any")
fig.show()

with open("savings_data_final.csv",newline="")as f:
  reader = csv.reader(f)
  file_data=list(reader)

#remove the title from the data list 
file_data.pop(0)

#findinf total number of who where reminded and not reminded
total = len(file_data)
total_people_given_reminder=0
for i in file_data:
  if int(i[3])==1:
    total_people_given_reminder=total_people_given_reminder+1

fig=go.Figure(go.Bar(x=["reminded","not reminded"],y=[total_people_given_reminder,(total-total_people_given_reminder)]))
fig.show()    
