import os
import streamlit as st
import pandas as pd
import altair as alt

from dotenv import load_dotenv
from utils.congress_api import search_bills
from utils.user_impact import get_user_impact
from utils.mistral_summary import get_mistral_summary
from utils.rag import get_rag_summary
from spark_model import predict_passage_probability

# Load environment variables
load_dotenv()

# Load static trend data
df_trends = pd.read_csv("data/topic_trends_by_year.csv")

# Streamlit configuration
st.set_page_config(page_title="PolicyPulse AI", layout="wide")
st.title("\U0001F4DC PolicyPulse AI")
st.markdown("Real-time U.S. policy explorer powered by Congress.gov, Mistral 7B, and LangChain.")

# Sidebar: User context
st.sidebar.header("\U0001F464 Your Info")
role = st.sidebar.text_input("Role (e.g. Parent, Veteran)", "Student")
state = st.sidebar.text_input("State (e.g. CA, NY)", "CA")

# Search input
query = st.text_input("\U0001F50D Search policy by keyword", "childcare")

if not query:
    st.stop()

try:
    search_result = search_bills(query)
    bills = search_result.get("bills", [])
except Exception as e:
    st.error(f"\u274C Failed to fetch bills: {e}")
    bills = []

if not bills:
    st.warning("No bills found.")
    st.stop()

# Bill selection dropdown
options = [f"{b['title']} ({b['number']})" for b in bills]
selection = st.selectbox("\U0001F4CC Select a bill", options)
selected = bills[options.index(selection)]

# Display selected bill details
st.subheader("\U0001F9FE Bill Details")
st.markdown(f"**Title:** {selected['title']}")
st.markdown(f"**Bill #:** {selected['number']}")
st.markdown(f"**Date Introduced:** {selected['introducedDate']}")
st.markdown(f"**Summary:** {selected['summary']}")

# Mistral Summary Button
if st.button("\U0001F9E0 Generate AI Summary with Mistral"):
    with st.spinner("Generating summary with Mistral 7B..."):
        summary = get_mistral_summary(selected["summary"])
        st.subheader("\U0001F4A1 Mistral AI Summary")
        st.write(summary)

# LangChain RAG Summary Button
if st.button("\U0001F50E Generate Contextual Summary with LangChain RAG"):
    with st.spinner("Running LangChain RAG over historical bills..."):
        summary = get_rag_summary(selected["summary"], all_bills=bills)
        st.subheader("\U0001F4DA LangChain RAG Summary")
        st.write(summary)

# Personalized impact section
st.subheader("\U0001F3DB️ Personalized Impact")
impact = get_user_impact(selected, role, state)
st.info(impact)

# Topic bar chart
st.subheader("\U0001F4CA Current Topics")
topics = selected.get("topics", [])
if topics:
    topic_df = pd.DataFrame({"Topic": topics})
    chart = alt.Chart(topic_df).mark_bar().encode(
        x="Topic", y='count()', color="Topic"
    )
    st.altair_chart(chart, use_container_width=True)
else:
    st.warning("No topics tagged to this bill.")

# Trends over time line chart
st.subheader("\U0001F4C8 Topic Trends Over Time")
trend_chart = alt.Chart(df_trends).mark_line(point=True).encode(
    x="Year:O", y="Count:Q", color="Topic:N"
).properties(height=300)
st.altair_chart(trend_chart, use_container_width=True)

# Passage probability prediction
st.subheader("\U0001F52E Passage Probability Prediction")
prob = predict_passage_probability(bills)
st.metric(label="Probability of Passage", value=prob)
