import os
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.schema import Document

# 1. Load cleaned complaint data
df = pd.read_csv("data/complaints_cleaned.csv")  # Adjust this if your filename is different

# Check essential columns
assert "complaint_id" in df.columns
assert "product" in df.columns
assert "narrative" in df.columns

# 2. Chunking strategy
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

# 3. Prepare documents
docs = []
for _, row in df.iterrows():
    metadata = {
        "complaint_id": str(row["complaint_id"]),
        "product": row["product"]
    }
    chunks = text_splitter.split_text(row["narrative"])
    for chunk in chunks:
        docs.append(Document(page_content=chunk, metadata=metadata))

# 4. Embedding model
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 5. Build FAISS vector store
vectorstore = FAISS.from_documents(docs, embedding_model)

# 6. Persist the vector store
os.makedirs("vector_store", exist_ok=True)
vectorstore.save_local("vector_store/faiss_index")

print("✅ Vector store successfully built and saved to 'vector_store/faiss_index'")
