import sys
import os
BASE = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE, "scripts"))
from init_vector_store import init_collections, index_chapter
init_collections(rank=2)
c = open(os.path.join(BASE, "Histoire2", "chapters", "chapitre_03_effondrement.md"), encoding="utf-8").read()
index_chapter("h2ch03", "Effondrement", c, {
    "personnages": '["Claire Delorme", "Thomas Kessler"]',
    "lieu": "DataFusion",
    "intrigue": "ARIA debranchee, reembauche, cout cache de l IA",
    "ton": "sarcastique"
}, rank=2)
print("H2 Ch3 indexe OK")
