<div align="center">
 
# 🛡️ AI-Powered Fake News Detector
 
**A hybrid intelligence system that combines traditional Machine Learning with Generative AI to detect and explain misinformation in real-time.**
 
[![Live Demo](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://fake-news-detector-harshal.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Accuracy](https://img.shields.io/badge/Accuracy-98.72%25-22C55E?style=for-the-badge)](/)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)
 
</div>
 
---
 
## 📖 Overview
 
The spread of digital misinformation is one of the most pressing challenges of our time. This project tackles it head-on with a **two-layer verification system** that combines the speed of classical ML with the reasoning power of large language models.
 
| Layer | Technology | Role |
|-------|------------|------|
| 🔢 **Layer 1 — Statistical** | Logistic Regression + TF-IDF | High-speed credibility scoring based on learned text patterns |
| 🧠 **Layer 2 — Reasoning** | Gemini 2.5 Flash API | Context-aware, human-readable explanation of why a story is flagged |
 
---
 
## ✨ Key Features
 
- **🎯 98.72% Accuracy** — Achieved through rigorous training and TF-IDF vectorization on the ISOT Fake News Dataset
- **🌐 Live Web Scraping** — Paste any news URL and verify it directly using integrated `Newspaper3k`
- **🧠 Explainable AI (XAI)** — Moves beyond binary labels; an LLM provides a logical, human-readable fact-checking summary
- **☁️ Cloud Deployment** — Fully responsive dashboard deployed on Streamlit Cloud, accessible from any device
 
---
 
## 🧪 Model Performance
 
The core classification model was trained on the [ISOT Fake News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset).
 
| Metric | Score |
|--------|-------|
| **Accuracy** | 98.72% |
| **Algorithm** | Logistic Regression |
| **Vectorizer** | TF-IDF |
| **Training Environment** | Google Colab |
 
---
 
## 📂 Repository Structure
 
```
fake-news-detector/
│
├── app.py                  # Main Streamlit application
├── fake_news.ipynb         # Data cleaning & model training notebook (Google Colab)
├── model.pkl               # Serialized Logistic Regression model
├── vectorizer.pkl          # Saved TF-IDF vectorizer
├── requirements.txt        # Python dependencies
└── .streamlit/
    └── secrets.toml        # API key configuration (not committed to repo)
```
 
---
 
## ⚙️ Local Setup & Installation
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/Harshal-2006/fake-news-detector-ai.git
cd fake-news-detector
```
 
### 2. Install Dependencies
 
```bash
pip install -r requirements.txt
```
 
### 3. Configure Your API Key
 
Create a `.streamlit/secrets.toml` file in the project root and add your [Google Gemini API Key](https://aistudio.google.com/app/apikey):
 
```toml
GEMINI_API_KEY = "your_api_key_here"
```
 
> ⚠️ **Never commit your `secrets.toml` to version control.** Add it to `.gitignore`.
 
### 4. Run the App
 
```bash
streamlit run app.py
```
 
The app will open automatically at `http://localhost:8501`.
 
---
 
## 🚀 Live Demo
 
Try it now — no installation required:
 
👉 **[fake-news-detector-harshal.streamlit.app](https://fake-news-detector-harshal.streamlit.app/)**
 
---
 
## 🛠️ Tech Stack
 
| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| ML Model | Scikit-learn (Logistic Regression) |
| Text Processing | TF-IDF Vectorizer |
| Generative AI | Google Gemini 2.5 Flash |
| Web Scraping | Newspaper3k |
| Deployment | Streamlit Cloud |
 
---
 
## 📄 License
 
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
 
---
 
<div align="center">
 
Developed with ❤️ by **[Harshal](https://github.com/Harshal-2006)**
 
⭐ If you found this project useful, please consider giving it a star!
 
</div>
