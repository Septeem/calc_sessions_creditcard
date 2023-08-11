import json
import pandas as pd
from datetime import datetime


def calculate_sessions(arrears: list, start_date: datetime, end_date: datetime):
    if not arrears:
        return 0
    if not arrears[0]:
        return 0

    df = pd.DataFrame(arrears)
    df = df.dropna()
    df = df.sort_values(by='calculationDate')
    df.set_index('calculationDate', inplace=True)
    df.index = pd.to_datetime(df.index)
    df = df[start_date: end_date]
    outstanding_list = df['outstanding'].values.tolist()

    num_sessions = 0

    for i in range(1, len(outstanding_list)):
        if outstanding_list[i] == 0:
            if outstanding_list[i] == outstanding_list[i - 1]:
                continue
            else:
                num_sessions = num_sessions + 1
    if outstanding_list[-1] != 0:
        num_sessions = num_sessions + 1

    return num_sessions