import dash
import dash_core_components as dcc
import dash_html_components as html

# static data
county = ['Millard, Utah', 'Hudspeth, Texas', 'Miami-Dade, Florida', 'Albany, New York', 'King, Washington', 'San Francisco, California', 'Pitkin, Colorodo']
overall = [22.6, 21.2, 27.6, 27.8, 29.4, 31.9, 31.1]
# TODO: working on this file to add more codes...
married = [23.9, 23.1, 30, 30, 30.6, 32.8, 31.5]
college = [27.0, 26.5, 31.1, 30.5, 31.4, 33.4, 32.5]

# initialize Dash environment
app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Hello Dash for HCDE 411'),

    # a div to put a short description
    html.Div(children='''
        This is a simple Dash application for HCDE 411
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='example-graph',
        figure={
            # configure the data
            'data': [
                # set x to be weekday, and y to be the counts. We use bars to represent our data.
                {'x': county, 'y': overall, 'type': 'bar', 'name': 'Overall'},
                {'x': county, 'y': married, 'type': 'bar', 'name': 'Married'},
                {'x': county, 'y': college, 'type': 'bar', 'name': 'College'},


            ],
            # configure the layout of the visualization --
            # set the title to be "Usage of the BGT North of NE 70th per week day"
            'layout': {
                'title': 'Age that women first enter motherhood'
            }
        }
    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)
