import streamlit as st

st.title("💬 Intelligent Complaint Analyzer")
st.subheader("Task 4: Evaluation & Feedback")

user_input = st.text_input("Enter a customer complaint:")
if st.button("Analyze"):
    # Simulate response
    st.write("✅ Retrieved response:")
    st.success("We are sorry to hear this. Your refund has been processed.")

st.markdown("---")
st.caption("RAG-powered chatbot by rufaeleshetu")
