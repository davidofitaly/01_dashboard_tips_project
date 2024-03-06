import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

# Tworzenie układu strony głównej
default_page_layout = html.Div()

# Rejestracja strony głównej
dash.register_page("default_page", path='/', name='Main Site 🌍', layout=default_page_layout)

