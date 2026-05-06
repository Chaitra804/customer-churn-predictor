def preprocess(df):
    # Drop unnecessary columns
    df = df.drop(['Customer_ID', 'Name', 'Email'], axis=1)

    # Map login frequency
    mapping = {'Daily': 3, 'Weekly': 2, 'Monthly': 1}
    df['Login_Frequency'] = df['Login_Frequency'].map(mapping)

    # Handle missing
    df = df.fillna(0)

    return df