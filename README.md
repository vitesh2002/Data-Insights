# 🛍️ Shopify Review Insights with AI

This project analyzes customer reviews from a Shopify store using AI-powered tools. It cleans a messy review dataset, extracts key business insights using large language models (LLMs), and provides a user-friendly Streamlit interface for non-technical stakeholders to query the data in natural language.

---

## 🚀 Features

- ✅ Data cleaning (timestamps, categories, missing fields)
- 📊 Insight generation with ChatGPT (OpenAI)
- 🧠 Stakeholder questions answered using LLMs
- 🎛️ Interactive Streamlit interface with filters
- 💬 Ask natural language questions like:
  - “Which product categories have the most 1-star reviews in Canada?”
  - “Do higher order values correlate with lower ratings?”
  - “Summarize the top complaints and compliments.”
  -  Filter data by country, rating, and more

---

## 🧰 Tech Stack

- Python (pandas, datetime)
- OpenAI GPT-4
- Streamlit (for the interactive UI)
- CSV/JSON data handling

---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/vitesh2002/Data-Insights.git
   cd /Data-Insights

2. **Add your OpenAI API key**
   - Edit app.py and replace:
   ```bash
   openai.api_key = "your_openai_api_key_here"
3. **Run the Streamlit app** 
   ```bash
   streamlit run app.py
