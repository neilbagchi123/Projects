import dash.dependencies
from dash import Dash, dash_table, dcc, html, Input, Output, callback, State
import pandas as pd

app = Dash(__name__)

df = pd.read_excel('doctor schedule-southwest.xlsx')
df = df[0:5] # just work with first 5 rows

app.layout = html.Div([
    dash_table.DataTable(
        id='Table-1',
        data=df.to_dict(orient='records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        editable=True
    ),
    html.Br(),
    html.Button('Submit', id='Submit-btn', n_clicks=0),
    html.Br(),
    html.P(id='Text-1')
])

@dash.callback(
    Output('Text-1', 'children'),
    Input('Submit-btn', 'n_clicks'),
    State('Table-1', 'data'),
    prevent_initial_call=True
)
def handle_button(n_clicks,data):
    df = pd.DataFrame(data)
    # when this callback is triggered, the user has pressed the button
    # at this point, the dataframe "df" has the *current* updated contents that the user edited

    # so we can give it a new name and save it here
    df.to_excel("updated_doctor schedule-southwest.xlsx")

    # this is just to test the program, remove later
    s = df.to_string(header=False)

    return s

if __name__ == '__main__':
   app.run_server()
