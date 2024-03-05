import dash
from dash import dash_table
from dash import html
import seaborn as sns

dash.register_page(__name__, path='/tips_table', name='Dataset 📋')

# LOAD DATASET
tips_data = sns.load_dataset('tips')

# PAGE LAYOUT
layout = html.Div(
    children=[
        html.Br(),
        dash_table.DataTable(
            columns=[{'name': col, 'id': col, 'type': 'numeric' if tips_data[col].dtype.kind in 'biufc' else 'text'}
                     for col in tips_data.columns],
            data=tips_data.to_dict('records'),
            editable=True,
            filter_action='native',
            sort_action='native',
            page_action='native',
            page_current=0,
            page_size=20,
            column_selectable='multi',
            row_selectable='multi',
            style_table={'overflowX': 'auto'},
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold'
            },
            style_cell={
                'height': 'auto',
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                }
            ]
        )
    ]
)


