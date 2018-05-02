import numpy as np
import pandas as pd

def windowTransform(df, window):
    #Tomorrow's Close. This is the target column    
    df['Close Tomorrow'] = df['Close'].shift(-1)
    df['Close Tomorrow Change'] = df['Close Tomorrow'] - df['Close']
    df['Close Tomorrow Trend'] = df['Close Tomorrow Change'].apply(np.sign)
    
    #Open window
    df['Open-0'] = df.Open
    for i in range(1,window):
        df['Open-'+str(i)] = df.Close.shift(i)
        df['Open Change-'+str(i-1)] = df['Open-'+str(i-1)] - df['Open-'+str(i)] 
        df['Open-'+str(i)+' Trend'] = df['Open Change-'+str(i-1)].apply(np.sign)
    df.drop('Open-0',axis=1, inplace=True)
    df.rename(columns={'Open Change-0':'Open Change'}, inplace=True)
    
    #High window
    df['High-0'] = df.High
    for i in range(1,window):
        df['High-'+str(i)] = df.Close.shift(i)
        df['High Change-'+str(i-1)] = df['High-'+str(i-1)] - df['High-'+str(i)] 
        df['High-'+str(i)+' Trend'] = df['High Change-'+str(i-1)].apply(np.sign)
    df.drop('High-0',axis=1, inplace=True)                                                                        
    df.rename(columns={'High Change-0':'High Change'}, inplace=True)
    
    #Low window
    df['Low-0'] = df.Low
    for i in range(1,window):
        df['Low-'+str(i)] = df.Close.shift(i)
        df['Low Change-'+str(i-1)] = df['Low-'+str(i-1)] - df['Low-'+str(i)] 
        df['Low-'+str(i)+' Trend'] = df['Low Change-'+str(i-1)].apply(np.sign)
    df.drop('Low-0',axis=1,  inplace=True)
    df.rename(columns={'Low Change-0':'Low Change'}, inplace=True)
    
    #Close window
    df['Close-0'] = df.Close
    for i in range(1,window):
        df['Close-'+str(i)] = df.Close.shift(i)
        df['Close Change-'+str(i-1)] = df['Close-'+str(i-1)] - df['Close-'+str(i)] 
        df['Close-'+str(i)+' Trend'] = df['Close Change-'+str(i-1)].apply(np.sign)
    df.drop('Close-0',axis=1, inplace=True)                                                                     
    df.rename(columns={'Close Change-0':'Close Change'}, inplace=True)
    
    #BBand window
    df['BBand-Upper-0'] = df['bol_bands_upper']
    df['BBand-Lower-0'] = df['bol_bands_lower']
    df['BBand-Middle-0'] = df['bol_bands_middle']

    for i in range(1,window):
        df['BBand-Upper-'+str(i)] = df.Close.shift(i)
        df['BBand-Upper Change-'+str(i-1)] = df['BBand-Upper-'+str(i-1)] - df['BBand-Upper-'+str(i)] 
        df['BBand-Upper-'+str(i)+' Trend'] = df['BBand-Upper Change-'+str(i-1)].apply(np.sign)

        df['BBand-Lower-'+str(i)] = df.Close.shift(i)
        df['BBand-Lower Change-'+str(i-1)] = df['BBand-Lower-'+str(i-1)] - df['BBand-Lower-'+str(i)] 
        df['BBand-Lower-'+str(i)+' Trend'] = df['BBand-Lower Change-'+str(i-1)].apply(np.sign)

        df['BBand-Middle-'+str(i)] = df.Close.shift(i)
        df['BBand-Middle Change-'+str(i-1)] = df['BBand-Middle-'+str(i-1)] - df['BBand-Middle-'+str(i)] 
        df['BBand-Middle-'+str(i)+' Trend'] = df['BBand-Middle Change-'+str(i-1)].apply(np.sign)

    df.drop('BBand-Upper-0',axis=1, inplace=True)
    df.drop('BBand-Lower-0',axis=1, inplace=True)
    df.drop('BBand-Middle-0',axis=1, inplace=True)
    df.rename(columns={'BBand-Upper Change-0':'BBand-Upper Change',
                       'BBand-Lower Change-0':'BBand-Lower Change',
                       'BBand-Middle Change-0':'BBand-Middle Change'}, inplace=True)

    #Macd window
    df['MACD-0'] = df['macd_val']
    df['MACD_Signal-0'] = df['macd_signal_line']
    for i in range(1,window):
        df['MACD-'+str(i)] = df.Close.shift(i)
        df['MACD Change-'+str(i-1)] = df['MACD-'+str(i-1)] - df['MACD-'+str(i)] 
        df['MACD-'+str(i)+' Trend'] = df['MACD Change-'+str(i-1)].apply(np.sign)

        df['MACD_Signal-'+str(i)] = df.Close.shift(i)
        df['MACD_Signal Change-'+str(i-1)] = df['MACD_Signal-'+str(i-1)] - df['MACD_Signal-'+str(i)] 
        df['MACD_Signal-'+str(i)+' Trend'] = df['MACD_Signal Change-'+str(i-1)].apply(np.sign)

    df.drop('MACD-0',axis=1, inplace=True)
    df.drop('MACD_Signal-0',axis=1, inplace=True)
    df.rename(columns={'MACD Change-0':'MACD Change',
                       'MACD_Signal Change-0':'MACD_Signal Change'}, inplace=True)
                                                                        
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['DayOfYear'] = df['Date'].dt.dayofyear
    df['WeekOfYear'] = df['Date'].dt.weekofyear
  
    #RSI window
    df['rsi-0'] = df.rsi
    for i in range(1,window):
        df['rsi-'+str(i)] = df.Close.shift(i)
        df['rsi Change-'+str(i-1)] = df['rsi-'+str(i-1)] - df['rsi-'+str(i)] 
        df['rsi-'+str(i)+' Trend'] = df['rsi Change-'+str(i-1)].apply(np.sign)
  
    df.drop(['rsi-0','rsi_u','rsi_d'], axis=1, inplace=True)
    df.rename(columns={'rsi Change-0':'rsi Change'}, inplace=True)
    
    #Williams %R
    df['williams_r-0'] = df.williams_r
    for i in range(1,window):
        df['williams_r-'+str(i)] = df.Close.shift(i)
        df['williams_r Change-'+str(i-1)] = df['williams_r-'+str(i-1)] - df['williams_r-'+str(i)] 
        df['williams_r-'+str(i)+' Trend'] = df['williams_r Change-'+str(i-1)].apply(np.sign)
  
    df.drop(['williams_r-0'], axis=1, inplace=True)
    df.rename(columns={'williams_r Change-0':'williams_r Change'}, inplace=True)
    
    #ultimate_oscillator
    df['ultimate_oscillator-0'] = df.ultimate_oscillator
    for i in range(1,window):
        df['ultimate_oscillator-'+str(i)] = df.Close.shift(i)
        df['ultimate_oscillator Change-'+str(i-1)] = df['ultimate_oscillator-'+str(i-1)] - df['ultimate_oscillator-'+str(i)] 
        df['ultimate_oscillator-'+str(i)+' Trend'] = df['ultimate_oscillator Change-'+str(i-1)].apply(np.sign)
  
    df.drop(['ultimate_oscillator-0'], axis=1, inplace=True) 
    df.rename(columns={'ultimate_oscillator Change-0':'ultimate_oscillator Change'}, inplace=True)

    df.dropna(axis=0, how='any', inplace=True)
    return df