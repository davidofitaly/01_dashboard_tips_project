import dash
from dash import html, dcc
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# Zaimportuj kod z pliku charts.py
from pages.charts import app as charts_app

# Załaduj zestaw narzędzi
px.defaults.template = "ggplot2"
external_css = ["https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css", ]

# Utwórz główny Dash app
app = dash.Dash(__name__, pages_folder='pages', use_pages=True, external_stylesheets=external_css)

# Dodaj stronę dla wykresów
dash.register_page('pages.charts', path='/charts', name='Charts 📊')

# Załaduj layout z pliku charts.py
app.layout = charts_app.layout

# Załaduj callback z pliku charts.py
@app.callback(
    Output('charts-output', 'children'),
    [Input('selection-charts', 'value')]
)
def update_charts(select):
    return charts_app.update_charts(select)

if __name__ == '__main__':
    app.run_server(debug=True, port=8009)
