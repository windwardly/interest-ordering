#!/usr/bin/env python3

# Play out a scenario, returning what is in savings account after 10 years
# month_interest is for the savings account
# income is bumped every year according to income_rate (inrate)
# spending is bumped every year according to spending_rate (outrate)
# Note: the final income and spending levels will be the same for
# any sorting of inrates and outrates, because it is just multiplying
# all the rates together times initial income or spending.
def play_out(income, spend, interest, inrates, outrates):
    monthly_savings_interest = 1.0 + (interest / (12.0 * 100.0));
    savings = 0.0;
    for year in range(len(inrates)):
        # print("inrates", (inrates[year] / 100.0))
        income *= 1.0 + (inrates[year] / 100.0)
        spend *= 1.0 + (outrates[year] / 100.0)
        for month in range(12):
            savings += income - spend
            savings *= monthly_savings_interest
            # print("Year", year + 1, "Month", month + 1,
            #    "Income", income, "Spend", spend, "Savings", savings)
    # uncomment for sanity check that this is the same in all scenarios
    # print("Income", '${:,.2f}'.format(income),
    #    "Spending", '${:,.2f}'.format(spend))
    return savings

# encapsulate python formatting
def format_money(amount):
    return '${:,.2f}'.format(amount)

def format_list(list):
    return ', '.join(['{:.2f}'.format(rate) for rate in list])

# The annual percentage rate at which income goes up.
income_rate = [3.4, 1.8, 1.4, 1.8, 0.1, 0.3, 2.1, 2.6, 1.4, 1.4, 5.5]
income_rate_lo_to_hi = income_rate.copy()
income_rate_lo_to_hi.sort()
income_rate_hi_to_lo = income_rate_lo_to_hi.copy()
income_rate_hi_to_lo.reverse()
income_ave = sum(income_rate) / len(income_rate)

# The annual inflation rate experienced.
spending_rate = [2.8, 2.9, 2.8, 3.1, 3.8, 3.1, 3.2, 3.9, 3.5, 1.6, 2.1]
spending_rate_lo_to_hi = spending_rate.copy()
spending_rate_lo_to_hi.sort()
spending_rate_hi_to_lo = spending_rate_lo_to_hi.copy()
spending_rate_hi_to_lo.reverse()
spending_ave = sum(spending_rate) / len(spending_rate)

income = 6000.0;    # monthly income stream
spend = 3000.0;     # monthly spending
savings_rates = [0.0, 5.0]

strategies = [
        ("Worst   ", income_rate_lo_to_hi, spending_rate_hi_to_lo),
        ("Unsorted", income_rate, spending_rate),
        ("Best    ", income_rate_hi_to_lo, spending_rate_lo_to_hi),
    ]

print()
print("Percent annual increases:")
print("Income  ", format_list(income_rate))
print("Average ", format_list([income_ave]))
print()
print("Spending", format_list(spending_rate))
print("Average ", format_list([spending_ave]))
print()
print("Ave Diff", format_list([spending_ave - income_ave]))
print()
print("Results below show that with no time value of money, order matters.")
print("And shows that with some actual time value of money, it matters more.")
print()
print("This is with starting monthly income of", '${:,.2f}'.format(income))
print("and with starting monthly spending of", '${:,.2f}'.format(spend))
print("and with a starting bank account balance of $0.00")
print()
print("Bank balance after", len(income_rate), "years")
print("with different sortings on rate increases")
for interest in savings_rates:
    print()
    print("Interest", '{:.2f}%'.format(interest))
    for (scenario, inrates, outrates) in strategies:
        print (scenario, format_money(play_out(income, spend, interest, inrates, outrates)))
print()
print("Show what it is like to have same inflation rates")
print("Same: spending inflation set equal to income inflation")
print("Different: the above 'Unsorted' case where inflation rates are different")
print("Same rates minus different rates = extra savings")
for interest in savings_rates:
    print()
    print("Interest", '{:.2f}%'.format(interest))
    different = play_out(income, spend, interest, income_rate, spending_rate)
    same = play_out(income, spend, interest, income_rate, income_rate)
    print(format_money(same), '-', format_money(different), '=', format_money(same-different))
print()
