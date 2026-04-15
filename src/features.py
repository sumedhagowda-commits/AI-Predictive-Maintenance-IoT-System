def create_features(df):
    # Simple rolling features (important for IoT)

    df = df.copy()

    df["sensor_1_roll"] = df["sensor_1"].rolling(3).mean()
    df["sensor_2_roll"] = df["sensor_2"].rolling(3).mean()

    df = df.fillna(0)

    return df