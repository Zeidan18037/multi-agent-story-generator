import json, os
BASE = os.path.dirname(os.path.dirname(__file__))
B = os.path.join(BASE, "Histoire2")
ws = json.load(open(os.path.join(B,"world_state/state.json"),encoding="utf-8"))
ws["intrigue"]["acte"] = 1
ws["intrigue"]["chapitre_courant"] = 1
ws["intrigue"]["evenements_cles"] = [
    "Kessler annonce la transformation AI-first",
    "Marc Delambre vend ARIA a DataFusion",
    "Claire licenciee pour avoir pose les bonnes questions",
    "Premier rapport ARIA : 47 pages d'hallucinations applaudies par Kessler",
    "Claire re-embauchee comme AI-Human Integration Lead a 70% du salaire"
]
ws["timeline"] = [
    "Ch.1 — L'Annonce : 53 employes licencies, ARIA deployee, Claire re-embauchee le soir meme"
]
json.dump(ws, open(os.path.join(B,"world_state/state.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
print("World state mis a jour.")
