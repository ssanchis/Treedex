# =====================================
# Treedex Application (Modular Version)
# =====================================

import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px

# Importem les nostres funcions modulars
from components.plots import make_scatter_plot
from components.plots import make_scatter_combo
from callbacks import register_callbacks
# del treedex.components.plots import make_pie_plot   # si fas un mòdul també pel pie

# ============================
# Sample artificial data
# ============================

df_table = pd.DataFrame({
    "Species": ["Human", "Mouse", "Elephant", "Whale"],
    "Weight (kg)": [70, 0.03, 5000, 30000],
    "Life Expectancy (years)": [79, 2, 70, 90]
})

df_scatter = pd.DataFrame({
    "Species": ["Human", "Mouse", "Elephant", "Whale"],
    "X": [1, 2, 3, 4],
    "Y": [10, 15, 13, 17]
})

# ============================
# Initialize Dash app
# ============================

app = dash.Dash(__name__)

# ============================
# Layout
# ============================

app.layout = html.Div([

    # Left column: Tree + Table
    html.Div([
        html.H2("Tree", style={'textAlign': 'center', 'padding': '10px'}),

        html.Div("Aquí aniria l'arbre...",
                 style={
                     'textAlign': 'center',
                     'border': '1px solid #ccc',
                     'height': '200px',
                     'marginBottom': '20px'
                 }),

        dash_table.DataTable(
            id="species-table",
            columns=[{"name": col, "id": col} for col in df_table.columns],
            data=df_table.to_dict("records"),
            row_selectable="multi",
            style_cell={'textAlign': 'center'}
        )

    ], style={
        'width': '25%',
        'display': 'inline-block',
        'verticalAlign': 'top',
        'padding': '10px',
        'borderRight': '1px solid #ccc'
    }),

    # Right column: Scatter + Pie
    html.Div([

        # Scatter created with your custom plot function
        dcc.Graph(
            id='scatter-plot',
            figure=make_scatter_plot(
                dfr=df_scatter,
                x="X",
                y="Y",
                title="Demo Scatter Plot",
                selection=[]
            )
        ),

    ], style={
        'width': '70%',
        'display': 'inline-block',
        'padding': '10px',
        'verticalAlign': 'top'
    })

])

# Registrem els callbacks modularment
register_callbacks(app, df_table, df_scatter)

# ============================
# Run server
# ============================

if __name__ == '__main__':
    app.run(debug=True)

