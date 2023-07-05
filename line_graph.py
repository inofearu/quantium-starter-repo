from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

data = (
    pd.read_csv("C:/Users/Inofearu/Desktop/Work/Work Experience/quantium-starter-repo/data/merged_sales_data.csv")
    .assign(date=lambda data: pd.to_datetime(data["date"], format="%Y-%m-%d"))
    .sort_values(by="date")
)


app = Dash(__name__)


app.layout = html.Div(
    children = [
        dcc.Graph(
            figure = {
                "data" : [
                    {
                        "y": data["sales"],
                        "x" : data["date"],
                        "type" : "lines",
                    },
                ],
                "layout" : {
                    "title" : "A graph to compare sales to time.",
                    "xaxis" : {
                        "title" : "Date"
                    },
                    "yaxis" : {
                        "title" : "Sales"
                    }
                },
            },
        ),
    ]
    
)
if __name__ == "__main__":
    app.run_server(debug=True)