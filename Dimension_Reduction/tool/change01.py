import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def change(datapath, column1, column2, savename):
    data = pd.read_csv(datapath)

    scaler = MinMaxScaler()
    data[[column1, column2]] = scaler.fit_transform(data[[column1, column2]])

    data.to_csv(savename, index=False)
