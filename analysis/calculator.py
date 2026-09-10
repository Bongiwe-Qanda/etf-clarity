#If I invest a fixed amount every month for X years what will I end up with?

import os
import sys

def calculate_scenario(monthly_investment, years, annual_return_rate):
    monthly_rate = annual_return_rate / 100 / 12
    months = years * 12

    future_value = monthly_investment * (((1+ monthly_rate) ** months -1)/ monthly_rate)
    total_invested = monthly_investment * months
    profit = future_value - total_invested

    print(f"""
If you invest R{monthly_investment:,.2f}/month for {years} years at {annual_return_rate}% annual return:
Total invested: R{total_invested:,.2f}
Estimated value: R{future_value:,.2f}
Profit: R{profit:,.2f}
""")
    return {
        "total_invested": total_invested,
        "estimated_value": future_value,
        "profit": profit
    }


if __name__ == "__main__":
    calculated = calculate_scenario(500,5,13.17)
    print(calculated)
