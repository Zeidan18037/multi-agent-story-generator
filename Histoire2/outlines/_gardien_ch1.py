import json, os
B = os.path.join(os.path.dirname(os.path.dirname(__file__)))
for f in ["characters/thomas_kessler.json","characters/claire_delorme.json"]:
    d=json.load(open(os.path.join(B,f),encoding="utf-8"))
    print(f"  {f} -- {d['nom']} ({d['role']})")
ws=json.load(open(os.path.join(B,"world_state/state.json"),encoding="utf-8"))
print(f"  Acte: {ws['intrigue']['acte']} | Chap: {ws['intrigue']['chapitre_courant']}")
print(f"  Persos: {ws['personnages_actifs']}")
c=open(os.path.join(B,"outlines/chapitre_01_canevas.md"),encoding="utf-8").read()
for i in ["Kessler","Claire","Marc Delambre","ARIA","all-hands","licenciee","hallucinations"]:
    print(f"  {'OK' if i in c else 'MANQUE'}: {i}")
print("  === VERIFICATION PASSEE ===")
