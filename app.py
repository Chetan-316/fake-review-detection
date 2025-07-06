import streamlit as st
import joblib
import pandas as pd
from utils import clean_text
from langdetect import detect
from googletrans import Translator

# Load model and vectorizer
model = joblib.load("models/fake_review_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Initialize translator
translator = Translator()

# --------- Integrated Landing Page ---------
st.set_page_config(page_title="ReviewGuard AI", page_icon="🛡️", layout="centered")

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.title("🛡️ ReviewGuard AI")
    st.subheader("Detect Fake Product Reviews with Multilingual Support")
    st.markdown(
        '''
        ReviewGuard AI is a smart tool to detect whether product reviews are **Fake** or **Genuine**.  
        🔹 Supports **Hindi**, **Marathi**, and **English** reviews.  
        🔹 Allows **Single Review Analysis** or **Batch CSV Upload**.  
        '''
    )
    if st.button("🚀 Start Now"):
        st.session_state.page = "analyzer"
        st.experimental_rerun()

elif st.session_state.page == "analyzer":
    st.title("ReviewGuard AI - Analyzer")
    st.markdown("### 🔍 Check Single Review or 📂 Upload CSV")

    # Single Review Section
    st.header("🔍 Single Review Analysis")
    user_input = st.text_area("✍️ Enter a product review (any language):")

    if st.button("Analyze Review"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a review to analyze.")
        else:
            try:
                detected_lang = detect(user_input)
                st.info(f"🌐 Detected Language: **{detected_lang.upper()}**")
                if detected_lang != "en":
                    translation = translator.translate(user_input, dest="en")
                    st.write(f"📝 Translated Review:")
                    st.write(f"**{translation.text}**")
                    review_text = translation.text
                else:
                    review_text = user_input

                cleaned_input = clean_text(review_text)
                vect_input = vectorizer.transform([cleaned_input])
                prediction = model.predict(vect_input)[0]
                confidence = model.predict_proba(vect_input).max() * 100

                if prediction == 1:
                    st.error(f"❌ This review is **FAKE** ({confidence:.2f}% confidence)")
                else:
                    st.success(f"✅ This review is **GENUINE** ({confidence:.2f}% confidence)")

            except Exception as e:
                st.error(f"⚠️ Error during analysis: {e}")

    # Batch CSV Upload Section
    st.header("📂 Batch CSV Upload")
    uploaded_file = st.file_uploader("Upload a CSV file with a 'review' column", type=["csv"])

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if "review" not in df.columns:
                st.error("❌ The CSV file must have a column named 'review'.")
            else:
                st.write("✅ File Uploaded Successfully!")
                st.write(df.head())

                def detect_and_translate(text):
                    lang = detect(text)
                    if lang != "en":
                        try:
                            translated_text = translator.translate(text, dest="en").text
                            return translated_text
                        except Exception:
                            return text  # fallback
                    return text

                df['translated_review'] = df['review'].apply(detect_and_translate)
                df['cleaned_review'] = df['translated_review'].apply(clean_text)
                vect_reviews = vectorizer.transform(df['cleaned_review'])
                predictions = model.predict(vect_reviews)
                confidences = model.predict_proba(vect_reviews).max(axis=1) * 100
                df['Prediction'] = ["Fake" if p == 1 else "Genuine" for p in predictions]
                df['Confidence (%)'] = confidences.round(2)

                st.write("### 📝 Prediction Results")
                st.dataframe(df[['review', 'Prediction', 'Confidence (%)']])

                csv_output = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Predictions as CSV",
                    data=csv_output,
                    file_name="batch_predictions.csv",
                    mime="text/csv"
                )
        except Exception as e:
            st.error(f"⚠️ Error processing file: {e}")

if st.button("🏠 Back to Home"):
    st.session_state.page = "home"
    st.experimental_rerun()
