import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import random


#### Define Variables ####

myheading = "Random Statistics by City"
githublink = 'https://github.com/ktemsupa/midcourse-project'

def get_random_data(num:int = 10) -> list:
    try:
        assert type(num) == int
    except AssertionError:
        print('Error Message: Please Use Integers')
        return []
    
#Builds a list of random integers. 
    random_data = []
    for i in range(num):
        random_data.append(random.randint(0,100))
    return random_data


#### Initiate the App ####

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


#### Set Up The Layout ####
app.layout = html.Div(
    children=[
        html.H2(children=myheading, style={"textAlign": "center"}),
        dcc.Dropdown(
            id="my-dropdown",
            options=[
                {"label": "New York City", "value": "NYC"},
                {"label": "Paris", "value": "PRS"},
                {"label": "Sydney", "value": "SYD"},
            ],
            value="NYC",
        ),
        dcc.Graph(
            id="graph",
            config={
                "showSendToCloud": True,
                "plotlyServerURL": "https://plot.ly",
            },
        ),
        
        
        html.A('Code on Github', href=githublink),
        html.Br(),
        
    ]
)

#### Define Callback ####
@app.callback(
    dash.dependencies.Output("graph", "figure"),
    [dash.dependencies.Input("my-dropdown", "value")],
)
def update_output(value:str) -> dict:
    y_axis_dict = {
        "NYC": get_random_data(num=25),
        "PRS": get_random_data(),
        "SYD": get_random_data(num=100),
    }
    return {
        "data": [{"type": "scatter", "y": y_axis_dict[value]}],
        "layout": {"title": value},
    }


#### Deploy ####

app.run_server(port=8051)
