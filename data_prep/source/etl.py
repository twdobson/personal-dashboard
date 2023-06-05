import pandas as pd

df = pd.read_excel('data_prep/data/stats_sa/electricity_production/Excel table from 2000.xlsx')

 
PD_MAX_ROWS = 500
PD_MAX_COLUMNS = 5100
PD_CONSOLE_WIDTH = 2000
PD_MAX_COLWIDTH = 1000

pd.options.display.max_rows = PD_MAX_ROWS
pd.options.display.max_columns = PD_MAX_COLUMNS
pd.options.display.width = PD_CONSOLE_WIDTH
pd.options.display.max_colwidth = PD_MAX_COLWIDTH

df.head()

df.columns

df_columns = df.columns

index_columns = df.columns[df.columns.str.contains('H')]
month_columns = df.columns[df.columns.str.contains('MO')]

df_melted = df.melt(
    id_vars=index_columns,
    value_vars=month_columns,
    value_name='index_value',
    var_name='month_id_original'
)


df_melted.head()

df_melted['month_id'] = pd.to_datetime(
    df_melted['month_id_original'].str.slice(4,8) + df_melted['month_id_original'].str.slice(2,4) + '01',
)

for col in index_columns:
    print(f"{col}: {','.join(df_melted[col].drop_duplicates().astype(str).tolist())}")

df_melted[['H04', 'H05']].drop_duplicates()
    

import plotly.express as px

import plotly.graph_objects as go
import urllib, json

url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
response = urllib.request.urlopen(url)
data = json.loads(response.read())

# override gray link colors with 'source' colors
opacity = 0.4
# change 'magenta' to its 'rgba' value to add opacity
data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
                                    for src in data['data'][0]['link']['source']]

fig = go.Figure(data=[go.Sankey(
    valueformat = ".0f",
    valuesuffix = "TWh",
    # Define nodes
    node = dict(
      pad = 15,
      thickness = 15,
      line = dict(color = "black", width = 0.5),
      label =  data['data'][0]['node']['label'],
      color =  data['data'][0]['node']['color']
    ),
    # Add links
    link = dict(
      source =  data['data'][0]['link']['source'],
      target =  data['data'][0]['link']['target'],
      value =  data['data'][0]['link']['value'],
      label =  data['data'][0]['link']['label'],
      color =  data['data'][0]['link']['color']
))])

fig.update_layout(title_text="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
                  font_size=10)
fig.show()




# --------------------------------------------------

from highcharts import Highmap, Highcharts

# Create the main map
chart = Highmap()
chart.set_options('chart', {
    'map': 'custom/world',
    'drilldown': {
        'activeDataLabelStyle': {
            'color': '#FFFFFF',
            'cursor': 'pointer',
            'fontWeight': 'bold',
            'textDecoration': 'underline'
        },
        'drillUpButton': {
            'relativeTo': 'spacingBox',
            'position': {
                'x': 0,
                'y': 60
            }
        }
    }
})

# Add the drilldown series
series_data = [
    {
        'name': 'Asia',
        'id': 'asia',
        'data': [
            ['in', 100],
            ['jp', 200],
            ['cn', 300]
        ]
    },
    {
        'name': 'Europe',
        'id': 'europe',
        'data': [
            ['de', 400],
            ['fr', 500],
            ['uk', 600]
        ]
    }
]

chart.add_drilldown_series(series_data)

# Configure drilldown data
drilldown_data = {
    'asia': {
        'name': 'Asia',
        'data': [
            ['in-ka', 50],
            ['in-mh', 70],
            ['jp-tk', 80],
            ['jp-ty', 120],
            ['cn-sh', 180],
            ['cn-bj', 120]
        ]
    },
    'europe': {
        'name': 'Europe',
        'data': [
            ['de-be', 80],
            ['de-by', 100],
            ['fr-idf', 110],
            ['fr-vd', 150],
            ['uk-en', 160],
            ['uk-sc', 190]
        ]
    }
}

chart.add_drilldown_data(drilldown_data)

# Set the chart title and subtitle
chart.set_title('Drilldown Map')
chart.set_subtitle('Click a region to view details')

# Set the tooltip and color axis
chart.set_options('tooltip', {'enabled': True})
chart.set_options('colorAxis', {'min': 0, 'max': 600})

# Render the chart
chart.htmlcontent