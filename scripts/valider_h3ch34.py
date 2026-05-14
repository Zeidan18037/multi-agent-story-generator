import sys
sys.path.insert(0, "C:\\Users\\medze\\roman\\scripts")
from init_vector_store import init_collections, index_chapter
init_collections(rank=3)
for n,title,filename in [
    ("h3ch03","FBI et KPI","chapitre_03_fbi.md"),
    ("h3ch04","Decision","chapitre_04_decision.md"),
]:
    c = open(f"C:\\Users\\medze\\roman\\Histoire3\\chapters\\{filename}", encoding="utf-8").read()
    index_chapter(n, title, c, {"personnages":'["Antoine Lambert","Vito Bianchi","Agent Park"]',"lieu":"Marseille","intrigue":f"Chapitre {n[-2:]}: {title}","ton":"sarcastique"}, rank=3)
print("H3 Ch3+4 indexes OK")
