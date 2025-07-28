import streamlit as st

pages = {
    "Overview": [
        st.Page("net_worth.py", title="🧮 Net Worth"),
        st.Page("spending_income.py", title="📊 Spending vs Income"),
        st.Page("health_check.py", title="🚦 Health Check"),
    ],
    "Cash Flow": [
        st.Page("monthly_tracker.py", title="📆 Monthly Tracker"),
        st.Page("budget_actual.py", title="✅ Budget vs Actual"),
        st.Page("account_balances.py", title="💳 Account Balances"),
    ],
    "Investments": [
        st.Page("portfolio_overview.py", title="💹 Portfolio Overview"),
        st.Page("asset_allocation.py", title="⚖️ Asset Allocation"),
        st.Page("rebalancing_flags.py", title="🔁 Rebalancing Flags"),
    ],
    "Freedom Plan": [
        st.Page("fire_progress.py", title="🎯 FIRE Progress"),
        st.Page("goal_forecast.py", title="📅 Goal Forecast"),
        st.Page("simulators.py", title="🧪 Simulators"),
    ],
}

pg = st.navigation(pages)
pg.run()