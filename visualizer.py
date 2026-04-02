import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# load data
data = pd.read_csv("processed_data.csv")
data = data.sort_values(by="date")

# create app
app = Dash(__name__)

# layout
app.layout = html.Div([
    html.H1("Pink Morsel Sales Dashboard", style={"textAlign": "center"}),

    dcc.RadioItems(
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        id="region-filter",
        inline=True,
        style={"textAlign": "center", "marginBottom": "20px"}
    ),

    dcc.Graph(id="sales-chart")
])

# callback
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_data = data
    else:
        filtered_data = data[data["region"] == selected_region]

    fig = px.line(filtered_data, x="date", y="sales",
                  title="Sales Trend Over Time")

    return fig

# run app
if __name__ == "__main__":
    app.run(debug=True)