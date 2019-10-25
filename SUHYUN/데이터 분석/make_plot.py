#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def make_plot(df, i):
    """
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(20,10))
    plt.plot(df.iloc[:, i], label = df.iloc[:, i].name)
    plt.plot(df.iloc[:, i+1], label = df.iloc[:, i+1].name)
    plt.plot(df.iloc[:, i+2], label = df.iloc[:, i+2].name)
    plt.plot(df.iloc[:, i+3], label = df.iloc[:, i+3].name)
    plt.plot(df.iloc[:, i+4], label = df.iloc[:, i+4].name)

    plt.xlabel('Time-hour')
    plt.ylabel('Amount')
    plt.title('Power demand(kwh)')
    plt.legend()
    return plt.show()
    """
    
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(20,10))
    plt.plot(df.iloc[:, i], label = df.iloc[:, i].name)
    plt.plot(df.iloc[:, i+1], label = df.iloc[:, i+1].name)
    plt.plot(df.iloc[:, i+2], label = df.iloc[:, i+2].name)
    plt.plot(df.iloc[:, i+3], label = df.iloc[:, i+3].name)
    plt.plot(df.iloc[:, i+4], label = df.iloc[:, i+4].name)

    plt.xlabel('Time-hour')
    plt.ylabel('Amount')
    plt.title('Power demand(kwh)')
    plt.legend()
    return plt.show()

