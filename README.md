Here’s a **simple and clean README.md** for your GitHub project 👇

---

### 📄 **README.md**

````markdown
# 🛡️ ReviewGuard AI

ReviewGuard AI is a smart web application that detects whether product reviews are **Fake** or **Genuine**. Built with Machine Learning and Natural Language Processing (NLP), it supports multilingual reviews including Hindi, Marathi, and English.  

## 🚀 Features
- 🌐 **Language Detection & Translation**: Automatically detects Hindi/Marathi reviews and translates them to English before analysis.  
- ✍️ **Single Review Analysis**: Check if an individual review is fake or genuine.  
- 📂 **Batch CSV Upload**: Upload a CSV file of reviews and get predictions for all at once.  
- 📥 **Downloadable Results**: Export analyzed results as a CSV file.  

## 🛠️ Technologies Used
- Python
- Streamlit (Frontend)
- Scikit-learn (ML Model)
- TF-IDF Vectorization
- Google Translate API
- Langdetect for language detection

## 📦 How to Run
1. Clone this repository:  
   ```bash
   git clone https://github.com/Chetan-316/reviewguard-ai.git
   cd reviewguard-ai
````

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## 📂 Project Structure

```
reviewguard-ai/
│
├── app.py                # Streamlit app
├── utils.py              # Helper functions
├── requirements.txt      # Project dependencies
├── models/               # Trained ML model and vectorizer
│   ├── fake_review_model.pkl
│   ├── tfidf_vectorizer.pkl
└── README.md             # Project description
```

## 👨‍💻 Author

Chetan Santosh Agrawal


