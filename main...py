import streamlit as st

# Markdown and Headings
html_temp = """ 
<div style="background-color: lightblue; padding: 16px">
<h2 style="color: black; text-align: center;">Financial Statement Calculation Web App</h2>
</div>
"""

st.markdown(html_temp, unsafe_allow_html=True)
st.write('')
st.write('')

# Function to calculate controlling and non-controlling interests
def calculate_interests(total_investment, parent_ownership):
    controlling_interest = total_investment * (parent_ownership / 100)
    non_controlling_interest = total_investment - controlling_interest
    return controlling_interest, non_controlling_interest

# Function to display results
def display_interests_results(subsidiary_name, controlling_interest, non_controlling_interest):
    st.write(f"Controlling Interest in {subsidiary_name}: {controlling_interest}")
    st.write(f"Non-Controlling Interest in {subsidiary_name}: {non_controlling_interest}")

# Input for user
st.header("Controlling and Non-Controlling Interest Calculator")

# Assumed values, replace with actual investment amounts and ownership percentages
total_investment_subsidiary1 = st.number_input("Enter Total Investment Amount in Subsidiary 1: ", min_value=0.0)
parent_ownership_subsidiary1 = st.number_input("Enter Parent Company's Ownership Percentage in Subsidiary 1: ", min_value=0.0, max_value=100.0)

total_investment_subsidiary2 = st.number_input("Enter Total Investment Amount in Subsidiary 2: ", min_value=0.0)
parent_ownership_subsidiary2 = st.number_input("Enter Parent Company's Ownership Percentage in Subsidiary 2: ", min_value=0.0, max_value=100.0)

total_investment_subsidiary3 = st.number_input("Enter Total Investment Amount in Subsidiary 3: ", min_value=0.0)
parent_ownership_subsidiary3 = st.number_input("Enter Parent Company's Ownership Percentage in Subsidiary 3: ", min_value=0.0, max_value=100.0)

# Calculate results
controlling_interest1, non_controlling_interest1 = calculate_interests(total_investment_subsidiary1, parent_ownership_subsidiary1)
controlling_interest2, non_controlling_interest2 = calculate_interests(total_investment_subsidiary2, parent_ownership_subsidiary2)
controlling_interest3, non_controlling_interest3 = calculate_interests(total_investment_subsidiary3, parent_ownership_subsidiary3)

# Display results
display_interests_results("Subsidiary 1", controlling_interest1, non_controlling_interest1)
display_interests_results("Subsidiary 2", controlling_interest2, non_controlling_interest2)
display_interests_results("Subsidiary 3", controlling_interest3, non_controlling_interest3)


def calculate_amortization(initial_intangible_assets, accumulated_amortization):
    amortization_expense = max(0, initial_intangible_assets - accumulated_amortization) / useful_life
    return amortization_expense

# Function to display results
def display_amortization_results(amortization_expense):
    st.write(f"Annual Amortization Expense: {amortization_expense}")

# Input for user
st.header("Amortization Expense Calculator")

# Assumed values, replace with actual values from your financial statements
initial_intangible_assets = st.number_input("Enter Initial Intangible Assets Value: ", min_value=0.0)
accumulated_amortization = st.number_input("Enter Accumulated Amortization: ", min_value=0.0)
useful_life = st.number_input("Enter Useful Life of Intangible Assets (in years): ", min_value=1)

# Calculate results
amortization_expense = calculate_amortization(initial_intangible_assets, accumulated_amortization)

# Display results
display_amortization_results(amortization_expense)


# Function to calculate fair value of assets
def calculate_fair_value(initial_book_value, accumulated_depreciation, market_conditions_adjustment):
    fair_value = initial_book_value - accumulated_depreciation + market_conditions_adjustment
    return max(0, fair_value)

# Function to display results
def display_fair_value_results(fair_value):
    st.write(f"Fair Value of Assets: {fair_value}")

# Input for user
st.header("Fair Value of Assets Calculator")

