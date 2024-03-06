import dash
from dash import dcc, html
import plotly.graph_objects as go
from dash.dependencies import Input, Output

external_stylesheets = ['/css/style.css']
dash.register_page(__name__, path='/introduction', name='Introduction 😉', external_stylesheets=external_stylesheets)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("Tips Dataset Overview"),
        "The 'Tips' dataset contains information about tips given to waiters/waitresses in restaurants.",
        html.Br(),html.Br(),
        "This dataset is often used to analyze tipping behavior and to study factors that may influence the amount of tip given.",
        html.Br(), html.Br(),
        "Let's explore some of the key variables in this dataset.",
    ]),
    html.Div(children=[
        html.Br(),
        html.H2("Data Variables"),
        html.B("total_bill: "), "Total bill amount",
        html.Br(),
        html.B("tip: "), "Tip amount",
        html.Br(),
        html.B("sex: "), "Sex of the person paying the bill",
        html.Br(),
        html.B("smoker: "), "Whether the party included smokers or not",
        html.Br(),
        html.B("day: "), "Day of the week",
        html.Br(),
        html.B("time: "), "Time of the meal (Lunch/Dinner)",
        html.Br(),
        html.B("size: "), "Size of the party",
    ])
], className="bg-light p-3 m-3")