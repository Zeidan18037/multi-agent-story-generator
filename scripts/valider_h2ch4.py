import sys
import os
BASE = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE, "scripts"))
from init_vector_store import init_collections, index_chapter
init_collections(rank=2)
c = open(os.path.join(BASE, "Histoire2", "chapters", "chapitre_04_normalisation.md"), encoding="utf-8").read()
index_chapter("h2ch04", "Normalisation", c, {
    "personnages": '["Claire Delorme", "Thomas Kessler", "Marc Delambre", "Stephane"]',
    "lieu": "DataFusion",
    "intrigue": "ARIA tourne encore, titres changes, salaries baisses, Marc Delambre facture 15K/mois pour rien",
    "ton": "sarcastique"
}, rank=2)
print("H2 Ch4 indexe OK")
