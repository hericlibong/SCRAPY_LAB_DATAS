import dash, dash_table
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import numpy as np

#from scrapy.fifalive.livefifaranking.livefifarankcrawl import databis

File = '/Users/mac/my_workshops/scrapy/fifalive/livefifaranking/livefifaranking/spiders/databis.csv'

data = pd.read_csv(File)
data = data.loc[~(data['country'].isna())]
data['rank'] = pd.to_numeric(data['rank'], downcast='integer', errors='coerce')
data['former rank'] = pd.to_numeric(data['former rank'], downcast='integer', errors='coerce')
data = data[['rank'] + ['country'] + ['moving', 'actual points', 'moving points', 'former points', 'former rank']]
data = data.fillna('0')
data = data.sort_values(by=['rank'], ascending=[True])


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])

app.layout = html.Div([
    html.Div([
        html.H4('Instant Fifa  Ranking', style={'margin-bottom': '0px', 'color': 'white'}),
        html.Hr(),
    
    dash_table.DataTable(
        data=data.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in data.columns],
        page_size=70,
        style_table={'height': '300px', 'overflowY': 'auto', 'Width':'50%'}, 
        fixed_rows={'headers': True},
        style_cell={'textAlign': 'left', 'padding': '5px'},
        style_as_list_view=True,
        style_header={
        'backgroundColor': 'grey',
        'fontWeight': 'bold'},
        style_data={
        'backgroundColor': 'rgb(50, 50, 50)',
        'color': 'white'},
#style_table={'minWidth': '100%'}

)], className = 'one-half columns')
    ],id = 'header', className= 'row flex-display', style={'margin-bottom': '25px'})
            
      






if __name__ == '__main__':
    app.run_server(debug=True)





