from colorutils import Color 
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
from math import sqrt
import numpy as np

# launch app with customer css
app = dash.Dash(__name__)
app.title = 'Foundation Shades Across the Globe'
shades = pd.read_csv("./data/shades_processed.csv") # read processed data
shades['hex'] = '#' + shades['hex'] # add # symbol for displaying color
df = px.data.tips()  # delete this next week
unique_countries = shades.country.unique()
server = app.server

# function to calculate the distance between 2 points
def distance(p1, p2):
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2]) ** 2)

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
                        figure=px.histogram(df, x="total_bill")
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
    ),
    # row 4: 1 title and 1 dropdown control underneath
    html.Div(
        [
            html.Div(
                [
                    html.H6('Finding the Top 5 Similar Foundations by HSV:'),
                    dcc.Dropdown(
                        id='dropdown_top_5_similar_foundation_by_countries',
                        options=[{'label': country, 'value': country } for country in unique_countries],
                        value=unique_countries,
                        multi=True
                    )
                ],
                className="six columns"
            ),
        ], 
        className="row"
    ),
    # row 5: 3 titles and 3 sliders control underneath
    html.Div(
        [
            html.Div(
                [
                    html.H6("Hue"),
                    dcc.Slider(
                        id='slider_hue', 
                        min=0, max=50, step=1, 
                        value=29,
                        marks={0: '0°', 10: '10°', 20: '20°', 30: '30°', 
                              40: '40°', 50: '50°'},
                    )
                ],
                className="three columns"
            ),
            html.Div(
                [
                    html.H6("Saturation"),
                    dcc.Slider(
                        id='slider_saturation',
                        min=0, max=1, step=0.01,
                        value=0.53,
                        marks={0: '0', 0.2: '0.2', 0.4: '0.4', 
                               0.6: '0.6', 0.8: '0.8', 1: '1'}
                    )
                ],
                className="three columns"
            ),
            html.Div(
                [
                    html.H6("Value/Brightness"),
                    dcc.Slider(
                        id='slider_value_brightness',
                        min=0.2, max=1, step=0.01,
                        value=0.7,
                        marks={ 0.2: '0.2', 0.6: '0.6', 1: '1'}
                    )
                ],
                className="three columns"
            ),
        ],
        className="row",
    ),
    # row 6: 1 sub title
    html.Div(
        [
            html.Div(
                [
                    html.P(id='HSV_user_choice_output'),
                    html.Div(id="user_selected_color_div"),
                    html.H6("Most Matching Results:")
                ],
                className='six columns',
            )
        ],
        className="row"
    ),
    # row 7: 5 top similar products
    html.Br(),
    html.Div(
        [
            html.Div(
                [
                    html.H1(id='match_1'),
                    html.P(id='match_1_text')
                ], 
                className = "two columns"
            ),
            html.Div(
                [
                    html.H1(id='match_2',
                        style = {'backgroundColor':'blue', 
                                    "height": "150px", 
                                    "width": "150px",
                                    "borderRadius": "15px"},
                        ),
                    html.P(id='match_2_text')
                ], 
                className = "two columns"
            ),
            html.Div(
                [
                    html.H1(id='match_3'),
                    html.P(id='match_3_text')
                ], 
                className = "two columns"
            ),
            html.Div(
                [
                    html.H1(id='match_4'),
                    html.P(id='match_4_text')
                ], 
                className = "two columns"
            ),
            html.Div(
                [
                    html.H1(id='match_5'),
                    html.P(id='match_5_text')
                ], 
                className = "two columns"
            ),
        ],
        className="row"
    ), 
],
className='ten columns offset-by-half')

# callback for displaying user selection
@app.callback(
    Output('HSV_user_choice_output', 'children'),
    Output('user_selected_color_div', 'style'),
    Input('slider_hue', 'value'),
    Input('slider_saturation', 'value'),
    Input('slider_value_brightness', 'value'))
def display_user_HSV_option(H, S, V):
    # output string for displaying user choice
    hex_color = Color(hsv=(H, S, V)).hex
    output_string = "You selected HSV value of H:" + \
        str(H) + ", S: " + str(S) + ", and V: " + str(V) + \
        " (Hex code: " + hex_color + ")"

    # style change for div
    style = {"backgroundColor": hex_color,
            "height": "50px", 
            "width": "100px"}
    return output_string, style

# callback for displaying most simliar color names
@app.callback(
    Output('match_1_text', 'children'),
    Output('match_2_text', 'children'),
    Output('match_3_text', 'children'),
    Output('match_4_text', 'children'),
    Output('match_5_text', 'children'),
    Input('slider_hue', 'value'),
    Input('slider_saturation', 'value'),
    Input('slider_value_brightness', 'value'))
def display_similar_HSV_option(H, S, V):
    # find matching color and output string for displaying user choice
    user_color = np.array([H, S, V])
    top_5_matches = shades.apply(lambda row : distance(row[["H", "S", "V"]], user_color), axis = 1).sort_values().index[:5]
    top_5_matches_colors = shades.iloc[top_5_matches.values, 2:6]
    most_similar_hex_colors = top_5_matches_colors["hex"].values.tolist()
    return most_similar_hex_colors

# callback for displaying most similar colors
@app.callback(
    Output('match_1', 'style'),
    Output('match_2', 'style'),
    Output('match_3', 'style'),
    Output('match_4', 'style'),
    Output('match_5', 'style'),
    Input('slider_hue', 'value'),
    Input('slider_saturation', 'value'),
    Input('slider_value_brightness', 'value'))
def display_similar_colors(H, S, V):
    # find matching color and output string for displaying user choice
    user_color = np.array([H, S, V])
    top_5_matches = shades.apply(lambda row : distance(row[["H", "S", "V"]], user_color), axis = 1).sort_values().index[:5]
    top_5_matches_colors = shades.iloc[top_5_matches.values, 2:6]
    most_similar_hex_colors = top_5_matches_colors["hex"].values.tolist()
    displayed_colors = []
    for similar_color in most_similar_hex_colors:
        displayed_colors.append({'backgroundColor': similar_color, 
                                 "height": "150px", 
                                 "width": "150px",
                                 "borderRadius": "15px"})
    return displayed_colors

if __name__ == '__main__':
    app.run_server(debug=True)