"""Persistent semantic evidence index. Only use fictional/demo resumes."""
import hashlib
import os
from pathlib import Path
from functools import lru_cache

@lru_cache(maxsize=1)
def _encoder():
    from sentence_transformers import SentenceTransformer
    return SentenceTransformer("all-MiniLM-L6-v2")

def _collection():
    import chromadb
    path = os.getenv("CHROMA_PATH", ".chroma")
    Path(path).mkdir(parents=True, exist_ok=True)
    return chromadb.PersistentClient(path=path).get_or_create_collection("hireflow_evidence_v2")

def chunks(text: str, size: int = 650, overlap: int = 100) -> list[str]:
    text = " ".join(text.split())
    if not text:
        return []
    result = []
    step = size - overlap
    for start in range(0, len(text), step):
        result.append(text[start:start + size])
        if start + size >= len(text):
            break
    return result

def index_document(doc_id: str, text: str) -> int:
    pieces = chunks(text)
    if not pieces:
        return 0
    collection = _collection()
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]
    ids = [f"{doc_id}:{digest}:{i}" for i in range(len(pieces))]
    vectors = _encoder().encode(pieces).tolist()
    # Replace old versions of this document; avoids stale evidence.
    old = collection.get(where={"doc_id": doc_id})
    if old["ids"]:
        collection.delete(ids=old["ids"])
    collection.upsert(ids=ids, documents=pieces, embeddings=vectors,
                      metadatas=[{"doc_id": doc_id, "chunk": i, "version": digest}
                                 for i in range(len(pieces))])
    return len(pieces)

def search_document(doc_id: str, query: str, top_k: int = 3) -> list[dict]:
    collection = _collection()
    entries = collection.get(where={"doc_id": doc_id})
    if not entries["ids"]:
        return []
    vector = _encoder().encode([query]).tolist()
    result = collection.query(query_embeddings=vector,
                              where={"doc_id": doc_id},
                              n_results=min(top_k, len(entries["ids"])),
                              include=["documents", "metadatas", "distances"])
    return [{"text": t, "source": m["doc_id"], "chunk": m["chunk"], "distance": d}
            for t, m, d in zip(result["documents"][0], result["metadatas"][0], result["distances"][0])]
