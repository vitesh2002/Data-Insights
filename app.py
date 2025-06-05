import streamlit as st
import pandas as pd
from openai import OpenAI

client = OpenAI(api_key="your_openai_api_key_here")
from datetime import datetime

# Load your cleaned dataset
df = pd.read_csv("shopify_reviews_cleaned.csv")

# Set your OpenAI API key here (you can load from environment or secrets)

# Streamlit app layout
st.title("📦 Shopify Review Insights")
st.markdown("Ask your question below and get instant AI-powered answers based on the customer reviews dataset.")

# Filters
with st.sidebar:
    st.header("🔍 Filters")
    selected_country = st.selectbox("Select Shipping Country (Optional)", ["All"] + sorted(df["Shipping Country"].dropna().unique().tolist()))
    rating_range = st.slider("Select Rating Range", 1, 5, (1, 5))
    show_data = st.checkbox("Show filtered data", False)

# Apply filters
filtered_df = df[
    (df["Rating"].between(rating_range[0], rating_range[1]))
]

if selected_country != "All":
    filtered_df = filtered_df[filtered_df["Shipping Country"] == selected_country]

if show_data:
    st.write("### Filtered Data Preview", filtered_df.head(20))

# Ask your question
user_question = st.text_area("💬 Ask a Question", placeholder="e.g., Which product categories have the most 1-star reviews in Canada?")

if st.button("Get Answer"):
    if not user_question.strip():
        st.warning("Please enter a question.")
    else:
        # Prepare a system prompt
        context = f"You are a data analyst assistant. Based on this customer reviews dataset with the following structure: \n\nColumns: {', '.join(filtered_df.columns)}\n\nTotal Rows: {len(filtered_df)}\n\nHere's a sample:\n{filtered_df.head(5).to_dict(orient='records')}\n\nAnswer the following question clearly and concisely:"

        # Call the OpenAI API
        try:
            response = client.chat.completions.create(model="gpt-4",
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": user_question}
            ],
            temperature=0.5)
            st.success("✅ Answer")
            st.markdown(response.choices[0].message.content)
        except Exception as e:
            st.error(f"OpenAI API call failed: {e}")
