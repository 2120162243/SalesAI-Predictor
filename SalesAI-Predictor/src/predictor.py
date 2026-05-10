from sklearn.linear_model import LinearRegression
import pandas as pd

class SalesPredictor:
    def __init__(self):
        self.model = LinearRegression()
    
    def train(self, data: pd.DataFrame, feature_cols, target_col):
        self.model.fit(data[feature_cols], data[target_col])
    
    def predict(self, data: pd.DataFrame, feature_cols):
        return self.model.predict(data[feature_cols])
