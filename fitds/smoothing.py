def smooth(data, column, window_span=25):
    ma = data[column].rolling(window=window_span, min_periods=window_span).mean()[:window_span]
    rest = data[column][window_span:]
    smoothed_df = pd.concat([sma, rest]).ewm(span=window_span, adjust=False).mean()
    smoothed_df = smoothed_df.fillna(value=0.0)
    return smoothed_df.values