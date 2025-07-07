# 🔍 Intelligent Complaint Analysis for Financial Services

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot system to help internal teams at CrediTrust Financial analyze and respond to customer complaints more effectively.

It combines vector-based semantic search with language models to answer questions grounded in real customer feedback.

---

## 🎯 Objective

Transform unstructured complaint narratives into an intelligent assistant that helps product managers, compliance officers, and support teams query and analyze customer pain points across five product categories:

- Credit Cards  
- Personal Loans  
- Buy Now Pay Later (BNPL)  
- Savings Accounts  
- Money Transfers

---

## 🧱 Project Structure

.
├── data/ # Raw and filtered complaint data
├── notebooks/ # Exploratory and development notebooks
├── report/ # Interim and final reports
├── src/ # Source code
│ ├── utils/ # Modular utility classes
├── vector_store/ # Serialized vector index & metadata
└── README.md # Project overview (this file)

---

## ✅ Task Coverage

### Task 1: EDA and Preprocessing

- Loaded and analyzed the CFPB complaint dataset
- Filtered relevant product categories
- Cleaned and saved data to `data/filtered_complaints.csv`

### Task 2: Chunking, Embedding & Indexing

- Used LangChain’s `RecursiveCharacterTextSplitter` for chunking  
- Embedded text using `all-MiniLM-L6-v2` from Sentence Transformers  
- Stored embeddings in FAISS index  
- Saved index + metadata to `vector_store/`

### Task 3+: (Upcoming)

- Implementing a retriever system and LLM-based question answering
- Creating an interactive chatbot with Streamlit/Gradio

---

## 💡 Technologies Used

- `langchain` for text chunking
- `sentence-transformers` for semantic embedding
- `faiss-cpu` for vector similarity search
- `pandas`, `tqdm`, `pickle` for processing and saving
- `streamlit` or `gradio` for UI (in Task 4)

---

## 📁 Key Files

### 🔹 `src/`
- `embedding_pipeline.py` – Main runner for Task 2
- `config.py` – Centralized chunking/embedding settings
- `utils/text_embedder.py` – Class for chunking and embedding
- `utils/vector_indexer.py` – Class for storing embeddings and metadata in FAISS

### 🔹 `vector_store/`
- `faiss_index.index` – Saved FAISS vector store
- `metadata.pkl` – Metadata for each embedded chunk

### 🔹 `report/`
- `interim_report.md` – Strategy and findings for Tasks 1 & 2
- `final_report.md` – To be completed for Tasks 3 & 4

---

## 🚀 How to Run Task 2

```bash
# Inside your conda or pip environment:
python src/embedding_pipeline.py