import sys
sys.path.insert(0, "C:\\Users\\medze\\roman\\scripts")
from init_vector_store import init_collections, index_chapter
init_collections(rank=3)
c = open("C:\\Users\\medze\\roman\\Histoire3\\chapters\\chapitre_02_audit.md", encoding="utf-8").read()
index_chapter("h3ch02", "Audit", c, {
    "personnages": '["Antoine Lambert","Vito Bianchi","Don Carlo Moretti","Giuseppe","Marco"]',
    "lieu": "Hangar 7 port de Marseille",
    "intrigue": "Antoine audite les activites et presente un plan strategique au Don",
    "ton": "sarcastique"
}, rank=3)
print("H3 Ch2 indexe OK")
