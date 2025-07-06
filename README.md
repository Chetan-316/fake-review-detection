
ReviewGuard AI is an intelligent tool that uses Machine Learning to detect whether a product review is **Fake** or **Genuine**.

✅ **Features**

* 🌐 **Multilingual Support**: Detects reviews in Hindi/Marathi and translates them to English before analysis.
* 📝 **Single Review Analysis**: Enter a review and get instant predictions.
* 📂 **Batch CSV Upload**: Upload a CSV file of reviews and analyze all at once.
* 📥 Downloadable results as CSV.

---

## 🚀 Live Demo

🌐 [Click Here to Try It](https://reviewguard-ai.streamlit.app)

---

## 📦 Installation

1️⃣ Clone the repository:

```bash
git clone https://github.com/Chetan-316/reviewguard-ai.git
cd reviewguard-ai
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Place your trained ML model files in the `models/` folder:

* `fake_review_model.pkl`
* `tfidf_vectorizer.pkl`

4️⃣ Run locally:

```bash
streamlit run app.py
```

---

## 🌟 Tech Stack

* **Frontend**: Streamlit
* **Backend**: Scikit-learn ML Model
* **Languages**: Python
* **Translation**: Google Translate API
* **Hosting**: Streamlit Cloud

---

## 📂 Example CSV Format

| review                             |
| ---------------------------------- |
| This product is amazing!           |
| बिलकुल अच्छा प्रोडक्ट नहीं है।     |
| Quality is very bad, disappointed. |

---

## 🧑‍💻 Author

👋 **Chetan Santosh Agrawal**
💼 [LinkedIn](https://www.linkedin.com/in/chetan-316/) | 🌐 [Portfolio](https://your-portfolio-link.com)


# fake-review-detection
