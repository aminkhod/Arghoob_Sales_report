
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output



app = dash.Dash()
df = pd.DataFrame({'message': ['Hi', 'Bye', 'GN', 'Hi', 'Bye', 'GN'],
                   'Date': ['01/08/19', '01/08/19', '01/08/19', '02/08/19', '02/08/19', '02/08/19'],
                   'Count': [10, 20, 30, 15, 25, 35]})
app.layout = html.Div([

    dcc.Dropdown(
        id = 'first_dropdown',
        options = df.Date,
        placeholder='Select a Date'
    ),
    html.Div(id='output-graph')

    ])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='first_dropdown', component_property='options')]
    )

def update_output_div(input_value):
    return dcc.Graph(id = 'Bar_Plor',
                  figure = {
                      'data' : [
                          {'x':df.message, 'y':df.Count, 'type':'bar', 'name':'First Chart'}
                          ]
                      })


if __name__ == '__main__':
    app.run_server(port=4050, debug=True)
