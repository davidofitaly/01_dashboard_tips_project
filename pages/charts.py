import pandas as pd
import seaborn as sns
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output
import plotly.graph_objects as go

# LOAD DATASET
tips_data = sns.load_dataset('tips')

# DASH APPLICATION
app = dash.Dash(__name__)

# DROP MENU
dropdown = dcc.Dropdown(
    id='selection-charts',
    options=[
        {'label': '1. scatter -> Total Bill vs Tip (days)', 'value': 'chart1'},
        {'label': '2. scatter -> Total Bill vs Tip (time)', 'value': 'chart2'},
        {'label': '3. scatter -> Tip vs Size (smoker)', 'value': 'chart3'},
        {'label': '4. scatter_matrix -> Scatter Matrix', 'value': 'chart4'},
        {'label': '5. parallel_categories -> Parallel Categories', 'value': 'chart5'},
        {'label': '6. bubble_chart -> Bubble Chart', 'value': 'chart6'},
        {'label': '7. line_chart -> Line Chart (size vs mean_total_bill)', 'value': 'chart7'},
        {'label': '8. bar_chart -> Bar Chart (sex vs mean tip)', 'value': 'chart8'},
        {'label': '9. pie_breast -> Pie Breast (smokers vs non smokers)', 'value': 'chart9'},
        {'label': '10. pie_breast -> Pie Breast (number of bills by part size)', 'value': 'chart10'},
        {'label': '11. histogram -> Histogram (distribution of the variable size', 'value': 'chart11'},
        {'label': '12. histogram -> Histogram (distribution of the variable total_bill)', 'value': 'chart12'},
    ]
)

# APP LAYOUT
app.layout = html.Div([
    dropdown,
    html.Div(id='charts-output')
])


# SCATTER-1
def create_scatter_plot1():
    fig = px.scatter(
        data_frame=tips_data,
        x='total_bill',
        y='tip',
        width=1200,
        height=700,
        color='smoker',
        trendline='ols',
        facet_col='day',
        category_orders={'day': ['Thur', 'Fri', 'Sat', 'Sun']},
        template='ggplot2'
    )
    return fig


# SCATTER-2
def create_scatter_plot2():
    fig = px.scatter(
        data_frame=tips_data,
        x='total_bill',
        y='tip',
        width=1200,
        height=700,
        color='time',
        trendline='ols',
        facet_row='sex',
        category_orders={'day': ['Thur', 'Fri', 'Sat', 'Sun']},
        template='ggplot2'
    )
    return fig


# SCATTER-3
def create_scatter_plot3():
    fig = px.scatter(
        data_frame=tips_data,
        x='tip',
        y='size',
        width=1200,
        height=700,
        color='smoker',
        trendline='ols',
        category_orders={'day': ['Thur', 'Fri', 'Sat', 'Sun']},
        template='ggplot2'
    )
    return fig


# SCATTER-MATRIX
def create_scatter_matrix():
    fig = px.scatter_matrix(
        data_frame=tips_data,
        color='sex',
        dimensions=['total_bill', 'tip', 'size'],
        title='Scatter Matrix',
        template='ggplot2'
    )
    return fig


# PARALLEL_CATEGORIES
def create_parallel_categories():
    fig = px.parallel_categories(
        data_frame=tips_data,
        title='Parallel Categories',
        color='size',
        template='ggplot2'
    )
    return fig


# BUBBLE CHART
def create_bubble_chart():
    fig = px.scatter(
        data_frame=tips_data,
        x='total_bill',
        y='tip',
        size='size',
        hover_name='day',
        color='time',
        labels={'total_bill': 'Total Bill', 'tip': 'Tip', 'size': 'Size'},
        title='Bubble Chart: Total Bill vs. Tip',
        template='ggplot2'
    )
    fig.update_traces(marker=dict(line=dict(color='black', width=1)))
    return fig


# LINE CHART
def create_line_chart():
    mean_total_bill_by_size = tips_data.groupby('size')['total_bill'].mean()
    data_tips_new = pd.DataFrame(mean_total_bill_by_size).reset_index()
    data_tips_new.columns = ['size', 'mean_total_bill']
    fig = px.line(
        data_frame=data_tips_new,
        title='Average Total Bill by Group Size',
        x='size',
        y='mean_total_bill',
        template='ggplot2'
    )
    return fig


# BAR CHART
def create_bar_chart():
    mean_tip_by_sex = tips_data.groupby('sex')['tip'].mean().reset_index()
    fig = px.bar(
        data_frame=mean_tip_by_sex,
        x='sex',
        y='tip',
        title='Mean Tip by Sex',
        labels={'sex': 'Sex', 'tip': 'Mean Tip'},
        template='ggplot2'
    )
    return fig


# PIE BREAST
def create_pie_breast_1():
    smoker_counts = tips_data['smoker'].value_counts()
    smoker_counts_yes = smoker_counts['Yes']
    smoker_counts_no = smoker_counts['No']
    fig = go.Figure(data=[
        go.Pie(labels=['Smoker', 'Non Smokers'],
               values=[smoker_counts_yes, smoker_counts_no]
               )])
    fig.update_layout(title='Smokers vs. Non Smokers', template='ggplot2')
    return fig


# PIE BREAST
def create_pie_breast_2():
    count_by_size = tips_data['size'].value_counts()
    fig = go.Figure(data=[
        go.Pie(labels=count_by_size.index,
               values=count_by_size.values,
               textinfo='percent+label'
               )])
    fig.update_layout(title='Number of Bills by Party Size', template='ggplot2')
    fig.update_traces(textfont_color='black')
    return fig


# HISTOGRAM
def create_histogram_1():
    fig = px.histogram(
        data_frame=tips_data,
        x='size',
        title='Distribution of the Variable Size',
        template='ggplot2',
        histnorm='probability density',
        facet_row='time',
        color='time',
    )
    return fig


# HISTOGRAM
def create_histogram_2():
    fig = px.histogram(
        data_frame=tips_data,
        x='total_bill',
        title='Distribution of the Variable Total Bill',
        template='ggplot2',
        histnorm='probability density',
        facet_row='time',
        color='time'
    )
    return fig


# CALLBACK
@app.callback(
    Output('charts-output', 'children'),
    [Input('selection-charts', 'value')]
)
def update_charts(select):
    if select == 'chart1':
        return dcc.Graph(figure=create_scatter_plot1())
    elif select == 'chart2':
        return dcc.Graph(figure=create_scatter_plot2())
    elif select == 'chart3':
        return dcc.Graph(figure=create_scatter_plot3())
    elif select == 'chart4':
        return dcc.Graph(figure=create_scatter_matrix())
    elif select == 'chart5':
        return dcc.Graph(figure=create_parallel_categories())
    elif select == 'chart6':
        return dcc.Graph(figure=create_bubble_chart())
    elif select == 'chart7':
        return dcc.Graph(figure=create_line_chart())
    elif select == 'chart8':
        return dcc.Graph(figure=create_bar_chart())
    elif select == 'chart9':
        return dcc.Graph(figure=create_pie_breast_1())
    elif select == 'chart10':
        return dcc.Graph(figure=create_pie_breast_2())
    elif select == 'chart11':
        return dcc.Graph(figure=create_histogram_1())
    elif select == 'chart12':
        return dcc.Graph(figure=create_histogram_2())


if __name__ == '__main__':
    app.run_server(debug=True, port=8000)