# Assumed values, replace with actual values from your financial statements
initial_book_value = st.number_input("Enter Initial Book Value of Assets: ", min_value=0.0)
accumulated_depreciation = st.number_input("Enter Accumulated Depreciation: ", min_value=0.0)
market_conditions_adjustment = st.number_input("Enter Market Conditions Adjustment: ", min_value=0.0)

# Calculate results
fair_value = calculate_fair_value(initial_book_value, accumulated_depreciation, market_conditions_adjustment)

# Display results
display_fair_value_results(fair_value)


# Function to calculate Goodwill
def calculate_goodwill(acquisition_cost, fair_value_identifiable_net_assets):
    goodwill = max(0, acquisition_cost - fair_value_identifiable_net_assets)
    return goodwill

# Function to display results
def display_goodwill_results(goodwill):
    st.write(f"Goodwill: {goodwill}")

# Input for user
st.header("Goodwill Calculator")

# Assumed values, replace with actual values from your financial statements
acquisition_cost = st.number_input("Enter Acquisition Cost: ", min_value=0.0)
fair_value_identifiable_net_assets = st.number_input("Enter Fair Value of Identifiable Net Assets: ", min_value=0.0)

# Calculate results
goodwill = calculate_goodwill(acquisition_cost, fair_value_identifiable_net_assets)

# Display results
display_goodwill_results(goodwill)

# Function to calculate impairments
def calculate_impairments(carrying_value, recoverable_amount):
    impairment_loss = max(0, carrying_value - recoverable_amount)
    return impairment_loss

# Function to display results
def display_impairments_results(impairment_loss):
    st.write(f"Impairment Loss: {impairment_loss}")

# Input for user
st.header("Impairments Calculator")

# Assumed values, replace with actual values from your financial statements
carrying_value = st.number_input("Enter Carrying Value of the Asset: ", min_value=0.0)
recoverable_amount = st.number_input("Enter Recoverable Amount of the Asset: ", min_value=0.0)

# Calculate results
impairment_loss = calculate_impairments(carrying_value, recoverable_amount)

# Display results
display_impairments_results(impairment_loss)


# Function to calculate fixed assets schedule
def calculate_fixed_assets_schedule(beginning_fixed_assets, additions, disposals, depreciation_expense):
    ending_fixed_assets = beginning_fixed_assets + additions - disposals - depreciation_expense
    return ending_fixed_assets

# Function to display results
def display_fixed_assets_schedule_results(ending_fixed_assets):
    st.write(f"Ending Fixed Assets: {ending_fixed_assets}")

# Input for user
st.header("Fixed Assets Schedule Calculator")

# Assumed values, replace with actual values from your financial statements
beginning_fixed_assets = st.number_input("Enter Beginning Fixed Assets: ", min_value=0.0)
additions = st.number_input("Enter Additions to Fixed Assets: ", min_value=0.0)
disposals = st.number_input("Enter Disposals of Fixed Assets: ", min_value=0.0)
depreciation_expense = st.number_input("Enter Depreciation Expense: ", min_value=0.0)

# Calculate results
ending_fixed_assets = calculate_fixed_assets_schedule(beginning_fixed_assets, additions, disposals, depreciation_expense)

# Display results
display_fixed_assets_schedule_results(ending_fixed_assets)


# Function to calculate Operating Profit
def calculate_operating_profit(revenue, cost_of_sales, selling_costs, admin_expenses):
    return revenue - cost_of_sales - selling_costs - admin_expenses

# Function to calculate Net Finance Costs
def calculate_net_finance_costs(fin_income, fin_costs):
    return fin_income - fin_costs

# Function to calculate Profit Before Taxation
def calculate_profit_before_tax(operating_profit, net_finance_costs):
    return operating_profit + net_finance_costs

# Function to calculate Taxation
def calculate_taxation(profit_before_tax):
    return 0.2 * profit_before_tax  # Assuming a tax rate of 20%

