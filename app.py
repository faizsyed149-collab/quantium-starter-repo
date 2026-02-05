import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed_data.csv")

# Ensure date column is datetime and sorted
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create Dash app
app = dash.Dash(__name__)

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Impact of Price Increase on Pink Morsel Sales",
    labels={
        "date": "Date",
        "sales": "Total Sales"
    }
)

# App layout
app.layout = html.Div(
    children=[
        html.H1("Pink Morsel Sales Over Time"),
        dcc.Graph(figure=fig)
    ]
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
