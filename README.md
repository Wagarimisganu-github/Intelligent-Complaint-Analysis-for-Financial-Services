# 💡 Intelligent Complaint Analysis for Financial Services

This project implements an end-to-end system for analyzing customer complaints in the financial services sector using advanced Natural Language Processing (NLP) techniques. It leverages **LLMs**, **semantic search**, **RAG (Retrieval-Augmented Generation)**, and an interactive **Streamlit interface** for deployment.

## 🚀 Project Structure

📦 Root
├── data/ # Contains raw and cleaned complaint data
├── src/ # Core logic: retrieval, generation, UI components
│ ├── retriever.py
│ ├── rag_pipeline.py
│ └── ...
├── evaluation/ # Evaluation scripts
│ └── evaluate.py
├── streamlit_app.py # Streamlit chatbot UI
├── requirements.txt
└── README.md # Project documentation

---

## ✅ Task 1: Data Cleaning and Complaint Categorization

### 🎯 Objective:
Clean raw complaint data and categorize them into logical complaint types such as:
- Refund issues
- Delays in service
- Fraud/Unauthorized transactions
- Account-related problems

### ⚙️ Key Steps:
- Removed duplicates and null values
- Normalized text: lowercase, punctuation removal
- Used basic rule-based logic for categorization

### 📦 Output:
Cleaned data stored in:
data/cleaned_complaints.csv


## ✅ Task 2: Vector Store and Retriever Pipeline

### 🎯 Objective:
Convert complaints into vector format and set up a retriever pipeline.

### ⚙️ Key Steps:
- Used `LangChain`'s `RecursiveCharacterTextSplitter` to chunk long complaint narratives
- Embedded text chunks using `OpenAIEmbeddings`
- Stored embeddings in a `FAISS` vector store

### 📦 Output:
- Vector index in `data/vector_store/`
- Retriever code in `src/retriever.py`

---

## ✅ Task 3: RAG Pipeline (Retriever + Generator)

### 🎯 Objective:
Combine retrieval and generation to produce accurate, context-aware answers to user queries.

### ⚙️ Key Steps:
- Retrieved relevant complaint chunks from FAISS
- Constructed context-aware prompts
- Used `ChatOpenAI` to generate helpful responses

### 📦 Output:
Full RAG pipeline implemented in:
src/rag_pipeline.py

## ✅ Task 4: Evaluation and Streamlit UI Deployment

### 🎯 Objective:
Evaluate how well the system performs and make it usable through an interactive web interface.

### ⚙️ Key Steps:
#### 🧪 Evaluation:
- Compared generated answers to reference answers using cosine similarity on embeddings
- Added scoring logic and visualizations

#### 💻 Streamlit UI:
- Built a front-end chatbot using `streamlit`
- Accepts user queries and displays generated answers in real time

### 📦 Output:
- Evaluation script: `evaluation/evaluate.py`
- UI: `streamlit_app.py`

---

## 🧪 How to Evaluate the Model

Run this command in your Colab or local terminal:

python evaluation/evaluate.py
🚀 How to Launch the Streamlit App
To launch the chatbot UI:

streamlit run streamlit_app.py
If you're using Colab, run:

!streamlit run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false
Then click the public URL that appears in the output.

✨ Features
Real-time LLM-based answers

RAG (Retrieval-Augmented Generation)

Cosine similarity evaluation

Interactive Streamlit chatbot UI

🔧 Requirements
Install dependencies with:

pip install -r requirements.txt

