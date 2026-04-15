import pandas as pd

def load_data(path):
    # NASA dataset has no headers
    df = pd.read_csv(path, sep=" ", header=None)

    # Remove empty columns
    df = df.dropna(axis=1)

    # Assign column names (CMAPSS format)
    columns = ["engine_id", "cycle"]

    # 3 operational settings
    for i in range(1, 4):
        columns.append(f"setting_{i}")

    # 21 sensor readings
    for i in range(1, 22):
        columns.append(f"sensor_{i}")

    df.columns = columns

    print("Dataset Loaded:", df.shape)
    return df