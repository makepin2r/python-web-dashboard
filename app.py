from dash import dcc, html, Dash
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children = [
        html.H1(children='Hello Dash'),
        dcc.Graph(
        id='graph1',
        figure=fig
    )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)