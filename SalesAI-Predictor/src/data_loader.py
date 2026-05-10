import pandas as pd
import yaml

def load_config(path="config/config.yaml"):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def load_crm_data(path="data/sample_crm.csv"):
    return pd.read_csv(path)

def load_market_data(path="data/sample_market.csv"):
    return pd.read_csv(path)

def merge_data(crm, market):
    return pd.merge(crm, market, on='Date', how='left')
