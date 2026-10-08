def temporal_split(df, date_column, train_q=0.7, valid_q=0.85):
    train_cut = df[date_column].quantile(train_q)
    valid_cut = df[date_column].quantile(valid_q)

    train = df[df[date_column] <= train_cut]
    valid = df[(df[date_column] > train_cut) & (df[date_column] <= valid_cut)]
    test = df[df[date_column] > valid_cut]

    return train, valid, test