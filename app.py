import streamlit as st
from planners.trip_planner import plan_trip
from planners.finance_planner import finance_agent

st.set_page_config(page_title="GenAI Lab Assignment", layout="wide")

# ---------------- Sidebar ----------------
with st.sidebar:
    st.header("Status")
    st.success("MCP Server: Running")
    st.info("Weather Tool: Enabled")
    st.info("Finance Tools: Enabled")

    st.divider()
    st.caption("Screenshots required:")
    st.markdown("""
    • App UI  
    • Trip output  
    • Finance output  
    • MCP /docs  
    """)

# ---------------- Main UI ----------------
st.title("GenAI Lab Assignment – MCP Based Agents")

# 🔴 TABS MUST BE DEFINED FIRST
tabs = st.tabs([
    "Problem 1: Trip Planner",
    "Problem 2: Currency & Stock Agent"
])

# ---------------- Problem 1 ----------------
with tabs[0]:
    st.subheader("Trip Planner Agent")

    col1, col2 = st.columns(2)

    with col1:
        city = st.text_input("Destination City", "Tokyo")
        month = st.text_input("Travel Month", "May")
        days = st.number_input("Trip Duration (days)", 1, 10, 3)

    with col2:
        origin = st.text_input("Origin City", "Bangalore")
        interests = st.text_input("Interests", "culture, food, history")

    prompt = st.text_area(
        "Prompt",
        "Plan a 3-day trip to Tokyo in May"
    )

    if st.button("Generate Trip Plan"):
        with st.spinner("Calling MCP Weather Tool..."):
            result = plan_trip(city, days, month, interests)
            st.markdown(result)

# ---------------- Problem 2 ----------------
with tabs[1]:
    st.subheader("Currency & Stock Market Agent")

    country = st.selectbox(
        "Select Country",
        ["Japan", "India", "US", "UK", "China", "South Korea"]
    )

    prompt = st.text_area(
        "Prompt",
        f"Give me currency and stock market details for {country}"
    )

    if st.button("Generate Market Info"):
        with st.spinner("Calling MCP Finance Tools..."):
            result = finance_agent(country)
            st.markdown(result)
