import pandas as pd

def add_rul(df):
    # RUL = Remaining Useful Life

    max_cycle = df.groupby("engine_id")["cycle"].max().reset_index()
    max_cycle.columns = ["engine_id", "max_cycle"]

    df = df.merge(max_cycle, on="engine_id")
    df["RUL"] = df["max_cycle"] - df["cycle"]

    # Binary classification (failure within 30 cycles)
    df["failure"] = df["RUL"].apply(lambda x: 1 if x <= 30 else 0)

    return df


def preprocess(df):
    df = df.copy()

    # Drop unnecessary columns
    df = df.drop(["engine_id", "max_cycle"], axis=1)

    X = df.drop(["RUL", "failure"], axis=1)
    y = df["failure"]

    return X, y