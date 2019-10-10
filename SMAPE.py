#!/usr/bin/env python
# coding: utf-8

# In[2]:


def smape_fast(df_y_true, df_y_pred):
    """
    @jit
    using SMAPE(Symmetric mean absolute percentage error)
    :setting:install 'numba' in anaconda
    :df_y_true: Real DateFrame
    :df_y_pred: DataFrame you made    
    """
    from numba import jit
    import math
    out = 0
    y_true = df_y_true.drop(df_y_true.columns[0], axis=1).values.reshape(-1)
    y_pred = df_y_pred.drop(df_y_pred.columns[0], axis=1).values.reshape(-1)    
    for i in range(y_true.shape[0]):
        a = y_true[i]
        b = y_pred[i]
        c = a+b
        if c == 0:
            continue
        out += math.fabs(a - b) / c
    out *= (200.0 / y_true.shape[0])
    return out


# In[ ]:




