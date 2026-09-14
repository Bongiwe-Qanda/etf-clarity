import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

from config.settings import TICKERS, SCHEDULE_HOUR, SCHEDULE_MINUTE
from etl.fetch import fetch_etf_data
from etl.transform import transform_raw_data
from db.load import load_etf_data

from apscheduler.schedulers.blocking import BlockingScheduler

def run_pipeline():

    for ticker in TICKERS:
        logger.info(f"Running pipeline for {ticker}")
        raw_data = fetch_etf_data(ticker)
        clean_data = transform_raw_data(raw_data)
        load_etf_data(clean_data,ticker)
        logger.info(f"Pipeline completed for {ticker}")


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(run_pipeline, 'cron', hour=SCHEDULE_HOUR, minute=SCHEDULE_MINUTE)
    print("Scheduler started - pipeline runs daily at 08:00")
    scheduler.start()
