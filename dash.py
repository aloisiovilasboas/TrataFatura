import dash
import pandas as pd

from lxml import etree 

""" with open('templatefile.xml', 'r') as f:
    data = f.read()

print(data) """

df = pd.read_xml('templatefile.xml')

with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(df)

# Create a Dash app
""" app = dash.Dash()

# Create a DataTable component
datatable = dash.DataTable(
    data=df.to_dict('records'),
    columns=[{'name': i, 'id': i} for i in df.columns]
)

# Add the DataTable component to the app layout
app.layout = dash.Div(
    [
        datatable,
    ]
)

# Run the Dash app
app.run_server(debug=True) """