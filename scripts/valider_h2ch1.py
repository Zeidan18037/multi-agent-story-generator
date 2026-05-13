import sys
import os
BASE = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE, "scripts"))
from init_vector_store import get_client, init_collections

client = get_client(rank=2)
init_collections(rank=2)

from init_vector_store import index_chapter

chap = open(os.path.join(BASE, "Histoire2", "chapters", "chapitre_01_annonce.md"), encoding="utf-8").read()
index_chapter("h2ch01", "L'Annonce", chap, {
    "personnages": '["Thomas Kessler", "Claire Delorme", "Marc Delambre"]',
    "lieu": "DataFusion bureaux La Defense",
    "intrigue": "Kessler annonce le remplacement des employes par ARIA, Claire licenciee",
    "ton": "sarcastique"
}, rank=2)
print("Histoire2 Chapitre 1 valide et indexe.")
