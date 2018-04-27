import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
from plotly.tools import FigureFactory as FF
import cufflinks as cf

def simpleStockChart(df,stockSymbol,split_validation,split_test):
    
    fig = FF.create_candlestick(df.Open, df.High, df.Low, df.Close, dates=df.index)

    # Make increasing ohlc sticks and customize their color and name
    fig_increasing = FF.create_candlestick(df.Open, df.High, df.Low, df.Close, dates=df.index,
        direction='increasing', name=stockSymbol,
        marker=Marker(color='rgb(150, 200, 250)'),
        line=Line(color='rgb(150, 200, 250)'))

    # Make decreasing ohlc sticks and customize their color and name
    fig_decreasing = FF.create_candlestick(df.Open, df.High, df.Low, df.Close, dates=df.index,
        direction='decreasing',
        marker=Marker(color='rgb(128, 128, 128)'),
        line=Line(color='rgb(128, 128, 128)'))

    add_line = Scatter(
        x=df.index,
        y=df.Close,
        name= 'Close',
        line=Line(color='grey', width = 1)
        )

    # Initialize the figure
    fig = fig_increasing

    # Add decreasing data with .extend()
    fig['data'].extend(fig_decreasing['data'])
    fig['data'].extend([add_line])

    fig['layout'].update({
        'title': 'Stock Price Prediction',
        'yaxis': {'title': stockSymbol + ' Stock'},
        'shapes': [{
            'x0': split_validation, 'x1': split_validation,
            'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper',
            'line': {'color': 'rgb(30,30,30)', 'width': 1}
        },
        {
            'x0': split_test, 'x1': split_test,
            'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper',
            'line': {'color': 'rgb(30,30,30)', 'width': 1}
        }
        ],
        'annotations': [{
            'x': split_validation, 'y': 0.05, 'xref': 'x', 'yref': 'paper',
            'showarrow': False, 'xanchor': 'left',
            'text': 'Validation'
        },
        {
            'x': split_validation, 'y': 0.05, 'xref': 'x', 'yref': 'paper',
            'showarrow': False, 'xanchor': 'right',
            'text': 'Training Data'
        },
        {
            'x': split_test, 'y': 0.05, 'xref': 'x', 'yref': 'paper',
            'showarrow': False, 'xanchor': 'left',
            'text': 'Test'
        }      
        ]
    })
    return fig

def technicalAnalysisChart(df):
    INCREASING_COLOR = '#17BECF'
    DECREASING_COLOR = '#7F7F7F'
    data = [ dict(
    type = 'candlestick',
    open = df.Open,
    high = df.High,
    low = df.Low,
    close = df.Close,
    x = df.Date,
    yaxis = 'y2',
    name = 'GS',
    increasing = dict( line = dict( color = INCREASING_COLOR ) ),
    decreasing = dict( line = dict( color = DECREASING_COLOR ) ),
    ) ]

    layout=dict()

    fig = dict( data=data, layout=layout )
    #Layout    
    fig['layout'] = dict()
    fig['layout']['plot_bgcolor'] = 'rgb(250, 250, 250)'
    fig['layout']['xaxis'] = dict( rangeselector = dict( visible = True ) )
    fig['layout']['yaxis'] = dict( domain = [0, 0.2], showticklabels = False )
    fig['layout']['yaxis2'] = dict( domain = [0.2, 0.8] )
    fig['layout']['legend'] = dict( orientation = 'h', y=0.9, x=0.3, yanchor='bottom' )
    fig['layout']['margin'] = dict( t=40, b=40, r=40, l=40 )
    #Buttons
    rangeselector=dict(
    visibe = True,
    x = 0, y = 0.9,
    bgcolor = 'rgba(150, 200, 250, 0.4)',
    font = dict( size = 13 ),
    buttons=list([
        dict(count=1,
             label='reset',
             step='all'),
        dict(count=1,
             label='1yr',
             step='year',
             stepmode='backward'),
        dict(count=3,
            label='3 mo',
            step='month',
            stepmode='backward'),
        dict(count=1,
            label='1 mo',
            step='month',
            stepmode='backward'),
        dict(step='all')
    ]))
    fig['layout']['xaxis']['rangeselector'] = rangeselector
    
    mv_y = df.ema12
    mv_x = list(df.Date)

    # Clip the ends
    mv_x = mv_x[5:-5]
    mv_y = mv_y[5:-5]

    fig['data'].append( dict( x=mv_x, y=mv_y, type='scatter', mode='lines', 
                             line = dict( width = 1 ),
                             marker = dict( color = '#E377C2' ),
                             yaxis = 'y2', name='Moving Average' ) )
    
    colors = []

    for i in range(len(df.Close)):
        if i != 0:
            if df.Close[i] > df.Close[i-1]:
                colors.append(INCREASING_COLOR)
            else:
                colors.append(DECREASING_COLOR)
        else:
            colors.append(DECREASING_COLOR)
            
            
    fig['data'].append( dict( x=df.Date, y=df.Volume,                         
                         marker=dict( color=colors ),
                         type='bar', yaxis='y', name='Volume' ) )
    
    

    fig['data'].append( dict( x=df.Date, y=df.bol_bands_upper, type='scatter', yaxis='y2', 
                             line = dict( width = 1 ),
                             marker=dict(color='#ccc'), hoverinfo='none', 
                             legendgroup='Bollinger Bands', name='Bollinger Bands') )

    fig['data'].append( dict( x=df.Date, y=df.bol_bands_lower, type='scatter', yaxis='y2',
                             line = dict( width = 1 ),
                             marker=dict(color='#ccc'), hoverinfo='none',
                             legendgroup='Bollinger Bands', showlegend=False ) )
    
    return fig