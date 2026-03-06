import streamlit as st
import os
from anthropic import Anthropic

st.set_page_config(page_title="AI Campaign Diagnosis Agent")

st.title("AI Campaign Performance Diagnosis Agent")
st.write("Enter your campaign metrics below:")

ctr = st.text_input("CTR (%)")
cvr = st.text_input("Conversion Rate (%)")
bounce = st.text_input("Bounce Rate (%)")
cpa = st.text_input("CPA (£)")
target_cpa = st.text_input("Target CPA (£)")

if st.button("Diagnose Campaign"):

    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if not api_key:
        st.error("API key not found.")
    else:
        client = Anthropic(api_key=api_key)

        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=500,
            messages=[
                {
                    "role": "user",
                    "content": f"""
You are a marketing performance analyst.

Analyse the campaign metrics below and:
1. Identify the primary performance issue.
2. Identify secondary issues.
3. Explain your reasoning.
4. Recommend 3 specific improvements.
5. Provide a confidence level.

Campaign Goal: Reduce CPA to {target_cpa}

Metrics:
CTR: {ctr}%
Conversion Rate: {cvr}%
Bounce Rate: {bounce}%
CPA: £{cpa}
"""
                }
            ],
        )

        st.subheader("Diagnosis & Recommendations")
        st.write(response.content[0].text)
