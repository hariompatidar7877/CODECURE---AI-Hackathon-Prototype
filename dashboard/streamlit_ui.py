import streamlit as st
from workflows.agent_pipeline import AgentPipeline

pipeline = AgentPipeline()

st.title("Epidemic Spread Prediction Agentic AI")

country = st.text_input("Enter Country")

if st.button("Predict"):

    prediction, trend, risk, explanation, policy = pipeline.run(country)

    st.write("### Prediction:", prediction)
    st.write("### Trend:", trend)
    st.write("### Risk:", risk)
    st.write("### Explanation:", explanation)

    st.write("### Suggested Policies:")
    for p in policy:
        st.write("-", p)
