import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State

# launch app with customer css
app = dash.Dash(__name__)
app.title = 'Foundation Shades Across the Globe'
shades = pd.read_csv("./data/shades_processed.csv") # read processed data
df = px.data.tips() # delete this next week
unique_countries = shades.country.unique()
server = app.server

"""
Dashboard layout
"""
app.layout = html.Div([
    # row 1: app title and app description
    html.Div(
        [
            html.H2(children='Foundation Shades Across the Globe',
                    className='nine columns'),
            html.Div(children='''
                    What is the range and distribution of makeup foundations shades \
                    offered by each of the best-selling cosmetics brands across the globe
                    ''',
                    className='ten columns',
                    style={'marginLeft': 0}
            )
        ], 
        className="row"
    ),
    # row 2: 2 titles and control side by side
    html.Div(
        [
            html.Div(
                [
                    html.H6('Best Seller Shades by Countries:'),
                    dcc.Dropdown(
                            id = 'dropdown_best_seller_shades_by_countries',
                            options = [{'label': country, 'value': country} for country in unique_countries],
                            value = unique_countries,
                            multi = True
                    ),
                ],
                className="six columns"
            ),
            html.Div(
                [
                    html.H6('Best-selling brands by country:'),
                    dcc.RadioItems(
                        id = 'radio_button_best_selling_brand_by_country',
                        options = [{'label': country, 'value': country} for country in unique_countries],
                        value = 'US',
                        labelStyle = {'display': 'inline-block'}
                    )                 
                ],
                className="five columns offset-by-half"
            )
        ],
        className="row"
    ),
    # row 3: 2 histograms side by side
    html.Div(
        [
            html.Div(
                [
                    dcc.Graph(
                        id='histogram_best_seller_by_country',
                        #figure=px.histogram(df, x="total_bill")
                    )
                ],
                className="six columns"
            ),
            html.Div(
                [
                    dcc.Graph(
                        id='histogram_best_seller_brand_by_country',
                        figure = px.histogram(df, x="total_bill")
                    )
                ],
                className="six columns"
            ),
        ],
        className="row"
    )
],
className='ten columns offset-by-half')

@app.callback(
    Output("histogram_best_seller_by_country", "figure"), 
    [Input("dropdown_best_seller_shades_by_countries", "value")])
    
def country_filter(value):
    if type(value) != list: value = [value]
    data_filtered = shades.loc[shades['country'].isin(value)]
    fig = px.histogram(data_filtered, x="L", color = "country", nbins=10, range_x=[0,100], range_y=[0,120])
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)