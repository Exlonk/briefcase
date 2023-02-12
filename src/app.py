import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc
import dash 


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.GRID],title='Exlonk',
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, \
                             initial-scale=1.0'}],use_pages=True) # SOLAR, LUX

server = app.server

app.layout = dash.page_container

if __name__ == "__main__":
    app.run()
