# Treedex Base Layout Example
import dash
from dash import dcc, html, dash_table
import plotly.express as px
import pandas as pd

# Sample artificial data
df_table = pd.DataFrame({
    "Species": ["Human", "Mouse", "Elephant", "Whale"],
    "Weight (kg)": [70, 0.03, 5000, 30000],
    "Life Expectancy (years)": [79, 2, 70, 90]
})

df_scatter = pd.DataFrame({
    "X": [1, 2, 3, 4],
    "Y": [10, 15, 13, 17],
    "Label": ["A", "B", "C", "D"]
})

df_pie = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Value": [30, 45, 25]
})

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.Div([
        html.H2("Tree", style={'textAlign': 'center', 'padding': '10px'}),
        html.Div("Aquí aniria l'arbre...", style={'textAlign': 'center', 'border': '1px solid #ccc', 
                                                  'height': '200px', 'marginBottom': '20px'}),
        dash_table.DataTable(
            columns=[{"name": i, "id": i} for i in df_table.columns],
            data=df_table.to_dict('records'),
            style_table={'overflowX': 'auto'},
            style_cell={'textAlign': 'center'}
        )
    ], style={'width': '25%', 'display': 'inline-block', 'verticalAlign': 'top', 'padding': '10px', 
              'borderRight': '1px solid #ccc'}),

    html.Div([
        dcc.Graph(
            id='scatter-plot',
            figure=px.scatter(df_scatter, x='X', y='Y', text='Label', title='Scatter Plot')
        ),
        dcc.Graph(
            id='pie-chart',
            figure=px.pie(df_pie, names='Category', values='Value', title='Pie Chart')
        )
    ], style={'width': '70%', 'display': 'inline-block', 'padding': '10px', 'verticalAlign': 'top'})
])

# Run server
if __name__ == '__main__':
    app.run(debug=True)
