import pandas as pd


def simple_moving_average(close: pd.Series, window: int, fillna: bool = False):
    min_periods = 0 if fillna else window
    return close.rolling(window=window, min_periods=min_periods).mean()
