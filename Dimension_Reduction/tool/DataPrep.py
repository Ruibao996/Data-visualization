from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np

def data_prep(datapath, num_features, cat_features, date_feature, impute_strategy='mean', scale=True):
    """
    Data preparation
    :param data: The input data
    :param num_features: List of numerical feature names
    :param cat_features: List of categorical feature names
    :param date_feature: Name of the date feature
    :param impute_strategy: The imputation strategy
    :param scale: If True, scale the data
    :return: The prepared data
    """
    # Load the data
    data = pd.read_csv(datapath)

    # Convert date feature to numerical
    data[date_feature] = pd.to_datetime(data[date_feature])
    data['Year'] = data[date_feature].dt.year
    data['Month'] = data[date_feature].dt.month
    data['Day'] = data[date_feature].dt.day
    num_features += ['Year', 'Month', 'Day']

    # Define the transformers
    num_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy=impute_strategy)),
        ('scaler', StandardScaler())]) if scale else SimpleImputer(strategy=impute_strategy)

    cat_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))])

    # Combine the transformers
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', num_transformer, num_features),
            ('cat', cat_transformer, cat_features)])

    # Fit and transform the data
    data_prepared = preprocessor.fit_transform(data)

    return data_prepared