# Function to calculate Profit for the Year
def calculate_profit_for_year(profit_before_tax, taxation):
    return profit_before_tax - taxation

# Function to display results
def display_income_statement_results(operating_profit, net_finance_costs, profit_before_tax, taxation, profit_for_year):
    st.write(f"Operating Profit: N{operating_profit}m")
    st.write(f"Net Finance Costs: N{net_finance_costs}m")
    st.write(f"Profit Before Taxation: N{profit_before_tax}m")
    st.write(f"Taxation: N{taxation}m")
    st.write(f"Profit for the Year: N{profit_for_year}m")

# Input for user
st.header("Income Statement Calculator")
revenue = st.number_input("Enter Revenue: ", min_value=0.0)
cost_of_sales = st.number_input("Enter Cost of Sales: ", min_value=0.0)
selling_costs = st.number_input("Enter Selling and Distribution Costs: ", min_value=0.0)
admin_expenses = st.number_input("Enter Administrative Expenses: ", min_value=0.0)
fin_income = st.number_input("Enter Finance Income: ", min_value=0.0)
fin_costs = st.number_input("Enter Finance Costs: ", min_value=0.0)

# Calculate results
operating_profit = calculate_operating_profit(revenue, cost_of_sales, selling_costs, admin_expenses)
net_finance_costs = calculate_net_finance_costs(fin_income, fin_costs)
profit_before_tax = calculate_profit_before_tax(operating_profit, net_finance_costs)
taxation = calculate_taxation(profit_before_tax)
profit_for_year = calculate_profit_for_year(profit_before_tax, taxation)

# Display results
display_income_statement_results(operating_profit, net_finance_costs, profit_before_tax, taxation, profit_for_year)


# Function to calculate Total Non-current Assets
def calculate_total_non_current_assets(goodwill, property_plant_equipment, long_term_lease_assets, net_investments_joint_ventures, deferred_tax_assets, tax_receivable, retirement_benefit_surplus):
    return goodwill + property_plant_equipment + long_term_lease_assets + net_investments_joint_ventures + deferred_tax_assets + tax_receivable + retirement_benefit_surplus

# Function to calculate Total Current Assets
def calculate_total_current_assets(inventories, trade_receivables, derivative_financial_assets, current_tax_receivable, current_asset_investments, cash_short_term_deposits, assets_held_for_sale):
    return inventories + trade_receivables + derivative_financial_assets + current_tax_receivable + current_asset_investments + cash_short_term_deposits + assets_held_for_sale

# Function to calculate Total Assets
def calculate_total_assets(total_non_current_assets, total_current_assets):
    return total_non_current_assets + total_current_assets

# Function to calculate Total Equity
def calculate_total_equity(share_capital, currency_translation_reserve, capital_redemption_reserve, other_reserve, hedging_reserve, retained_earnings, non_controlling_interests):
    return share_capital + currency_translation_reserve + capital_redemption_reserve + other_reserve + hedging_reserve + retained_earnings + non_controlling_interests

# Function to calculate Total Non-current Liabilities
def calculate_total_non_current_liabilities(borrowings, other_payables, long_term_lease_liability, deferred_tax_liabilities, retirement_long_term_employee_benefit_obligations):
    return borrowings + other_payables + long_term_lease_liability + deferred_tax_liabilities + retirement_long_term_employee_benefit_obligations

# Function to calculate Total Current Liabilities
def calculate_total_current_liabilities(overdrafts, trade_other_payables, short_term_lease_liability, derivative_financial_liabilities, current_tax_payable, provisions, liabilities_associated_assets_held_for_sale):
    return overdrafts + trade_other_payables + short_term_lease_liability + derivative_financial_liabilities + current_tax_payable + provisions + liabilities_associated_assets_held_for_sale

# Function to calculate Total Liabilities
def calculate_total_liabilities(total_non_current_liabilities, total_current_liabilities):
    return total_non_current_liabilities + total_current_liabilities

