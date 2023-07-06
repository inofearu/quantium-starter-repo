from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

data = (
    pd.read_csv("C:/Users/Inofearu/Desktop/Work/Work Experience/quantium-starter-repo/data/merged_sales_data.csv")
    .assign(date=lambda data: pd.to_datetime(data["date"], format="%Y-%m-%d"))
    .sort_values(by="date")
)

app = Dash(__name__)

app.layout = html.Div(
    style={"display": "flex", "flex-direction": "column", "align-items": "center", "backgroundColor": "#666699"},
    children=[
        dcc.Graph(
            id='sales_graph',
        ),
        html.Div(
            style={"padding": "2px", "text-align": "center", "border": "solid 2px #000000", "background-color" : "#FF00FF", "color": "black"}, 
            children=[
                html.H3(
                    'Graph Settings:',
                    style={"margin": "2px 5px", "color": "black"}
                ),
                dcc.RadioItems(
                    id='region_filter',
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"}
                    ],
                    labelStyle={"display": "flex", "align-items": "center", "padding": "0px 16px", "color": "black"}
                ),
            ],
        )
    ],
)

@app.callback(
    Output('sales_graph', 'figure'),
    [Input('region_filter', 'value')]
)
def update_graph(region):
    if region == "all":
        filtered_data = data
    else:
        filtered_data = data[data['region'] == region]
    fig = px.line(filtered_data, x="date", y="sales", title="A graph to compare sales to time.")
    fig.update_layout(xaxis_title="Date", yaxis_title="Sales")
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
