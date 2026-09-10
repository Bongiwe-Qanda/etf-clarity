import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from analysis.explainer import explain_etf
from analysis.calculator import calculate_scenario


def main():
    print("===========WELCOME TO ETF-CLARITY============")

    etf = input("Which ETF  do you want to look at? ")
    explained = explain_etf(etf)

    monthly_investment = float(input("How much do you want to invest per month? "))
    years = int(input("How many years do you want to invest for? "))
    annual_interest_rate = explained["return_1y"]
    calculate_scenario(monthly_investment,years,annual_interest_rate)

main()

