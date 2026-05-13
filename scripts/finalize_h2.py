import json, os

BASE = os.path.dirname(os.path.dirname(__file__))
B = os.path.join(BASE, "Histoire2")
ws = json.load(open(os.path.join(B,"world_state/state.json"), encoding="utf-8"))
ws["rendu"]["illustrations"] = True
ws["rendu"]["html_genere"] = True
ws["rendu"]["date_dernier_rendu"] = "2026-05-13"
ws["intrigue"]["evenements_cles"].extend([
    "Kessler realise qu'ARIA coute plus cher que les humains",
    "ARIA debranchee, equipes re-embauchees a salaire reduit",
    "Marc Delambre facture 15K/mois pour un serveur qui tourne dans le vide"
])
json.dump(ws, open(os.path.join(B,"world_state/state.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print("Histoire2 finalisee.")
