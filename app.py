import streamlit as st
import pickle
import re
import string
import google.generativeai as genai
from newspaper import Article

#Loading data
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) 
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)    
    return text

#Streamlit 
st.set_page_config(page_title="AI Fake News Detector", page_icon="🛡️")
st.markdown("### Welcome to the **AI-powered Fake News Detector**")
st.write("Paste a news snippet or provide a link to a news article, and our ML model will verify its authenticity.")

input_type = st.radio("Choose Input Type:", ["Text", "URL Link"])
user_input = st.text_area("Enter News Headline or Article Link:")

if st.button("Analyze News"):
    final_text = ""
    
    if input_type == "URL Link" and user_input.startswith("http"):
        try:
            article = Article(user_input)
            article.download()
            article.parse()
            final_text = article.text
            st.success(f"Scraped Article: {article.title}")
        except:
            st.error("Failed to scrape the link. Please paste the text instead.")
    else:
        final_text = user_input

    if final_text:
        cleaned = clean_text(final_text)
        vectorized = vectorizer.transform([cleaned])
        prediction = model.predict(vectorized)
        
        if prediction[0] == 0:
            st.error("🚨 Result: THIS NEWS IS LIKELY FAKE")
            
            st.subheader("🔍 Why is this fake? (AI Insights)")
            with st.spinner("Gemini is fact-checking..."):
                prompt = f"Fact check this news: '{final_text}'. Explain why it is considered misinformation."
                response = genai.GenerativeModel('gemini-flash-latest').generate_content(prompt)
                st.write(response.text)
        else:
            st.success("✅ Result: THIS NEWS LOOKS REAL")
