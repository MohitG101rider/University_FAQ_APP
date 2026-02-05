import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="University FAQ Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------------- STYLING ----------------
st.markdown("""
<style>
body {
    background-color: #f4f6fb;
}
.title {
    font-size: 40px;
    font-weight: 700;
    color: #3f51b5;
}
.subtitle {
    font-size: 18px;
    color: #555;
}
.box {
    background: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0px 8px 24px rgba(0,0,0,0.1);
    margin-top: 20px;
}
.answer {
    font-size: 18px;
    color: #222;
}
.sidebar {
    background-color: #eef1ff;
    padding: 15px;
    border-radius: 10px;
}
.footer {
    text-align: center;
    margin-top: 50px;
    color: #888;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='title'>🎓 University FAQ Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Offline, Dataset-Driven Intelligent FAQ System</div>", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
data = pd.read_csv("university_faq.csv")

questions = data["question"].tolist()
answers = data["answer"].tolist()

# ---------------- VECTOR MODEL ----------------
vectorizer = TfidfVectorizer(stop_words="english")
question_vectors = vectorizer.fit_transform(questions)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("### 📌 Project Info")
    st.markdown("""
    - No API used  
    - Trained using CSV dataset  
    - TF-IDF + Cosine Similarity  
    - Streamlit Interface  
    """)
    st.markdown("### 📊 Dataset Size")
    st.write(f"Total FAQs: {len(questions)}")

# ---------------- MAIN UI ----------------
col1, col2 = st.columns([3, 1])

with col1:
    user_question = st.text_input("Ask a university-related question")

with col2:
    st.write("")
    ask_btn = st.button("🔍 Find Answer")

# ---------------- PROCESS ----------------
if ask_btn:
    if user_question.strip() == "":
        st.warning("Please type a question.")
    else:
        user_vector = vectorizer.transform([user_question])
        similarity_scores = cosine_similarity(user_vector, question_vectors)
        best_index = similarity_scores.argmax()
        best_score = similarity_scores[0][best_index]

        if best_score > 0.30:
            st.markdown(f"""
            <div class="box">
                <h3>Answer</h3>
                <div class="answer">{answers[best_index]}</div>
                <br>
                <small>Confidence Score: {round(best_score, 2)}</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("No suitable answer found. Try rephrasing.")

# ---------------- FOOTER ----------------
st.markdown("<div class='footer'>University FAQ Assistant • Dataset Based • No API</div>", unsafe_allow_html=True)