# Function to display results
def display_balance_sheet_results(total_non_current_assets, total_current_assets, total_assets, total_equity, total_non_current_liabilities, total_current_liabilities, total_liabilities):
    st.write(f"Total Non-current Assets: N{total_non_current_assets}m")
    st.write(f"Total Current Assets: N{total_current_assets}m")
    st.write(f"Total Assets: N{total_assets}m")
    st.write(f"Total Equity: N{total_equity}m")
    st.write(f"Total Non-current Liabilities: N{total_non_current_liabilities}m")
    st.write(f"Total Current Liabilities: N{total_current_liabilities}m")
    st.write(f"Total Liabilities: N{total_liabilities}m")

# Input for user
st.header("Balance Sheet Calculator")
goodwill = st.number_input("Enter Goodwill and Other Intangible Assets: ", min_value=0.0)
property_plant_equipment = st.number_input("Enter Property, Plant, and Equipment: ", min_value=0.0)
long_term_lease_assets = st.number_input("Enter Long-term Right-of-use Assets: ", min_value=0.0)
net_investments_joint_ventures = st.number_input("Enter Net Investments in Joint Ventures: ", min_value=0.0)
deferred_tax_assets = st.number_input("Enter Deferred Tax Assets: ", min_value=0.0)
tax_receivable = st.number_input("Enter Tax Receivable: ", min_value=0.0)
retirement_benefit_surplus = st.number_input("Enter Retirement Benefit Surplus: ", min_value=0.0)
inventories = st.number_input("Enter Inventories: ", min_value=0.0)
trade_receivables = st.number_input("Enter Trade and Other Receivables: ", min_value=0.0)
derivative_financial_assets = st.number_input("Enter Derivative Financial Assets: ", min_value=0.0)
current_tax_receivable = st.number_input("Enter Current Tax Receivable: ", min_value=0.0)
current_asset_investments = st.number_input("Enter Current Asset Investments: ", min_value=0.0)
cash_short_term_deposits = st.number_input("Enter Cash and Short-term Deposits: ", min_value=0.0)
assets_held_for_sale = st.number_input("Enter Assets Held for Sale: ", min_value=0.0)
share_capital = st.number_input("Enter Share Capital: ", min_value=0.0)
currency_translation_reserve = st.number_input("Enter Currency Translation Reserve: ", min_value=0.0)
capital_redemption_reserve = st.number_input("Enter Capital Redemption Reserve: ", min_value=0.0)
other_reserve = st.number_input("Enter Other Reserve: ", min_value=0.0)
hedging_reserve = st.number_input("Enter Hedging Reserve: ", min_value=0.0)
retained_earnings = st.number_input("Enter Retained Earnings: ", min_value=0.0)
non_controlling_interests = st.number_input("Enter Non-controlling Interests: ", min_value=0.0)
borrowings = st.number_input("Enter Borrowings: ", min_value=0.0)
other_payables = st.number_input("Enter Other Payables: ", min_value=0.0)
long_term_lease_liability = st.number_input("Enter Long-term Lease Liability: ", min_value=0.0)
deferred_tax_liabilities = st.number_input("Enter Deferred Tax Liabilities: ", min_value=0.0)
retirement_long_term_employee_benefit_obligations = st.number_input("Enter Retirement and Other Long-term Employee Benefit Obligations: ", min_value=0.0)
overdrafts = st.number_input("Enter Overdrafts: ", min_value=0.0)
trade_other_payables = st.number_input("Enter Trade and Other Payables: ", min_value=0.0)
short_term_lease_liability = st.number_input("Enter Short-term Lease Liability: ", min_value=0.0)
derivative_financial_liabilities = st.number_input("Enter Derivative Financial Liabilities: ", min_value=0.0)
current_tax_payable = st.number_input("Enter Current Tax Payable: ", min_value=0.0)
provisions = st.number_input("Enter Provisions: ", min_value=0.0)
liabilities_associated_assets_held_for_sale = st.number_input("Enter Liabilities Associated with Assets Held for Sale: ", min_value=0.0)

