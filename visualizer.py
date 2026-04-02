import pandas as pd
from dash import Dash,html,dcc
import plotly.express as px

#loading data
data = pd.read_csv("processed_data.csv")
data = data.sort_values(by="date")


#creat app
app = Dash(__name__)

#crear graph
fig = px.line(data,x="date",y="sales",title="Pink Morsel Sales")

#layout
app.layout=html.Div([
    html.H1("Pink Morsel Visualizer"),
    dcc.Graph(figure=fig)
])

#run app
if __name__=="__main__":
    app.run(debug=True)