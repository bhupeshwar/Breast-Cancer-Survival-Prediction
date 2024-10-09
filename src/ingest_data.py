import os
import sys

# Add the project's root directory to sys.path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


import pandas as pd
from src.logger import get_console_logger
from typing import Optional

logger = get_console_logger('Data-ingestion')

## The data import from API is also imported here if there is any..
def ingest_data()-> pd.DataFrame:
    data = pd.read_csv("data\data.csv")
    return data