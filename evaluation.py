from sklearn.metrics.pairwise import cosine_similarity

def evaluate_rag(preds, truths, embeddings_fn):
    pred_emb = embeddings_fn(preds)
    truth_emb = embeddings_fn(truths)
    cosine_sim = cosine_similarity(pred_emb, truth_emb).diagonal().mean()
    return {
        "cosine_similarity": round(cosine_sim, 4)
    }
