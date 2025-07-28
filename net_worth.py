import streamlit as st
import json
import locale
import pandas as pd
locale.setlocale(locale.LC_ALL, 'en_AU.UTF-8')

def get_net_worth(assets_data:dict) -> int:
    net_worth = 0
    for category in assets_data:
        net_worth = net_worth + sum(assets_data[category].values())
    return net_worth

def get_actual_spending(cash_flow_data:dict) -> int:
    actual_spending = 0
    for item in cash_flow_data:
        if item != "Savings and Investments":
            actual_spending = actual_spending + sum(cash_flow_data[item].values())
    return actual_spending

def get_emergency_fund_target(actual_spending:int, months:int) -> int:
    """Ideal value 6 months of essenial expenses"""
    return actual_spending * months

def get_net_worth_trend(previous_month_net_worth:int, latest_month_net_worth:int) -> str:
    net_performance = ((latest_month_net_worth - previous_month_net_worth)/previous_month_net_worth)*100
    if latest_month_net_worth > previous_month_net_worth:
        return f":green-badge[↑ +{net_performance:.2f} %]"
    else:
        return f":red-badge[↓ {net_performance:.2f} %]"

def get_asset_percentage(net_worth:int ,asset:int) -> str:
    percentage = (asset*100)/net_worth
    return f"{percentage:.2f}"

with open('data/assets.json', 'r') as file:
    assets_data = json.loads(file.read())

with open('data/cash_flow.json', 'r') as file:
    cash_flow_data = json.loads(file.read())



previous_month_assets = assets_data[-2]
previous_month_net_worth = get_net_worth(previous_month_assets)
latest_month_assets = assets_data[-1]
latest_month_net_worth = get_net_worth(latest_month_assets)

st.html("<h1>Summary Overview</h1>")
st.html(f'<strong>Net Worth</strong>: {locale.currency(latest_month_net_worth, grouping=True)} AUD')
st.markdown(f'{get_net_worth_trend(previous_month_net_worth, latest_month_net_worth)} from last moth.')

st.html("<h1>Asset Breakdown</h1>")
st.markdown("💰 Cash")
cash_data = latest_month_assets['Cash'].copy()
# Format all AUD values
for item in cash_data:
    cash_data[item] = locale.currency(cash_data[item], grouping=True)
df_cash = pd.DataFrame(list(cash_data.items()), columns=['Item', 'Current Value (AUD)'])
st.dataframe(df_cash, hide_index=True)

st.markdown("📈 Investments")
investmenst_data = latest_month_assets['Investments'].copy()
# Format all AUD values
for item in investmenst_data:
    investmenst_data[item] = locale.currency(investmenst_data[item], grouping=True)
df_investments = pd.DataFrame(list(investmenst_data.items()), columns=['Item', 'Current Value (AUD)'])
st.dataframe(df_investments, hide_index=True)

st.markdown("🏠 Assets")
assets_data = latest_month_assets['Assets'].copy()
# Format all AUD values
for item in assets_data:
    assets_data[item] = locale.currency(assets_data[item], grouping=True)
df_assets = pd.DataFrame(list(assets_data.items()), columns=['Item', 'Current Value (AUD)'])
st.dataframe(df_assets, hide_index=True)

st.html("<h1>Insights</h1>")

actual_spending = get_actual_spending(cash_flow_data)
emergency_fund_target = get_emergency_fund_target(actual_spending, 6)
st.markdown(f"🔴 Emergency Fund is {get_asset_percentage(emergency_fund_target, latest_month_assets['Cash']['Emergency Fund'])}% funded (Goal: {locale.currency(emergency_fund_target, grouping=True)}).")
st.markdown(f"🔴 Opportunity Fund is {get_asset_percentage(actual_spending, latest_month_assets['Cash']['Opportunity Fund'])}% funded (Goal: {locale.currency(actual_spending, grouping=True)}).")
st.markdown(f"🟢 Crypto is {get_asset_percentage(latest_month_net_worth, latest_month_assets['Investments']['Crypto'])} % of net worth.")