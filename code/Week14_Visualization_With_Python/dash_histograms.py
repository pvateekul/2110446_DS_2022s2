from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

iris = pd.read_csv('iris.csv')

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Slider(id="bins", min=1, max=10, value=2, step=1,
               marks={str(x):str(x) for x in range(1,11)})
])

@app.callback(
    Output('graph', 'figure'), 
    Input(component_id='bins', component_property='value'))
def update_figure(bins):
    fig = px.histogram(iris, x='PetalLengthCm', nbins=bins)
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
