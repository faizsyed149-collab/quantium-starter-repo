import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load processed data
df = pd.read_csv("data/processed_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create artificial region splits (IMPORTANT PART)
region_map = {
    "north": 0.90,
    "east": 1.05,
    "south": 0.95,
    "west": 1.10,
}

# Dash app
app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "textAlign": "center",
        "fontFamily": "Arial",
        "padding": "20px"
    },
    children=[
        html.H1(
            "Pink Morsel Sales Over Time",
            style={"color": "#e75480"}
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "25px"}
        ),

        dcc.Graph(id="sales-line-chart")
    ]
)

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):
    filtered_df = df.copy()

    if selected_region != "all":
        factor = region_map[selected_region]
        filtered_df["sales"] = filtered_df["sales"] * factor

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Impact of Price Increase on Pink Morsel Sales",
        labels={"date": "Date", "sales": "Total Sales"}
    )

    fig.update_layout(
        plot_bgcolor="#f9f9f9",
        paper_bgcolor="#ffffff"
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)