# Calculate results
total_non_current_assets = calculate_total_non_current_assets(goodwill, property_plant_equipment, long_term_lease_assets, net_investments_joint_ventures, deferred_tax_assets, tax_receivable, retirement_benefit_surplus)
total_current_assets = calculate_total_current_assets(inventories, trade_receivables, derivative_financial_assets, current_tax_receivable, current_asset_investments, cash_short_term_deposits, assets_held_for_sale)
total_assets = calculate_total_assets(total_non_current_assets, total_current_assets)
total_equity = calculate_total_equity(share_capital, currency_translation_reserve, capital_redemption_reserve, other_reserve, hedging_reserve, retained_earnings, non_controlling_interests)
total_non_current_liabilities = calculate_total_non_current_liabilities(borrowings, other_payables, long_term_lease_liability, deferred_tax_liabilities, retirement_long_term_employee_benefit_obligations)
total_current_liabilities = calculate_total_current_liabilities(overdrafts, trade_other_payables, short_term_lease_liability, derivative_financial_liabilities, current_tax_payable, provisions, liabilities_associated_assets_held_for_sale)
total_liabilities = calculate_total_liabilities(total_non_current_liabilities, total_current_liabilities)

# Display results
display_balance_sheet_results(total_non_current_assets, total_current_assets, total_assets, total_equity, total_non_current_liabilities, total_current_liabilities, total_liabilities)


# Function to calculate Total Comprehensive Income
def calculate_total_comprehensive_income(loss_for_year, re_measurement_post_employment_obligations, exchange_differences_translation_foreign_operations, cash_flow_hedges, disposals_equity_reserves, deferred_tax_re_measurement_post_employment_obligations, deferred_tax_foreign_exchange_quasi_equity_loans):
    return loss_for_year + re_measurement_post_employment_obligations + exchange_differences_translation_foreign_operations + cash_flow_hedges + disposals_equity_reserves + deferred_tax_re_measurement_post_employment_obligations + deferred_tax_foreign_exchange_quasi_equity_loans

# Function to calculate Total Transactions with Owners
def calculate_total_transactions_with_owners(ordinary_dividends, non_controlling_interests_dividend_paid, acquisition_non_controlling_interests, share_based_payment_charges, sale_non_controlling_interests):
    return ordinary_dividends + non_controlling_interests_dividend_paid + acquisition_non_controlling_interests + share_based_payment_charges + sale_non_controlling_interests

# Function to calculate Total Equity
def calculate_total_equity_at_end(total_equity_beginning, total_comprehensive_income, total_transactions_with_owners):
    return total_equity_beginning + total_comprehensive_income + total_transactions_with_owners

# Function to display results
def display_changes_in_equity_results(total_comprehensive_income, total_transactions_with_owners, total_equity_at_end):
    st.write(f"Total Comprehensive Income: N{total_comprehensive_income}m")
    st.write(f"Total Transactions with Owners: N{total_transactions_with_owners}m")
    st.write(f"Total Equity at End: N{total_equity_at_end}m")

# Input for user
st.header("Statement of Changes in Equity Calculator")
loss_for_year = st.number_input("Enter Loss for the Year: ", min_value=0.0)
re_measurement_post_employment_obligations = st.number_input("Enter Re-measurement of Post-employment Benefit Obligations: ", min_value=0.0)
exchange_differences_translation_foreign_operations = st.number_input("Enter Exchange Differences on Translation of Foreign Operations: ", min_value=0.0)
cash_flow_hedges = st.number_input("Enter Cash Flow Hedges - Fair Value Loss in Year Net of Taxation: ", min_value=0.0)
disposals_equity_reserves = st.number_input("Enter Disposals - Recycle of Equity Reserves: ", min_value=0.0)
deferred_tax_re_measurement_post_employment_obligations = st.number_input("Enter Deferred Tax on Re-measurement of Post-employment Benefit Obligations: ", min_value=0.0)
deferred_tax_foreign_exchange_quasi_equity_loans = st.number_input("Enter Deferred Tax on Foreign Exchange Related to Quasi-equity Loans: ", min_value=0.0)
ordinary_dividends = st.number_input("Enter Ordinary Dividends: ", min_value=0.0)
non_controlling_interests_dividend_paid = st.number_input("Enter Non-controlling Interests Dividend Paid: ", min_value=0.0)
acquisition_non_controlling_interests = st.number_input("Enter Acquisition of Non-controlling Interests: ", min_value=0.0)
share_based_payment_charges = st.number_input("Enter Share-based Payment Charges: ", min_value=0.0)
sale_non_controlling_interests = st.number_input("Enter Sale of Non-controlling Interests: ", min_value=0.0)
total_equity_beginning = st.number_input("Enter Total Equity at the Beginning: ", min_value=0.0)

