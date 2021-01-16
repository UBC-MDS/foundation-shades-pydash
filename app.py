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
    # row 2: 2 histograms side by side
    html.Div(
        [
            html.Div(
                [
                    html.H6('Best Seller Shades by Countries:'),
                    dcc.Dropdown(
                            id = 'dropdown_best_seller_shades_by_countries',
                            options = [{'label': country, 'value': country} for country in unique_countries],
                            value = unique_countries,
                            multi=True
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
    )
],
className='ten columns offset-by-half')

if __name__ == '__main__':
    app.run_server(debug=True)