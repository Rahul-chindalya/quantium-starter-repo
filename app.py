import dash
from dash import html
import pandas as pd

app = dash.Dash(__name__)

# Sample data
data = {
    "Month": ["Jan", "Feb", "Mar"],
    "Sales": [100, 200, 150]
}
df = pd.DataFrame(data)

app.layout = html.Div([
    html.H1("Quantium Sales Dashboard"),
    html.P("Basic dashboard created using Dash"),

    html.H3("Sample Data"),
    html.Ul([html.Li(f"{row['Month']} : {row['Sales']}") for _, row in df.iterrows()])
])

if __name__ == "__main__":
    app.run(debug=True)