# Calculate results
total_comprehensive_income = calculate_total_comprehensive_income(loss_for_year, re_measurement_post_employment_obligations, exchange_differences_translation_foreign_operations, cash_flow_hedges, disposals_equity_reserves, deferred_tax_re_measurement_post_employment_obligations, deferred_tax_foreign_exchange_quasi_equity_loans)
total_transactions_with_owners = calculate_total_transactions_with_owners(ordinary_dividends, non_controlling_interests_dividend_paid, acquisition_non_controlling_interests, share_based_payment_charges, sale_non_controlling_interests)
total_equity_at_end = calculate_total_equity_at_end(total_equity_beginning, total_comprehensive_income, total_transactions_with_owners)

# Display results
display_changes_in_equity_results(total_comprehensive_income, total_transactions_with_owners, total_equity_at_end)


# Function to calculate Net Cash Generated from Operating Activities
def calculate_net_cash_operating_activities(cash_generated_from_operations, taxation_paid, interest_paid):
    return cash_generated_from_operations - taxation_paid - interest_paid

# Function to calculate Net Cash from Investing Activities
def calculate_net_cash_investing_activities(interest_income, investment_income, purchase_property_equipment, proceeds_disposal_ppe, cash_flow_disposal_companies, resolution_purchase_price_disposal_company, acquisition_subsidary, cash_receipts_joint_venture, cash_advances_loans_joint_venture):
    return interest_income + investment_income + proceeds_disposal_ppe + cash_flow_disposal_companies + resolution_purchase_price_disposal_company + cash_receipts_joint_venture + cash_advances_loans_joint_venture - purchase_property_equipment - acquisition_subsidary

# Function to calculate Net Cash Generated/Used in Financing Activities
def calculate_net_cash_financing_activities(dividends_paid_non_controlling, dividends_paid_company_shareholders, acquisition_non_controlling_interests, proceeds_loans_joint_venture, repayment_lease_liabilities, proceeds_repayment_loan_facility):
    return -dividends_paid_non_controlling - dividends_paid_company_shareholders - acquisition_non_controlling_interests + proceeds_loans_joint_venture - repayment_lease_liabilities + proceeds_repayment_loan_facility

# Function to calculate Net Increase in Cash and Cash Equivalents
def calculate_net_increase_cash_equivalents(net_cash_operating_activities, net_cash_investing_activities, net_cash_financing_activities):
    return net_cash_operating_activities + net_cash_investing_activities + net_cash_financing_activities

# Function to calculate Cash and Cash Equivalents at the End of the Year
def calculate_cash_equivalents_end(cash_equivalents_beginning, net_increase_cash_equivalents, effect_foreign_exchange_rates):
    return cash_equivalents_beginning + net_increase_cash_equivalents + effect_foreign_exchange_rates

# Function to display results
def display_cash_flow_statement_results(net_cash_operating_activities, net_cash_investing_activities, net_cash_financing_activities, net_increase_cash_equivalents, cash_equivalents_end):
    st.write(f"Net Cash Generated from Operating Activities: N{net_cash_operating_activities}m")
    st.write(f"Net Cash from Investing Activities: N{net_cash_investing_activities}m")
    st.write(f"Net Cash Generated/Used in Financing Activities: N{net_cash_financing_activities}m")
    st.write(f"Net Increase in Cash and Cash Equivalents: N{net_increase_cash_equivalents}m")
    st.write(f"Cash and Cash Equivalents at the End of the Year: N{cash_equivalents_end}m")

