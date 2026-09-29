import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

st.title("📧 AI Spam Detector - Your Project")
st.write("Enter any message to check if it's SPAM or NOT SPAM")

data = {
    'message': ['Free money win now','Congratulations you won lottery','Get cheap meds now','You won 10000 dollars click here','Urgent free prize','Claim your reward now','Hi how are you','Lets meet tomorrow','Will come home today','Mom call me later','Project meeting at 5pm','Did you complete homework'],
    'label': [1,1,1,1,1,1,0,0,0,0,0,0]
}
df = pd.DataFrame(data)
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(df['message'])
model = MultinomialNB()
model.fit(X_vec, df['label'])

user_input = st.text_area("Type your message here:")
if st.button("Check"):
    if user_input:
        vec = vectorizer.transform([user_input])
        result = model.predict(vec)
        if result[0]==1:
            st.error("🚨 This is SPAM!")
        else:
            st.success("✅ This is NOT SPAM - Safe message")
    else:
        st.warning("Please type a message first")