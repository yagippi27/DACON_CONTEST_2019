#!/usr/bin/env python
# coding: utf-8

# In[2]:


## anaconda에서 numba를 찾은 후, 설치해 주세요.

# @jit
def smape_fast(y_true, y_pred):
    from numba import jit
    import math
    out = 0
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