# Input for user
st.header("Cash Flow Statement Calculator")
cash_generated_from_operations = st.number_input("Enter Cash Generated from Operations: ", min_value=0.0)
taxation_paid = st.number_input("Enter Taxation Paid: ", min_value=0.0)
interest_paid = st.number_input("Enter Interest Paid: ", min_value=0.0)
interest_income = st.number_input("Enter Interest Income: ", min_value=0.0)
investment_income = st.number_input("Enter Investment Income: ", min_value=0.0)
purchase_property_equipment = st.number_input("Enter Purchase of Property, Plant, and Equipment: ", min_value=0.0)
proceeds_disposal_ppe = st.number_input("Enter Proceeds from Disposal of PPE: ", min_value=0.0)
cash_flow_disposal_companies = st.number_input("Enter Cash Flow from Disposal of Companies and Businesses: ", min_value=0.0)
resolution_purchase_price_disposal_company = st.number_input("Enter Resolution of Purchase Price from Disposal of Company: ", min_value=0.0)
acquisition_subsidary = st.number_input("Enter Acquisition of Subsidiary: ", min_value=0.0)
cash_receipts_joint_venture = st.number_input("Enter Cash Receipts from Repayment of Loans by Joint Venture: ", min_value=0.0)
cash_advances_loans_joint_venture = st.number_input("Enter Cash Advances and Loans Provided to Joint Venture: ", min_value=0.0)
dividends_paid_non_controlling = st.number_input("Enter Dividends Paid to Non-controlling Interests: ", min_value=0.0)
dividends_paid_company_shareholders = st.number_input("Enter Dividends Paid to Company Shareholders: ", min_value=0.0)

proceeds_loans_joint_venture = st.number_input("Enter Proceeds from Loans by Joint Ventures: ", min_value=0.0)
repayment_lease_liabilities = st.number_input("Enter Repayment of Lease Liabilities: ", min_value=0.0)
proceeds_repayment_loan_facility = st.number_input("Enter Proceeds from/Repayment of Loan Facility: ", min_value=0.0)
cash_equivalents_beginning = st.number_input("Enter Cash and Cash Equivalents at the Beginning of the Year: ", min_value=0.0)
effect_foreign_exchange_rates = st.number_input("Enter Effect of Foreign Exchange Rates: ", min_value=0.0)

# Calculate results
net_cash_operating_activities = calculate_net_cash_operating_activities(cash_generated_from_operations, taxation_paid, interest_paid)
net_cash_investing_activities = calculate_net_cash_investing_activities(interest_income, investment_income, purchase_property_equipment, proceeds_disposal_ppe, cash_flow_disposal_companies, resolution_purchase_price_disposal_company, acquisition_subsidary, cash_receipts_joint_venture, cash_advances_loans_joint_venture)
net_cash_financing_activities = calculate_net_cash_financing_activities(dividends_paid_non_controlling, dividends_paid_company_shareholders, acquisition_non_controlling_interests, proceeds_loans_joint_venture, repayment_lease_liabilities, proceeds_repayment_loan_facility)
net_increase_cash_equivalents = calculate_net_increase_cash_equivalents(net_cash_operating_activities, net_cash_investing_activities, net_cash_financing_activities)
cash_equivalents_end = calculate_cash_equivalents_end(cash_equivalents_beginning, net_increase_cash_equivalents, effect_foreign_exchange_rates)

# Display results
display_cash_flow_statement_results(net_cash_operating_activities, net_cash_investing_activities, net_cash_financing_activities, net_increase_cash_equivalents, cash_equivalents_end)


st.header('Thank You For Visiting And Using The Web Application')