import numpy as np
import pandas as pd

def windowTransform(df):
    df['Close Tomorrow'] = df['Close'].shift(-1)
    df['Close Tomorrow Change'] = df['Close Tomorrow'] - df['Close']
    df['Close Tomorrow s'] = df['Close Tomorrow Change'].apply(np.sign)

    df['Close-1'] = df['Close'].shift(1)
    df['Close Change'] = df['Close'] - df['Close-1'] 
    df['Close Change s'] = df['Close Change'].apply(np.sign)

    df['Close-2'] = df['Close'].shift(2)
    df['Close-1 Change'] = df['Close-1'] - df['Close-2'] 
    df['Close-1 s'] = df['Close-1 Change'].apply(np.sign)

    df['Close-3'] = df['Close'].shift(3)
    df['Close-2 Change'] = df['Close-2'] - df['Close-3'] 
    df['Close-2 s'] = df['Close-2 Change'].apply(np.sign)

    df['Close-4'] = df['Close'].shift(4)
    df['Close-3 Change'] = df['Close-3'] - df['Close-4'] 
    df['Close-3 s'] = df['Close-3 Change'].apply(np.sign)

    df['Close-5'] = df['Close'].shift(5)
    df['Close-4 Change'] = df['Close-4'] - df['Close-5'] 
    df['Close-4 s'] = df['Close-4 Change'].apply(np.sign)

    df['Close-6'] = df['Close'].shift(6)
    df['Close-5 Change'] = df['Close-5'] - df['Close-6'] 
    df['Close-5 s'] = df['Close-5 Change'].apply(np.sign)

    df['Close-7'] = df['Close'].shift(7)
    df['Close-6 Change'] = df['Close-6'] - df['Close-7'] 
    df['Close-6 s'] = df['Close-6 Change'].apply(np.sign)

    df['Close-8'] = df['Close'].shift(8)
    df['Close-7 Change'] = df['Close-7'] - df['Close-8'] 
    df['Close-7 s'] = df['Close-7 Change'].apply(np.sign)

    df['Close-9'] = df['Close'].shift(9)
    df['Close-8 Change'] = df['Close-8'] - df['Close-9'] 
    df['Close-8 s'] = df['Close-8 Change'].apply(np.sign)

    df['Close-10'] = df['Close'].shift(10)
    df['Close-9 Change'] = df['Close-9'] - df['Close-10'] 
    df['Close-9 s'] = df['Close-9 Change'].apply(np.sign)

    df['Close-11'] = df['Close'].shift(11)
    df['Close-10 Change'] = df['Close-10'] - df['Close-11'] 
    df['Close-10 s'] = df['Close-10 Change'].apply(np.sign)

    df['Close-12'] = df['Close'].shift(12)
    df['Close-11 Change'] = df['Close-11'] - df['Close-12'] 
    df['Close-11 s'] = df['Close-11 Change'].apply(np.sign)

    df['Close-13'] = df['Close'].shift(13)
    df['Close-12 Change'] = df['Close-12'] - df['Close-13'] 
    df['Close-12 s'] = df['Close-12 Change'].apply(np.sign)

    df['Close-14'] = df['Close'].shift(14)
    df['Close-13 Change'] = df['Close-13'] - df['Close-14'] 
    df['Close-13 s'] = df['Close-13 Change'].apply(np.sign)

    df['Close-15'] = df['Close'].shift(15)
    df['Close-14 Change'] = df['Close-14'] - df['Close-15'] 
    df['Close-14 s'] = df['Close-14 Change'].apply(np.sign)

    df['Close-16'] = df['Close'].shift(16)
    df['Close-15 Change'] = df['Close-15'] - df['Close-16'] 
    df['Close-15 s'] = df['Close-15 Change'].apply(np.sign)

    df['Close-17'] = df['Close'].shift(17)
    df['Close-16 Change'] = df['Close-16'] - df['Close-17'] 
    df['Close-16 s'] = df['Close-16 Change'].apply(np.sign)

    df['Close-18'] = df['Close'].shift(18)
    df['Close-17 Change'] = df['Close-17'] - df['Close-18'] 
    df['Close-17 s'] = df['Close-17 Change'].apply(np.sign)

    df['Close-19'] = df['Close'].shift(19)
    df['Close-18 Change'] = df['Close-18'] - df['Close-19'] 
    df['Close-18 s'] = df['Close-18 Change'].apply(np.sign)

    df['Close-20'] = df['Close'].shift(20)
    df['Close-19 Change'] = df['Close-19'] - df['Close-20'] 
    df['Close-19 s'] = df['Close-19 Change'].apply(np.sign)

    df['Close-21'] = df['Close'].shift(21)
    df['Close-20 Change'] = df['Close-20'] - df['Close-21'] 
    df['Close-20 s'] = df['Close-20 Change'].apply(np.sign)

    df['Close-22'] = df['Close'].shift(22)
    df['Close-21 Change'] = df['Close-21'] - df['Close-22'] 
    df['Close-21 s'] = df['Close-21 Change'].apply(np.sign)

    df['Close-23'] = df['Close'].shift(23)
    df['Close-22 Change'] = df['Close-22'] - df['Close-23'] 
    df['Close-22 s'] = df['Close-22 Change'].apply(np.sign)

    df['rsi-1'] = df['rsi'].shift(1)
    df['rsi Change'] = df['rsi'] - df['rsi-1'] 

    df['money_flow_index-1'] = df['money_flow_index'].shift(1)
    df['money_flow_index Change'] = df['money_flow_index'] - df['money_flow_index-1'] 

    df['macd_val-1'] = df['macd_val'].shift(1)
    df['macd_val-2'] = df['macd_val'].shift(2)
    df['macd_val-3'] = df['macd_val'].shift(3)
    df['macd_val-4'] = df['macd_val'].shift(4)
    df['macd_val-5'] = df['macd_val'].shift(5)
    df['macd_val-6'] = df['macd_val'].shift(6)
    df['macd_val-7'] = df['macd_val'].shift(7)

    df['macd_signal_line-1'] = df['macd_signal_line'].shift(1)
    df['macd_signal_line-2'] = df['macd_signal_line'].shift(2)
    df['macd_signal_line-3'] = df['macd_signal_line'].shift(3)
    df['macd_signal_line-4'] = df['macd_signal_line'].shift(4)
    df['macd_signal_line-5'] = df['macd_signal_line'].shift(5)
    df['macd_signal_line-6'] = df['macd_signal_line'].shift(6)
    df['macd_signal_line-7'] = df['macd_signal_line'].shift(7)

    df['High-1'] = df['High'].shift(1)
    df['Low-1'] = df['Low'].shift(1)
    df['Open-1'] = df['Open'].shift(1)
    df['Volume-1'] = df['Volume'].shift(1)
    df['Change-1'] = df['Close']-df['Close-1']
    df['Change-2'] = df['Close-1']-df['Close-2']
    df['Change-3'] = df['Close-2']-df['Close-3']
    #df['Change'] = df['Close Tomorrow'] - df['Close'] # Be sure to ignore this column in training
    #df['Change Direction'] = df['Change'].apply(np.sign)      # If regressing tomorrow's close, ignore
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['DayOfYear'] = df['Date'].dt.dayofyear
    df['WeekOfYear'] = df['Date'].dt.weekofyear
    return df