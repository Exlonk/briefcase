import pandas as pd
import numpy as np
import time
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import plotly.express as px
from sklearn import datasets
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import cross_val_predict
import pandas as pd
import numpy as np
from sklearn.model_selection import cross_val_score
import plotly.express as px
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.svm import LinearSVR
import math
from dash import dash_table,callback,Dash, html, dcc,  Input
from dash import Output, no_update, ctx
import plotly.express as px
import dash_bootstrap_components as dbc
from jupyter_dash import JupyterDash
import data_science as ds
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sklearn import preprocessing
from dash_bootstrap_templates import load_figure_template # para los fondos de  las imagenes
import os        
import random                                    
from dash import DiskcacheManager
import diskcache
import dash 


app = dash.Dash(__name__,external_stylesheets=[dbc.themes.GRID],title='Exlonk',
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, \
                             initial-scale=1.0'}],use_pages=True) # SOLAR, LUX

server = app.server

app.layout = dash.page_container

if __name__ == "__main__":
    app.run()
