import sys
import os
BASE = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE, "scripts"))
from init_vector_store import init_collections, index_chapter

init_collections(rank=2)
chap = open(os.path.join(BASE, "Histoire2", "chapters", "chapitre_02_essaim_cognitif.md"), encoding="utf-8").read()
index_chapter("h2ch02", "L'Essaim Cognitif", chap, {
    "personnages": '["Claire Delorme", "Thomas Kessler", "Stephane"]',
    "lieu": "DataFusion bureaux La Defense",
    "intrigue": "ARIA hallucine a grande echelle : 47 tickets bidon, rendez-vous chez concurrent",
    "ton": "sarcastique"
}, rank=2)
print("H2 Ch2 valide et indexe.")
