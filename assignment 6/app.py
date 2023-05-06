import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import Flask

server = Flask(__name__)

app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    dcc.Graph(id='example-graph', figure={
        'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'}],
        'layout': {'title': 'Dash Data Visualization'}
    })
])

@server.route("/")
def index():
    return '''
        <html>
            <head>
                <title>Dash App</title>
            </head>
            <body>
                <h1>Dash App</h1>
                <div>{}</div>
            </body>
        </html>
    '''.format(dcc.Location(id='url', refresh=False))

if __name__ == '__main__':
    app.run_server(debug=True)