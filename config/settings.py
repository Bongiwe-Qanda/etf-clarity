import os
from dotenv import load_dotenv

load_dotenv()

# Database
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# ETF Tickers
TICKERS = ["STX40.JO", "STXNDQ.JO", "SYG4IR.JO"]

# Pipeline
HISTORY_PERIOD = "5y"
SCHEDULE_HOUR = 8
SCHEDULE_MINUTE = 0