import chromadb
import os
import json
from datetime import datetime

def get_client(rank=1):
    base = os.path.dirname(os.path.dirname(__file__))
    persist = os.path.join(base, f"Histoire{rank}", "chroma_data")
    os.makedirs(persist, exist_ok=True)
    return chromadb.PersistentClient(path=persist)

def init_collections(rank=1):
    client = get_client(rank)
    collection = client.get_or_create_collection(
        name="chapitres",
        metadata={"description": f"Histoire{rank} - Index vectoriel des chapitres valides"}
    )
    print(f"Collection 'chapitres' prete. Count: {collection.count()}")
    return collection

def index_chapter(chapter_id, title, content, metadata=None, rank=1):
    client = get_client(rank)
    collection = client.get_collection("chapitres")
    default_metadata = {
        "date_index": datetime.now().isoformat(),
        "personnages": "[]",
        "lieu": "",
        "intrigue": "",
        "ton": "",
    }
    if metadata:
        default_metadata.update(metadata)
    collection.upsert(
        ids=[chapter_id],
        documents=[content],
        metadatas=[default_metadata]
    )
    print(f"Chapitre indexe : {chapter_id} — {title}")

def search_chapters(query, n_results=3, filter_dict=None, rank=1):
    client = get_client(rank)
    collection = client.get_collection("chapitres")
    return collection.query(query_texts=[query], n_results=n_results, where=filter_dict)

if __name__ == "__main__":
    import sys
    r = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    init_collections(r)
    print(f"Base vectorielle Histoire{r} initialisee.")
