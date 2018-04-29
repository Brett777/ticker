import numpy as np
import pandas as pd

def windowTransform(df):
    #Tomorrow's Close. This is the target column    
    df['Close Tomorrow'] = df['Close'].shift(-1)
    df['Close Tomorrow Change'] = df['Close Tomorrow'] - df['Close']
    df['Close Tomorrow Tren'] = df['Close Tomorrow Change'].apply(np.sign)
    
    #Open window
    df['Open-0'] = df.Open
    for i in range(1,window):
        df['Open-'+str(i)] = df.Close.shift(i)
        df['Open Change-'+str(i-1)] = df['Open-'+str(i-1)] - df['Open-'+str(i)] 
        df['Open-'+str(i)+' Trend'] = df['Open Change-'+str(i-1)].apply(np.sign)
    df.drop('Open-0',axis=1, inplace=True)
    
    #High window
    df['High-0'] = df.High
    for i in range(1,window):
        df['High-'+str(i)] = df.Close.shift(i)
        df['High Change-'+str(i-1)] = df['High-'+str(i-1)] - df['High-'+str(i)] 
        df['High-'+str(i)+' Trend'] = df['High Change-'+str(i-1)].apply(np.sign)
    df.drop('High-0',axis=1, inplace=True)                                                                        
                                                                        
    #Low window
    df['Low-0'] = df.Low
    for i in range(1,window):
        df['Low-'+str(i)] = df.Close.shift(i)
        df['Low Change-'+str(i-1)] = df['Low-'+str(i-1)] - df['Low-'+str(i)] 
        df['Low-'+str(i)+' Trend'] = df['Low Change-'+str(i-1)].apply(np.sign)
    df.drop('Low-0',axis=1,  inplace=True)
                   
    #Close window
    df['Close-0'] = df.Close
    for i in range(1,window):
        df['Close-'+str(i)] = df.Close.shift(i)
        df['Close Change-'+str(i-1)] = df['Close-'+str(i-1)] - df['Close-'+str(i)] 
        df['Close-'+str(i)+' Trend'] = df['Close Change-'+str(i-1)].apply(np.sign)
    df.drop('Close-0',axis=1, inplace=True)                                                                     

    #BBand window
    df['BBand-Upper-0'] = df['Real Upper Band']
    df['BBand-Lower-0'] = df['Real Lower Band']
    df['BBand-Middle-0'] = df['Real Middle Band']

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

    #Macd window
    df['MACD_Hist-0'] = df['MACD_Hist']
    df['MACD-0'] = df['MACD']
    df['MACD_Signal-0'] = df['MACD_Signal']
    for i in range(1,window):
        df['MACD_Hist-'+str(i)] = df.Close.shift(i)
        df['MACD_Hist Change-'+str(i-1)] = df['MACD_Hist-'+str(i-1)] - df['MACD_Hist-'+str(i)] 
        df['MACD_Hist-'+str(i)+' Trend'] = df['MACD_Hist Change-'+str(i-1)].apply(np.sign)

        df['MACD-'+str(i)] = df.Close.shift(i)
        df['MACD Change-'+str(i-1)] = df['MACD-'+str(i-1)] - df['MACD-'+str(i)] 
        df['MACD-'+str(i)+' Trend'] = df['MACD Change-'+str(i-1)].apply(np.sign)

        df['MACD_Signal-'+str(i)] = df.Close.shift(i)
        df['MACD_Signal Change-'+str(i-1)] = df['MACD_Signal-'+str(i-1)] - df['MACD_Signal-'+str(i)] 
        df['MACD_Signal-'+str(i)+' Trend'] = df['MACD_Signal Change-'+str(i-1)].apply(np.sign)

    df.drop('MACD_Hist-0',axis=1, inplace=True)
    df.drop('MACD-0',axis=1, inplace=True)
    df.drop('MACD_Signal-0',axis=1, inplace=True)
                                                                        
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['DayOfYear'] = df['Date'].dt.dayofyear
    df['WeekOfYear'] = df['Date'].dt.weekofyear
                                                                        
    df.replace(0,-1,inplace=True)                                                                        
    return df