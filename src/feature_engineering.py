def create_features(df):
    # Ticket length
    df['ticket_length'] = df['Last_Support_Ticket'].apply(lambda x: len(str(x)))

    # Engagement score
    df['engagement_score'] = df['Daily_Usage_Mins'] * df['Login_Frequency']

    # Complaint detection
    df['has_complaint'] = df['Last_Support_Ticket'].str.contains(
        'issue|error|problem|not working', case=False, na=False
    ).astype(int)

    # Drop text column
    df = df.drop(['Last_Support_Ticket'], axis=1)

    return df