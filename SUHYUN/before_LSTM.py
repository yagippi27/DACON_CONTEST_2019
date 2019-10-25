#!/usr/bin/env python
# coding: utf-8

# In[2]:


def before_LSTM(Series_data):
    """
    :usage1: Use this with like 'dataframe_name.iloc[:, col_number]' ex) train.iloc[:, 0]
    :usage2: You can get X_dataset_t, and y_dataset from this for LSTM. Also those are global variable.
    :caution: ONLY use SERIES type with ONE COLUMN!!!
    :who made this: SUHYUN AN ^^
    """
    
    import pandas as pd
    import numpy as np
    
    global X_dataset_t
    global y_dataset
    making_shift_count = 25

    dataset = Series_data.to_frame()

    from sklearn.preprocessing import MinMaxScaler
    dataset_sc=MinMaxScaler().fit_transform(dataset)
    dataset_sc_df = pd.DataFrame(dataset_sc, columns=dataset.columns, index = dataset.index)

    for s in range(1, making_shift_count):
        dataset_sc_df['shift_{}'.format(s)] = dataset_sc_df[dataset.columns].shift(s)

    X_dataset = dataset_sc_df.dropna().drop(dataset.columns, axis=1)
    y_dataset = dataset_sc_df.dropna()[dataset.columns]

    X_dataset = X_dataset.values
    y_dataset = y_dataset.values

    X_dataset_t = X_dataset.reshape(X_dataset.shape[0], making_shift_count-1, 1)

    return X_dataset_t.shape, X_dataset_t, y_dataset.shape, y_dataset


# In[ ]:




