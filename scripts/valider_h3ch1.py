import sys
sys.path.insert(0, "C:\\Users\\medze\\roman\\scripts")
from init_vector_store import init_collections, index_chapter
init_collections(rank=3)
c = open("C:\\Users\\medze\\roman\\Histoire3\\chapters\\chapitre_01_recrutement.md", encoding="utf-8").read()
index_chapter("h3ch01", "Recrutement", c, {
    "personnages": '["Antoine Lambert","Vito Bianchi","Don Carlo Moretti"]',
    "lieu": "Bar Marseille + hangar 7",
    "intrigue": "Actuaire licencie recrute par la mafia",
    "ton": "sarcastique"
}, rank=3)
print("H3 Ch1 indexe OK")
