import spacy
import re
import sys
from collections import Counter

try:
    nlp = spacy.load("fr_core_news_sm")
except OSError:
    print("Modele fr_core_news_sm non trouve. Lance : python -m spacy download fr_core_news_sm")
    sys.exit(1)

LEXIQUE_SARCLASME = [
    "bien sur", "evidemment", "visiblement", "apparemment", "soi-disant",
    "pretendument", "miraculeusement", "inevitablement", "naturellement",
    "helas", "bravo", "felicitations", "genial", "super", "formidable",
    "remarquable", "exceptionnel", "innovant", "disruptif", "agile",
    "synergie", "optimisation", "scalable", "growth", "mindset",
]

MARQUEURS_IRONIE = [
    r"c'est\s+sans\s+doute", r"comme\s+par\s+hasard",
    r"quelle\s+surprise", r"on\s+se\s+demande",
    r"qui\s+l'eut\s+cru", r"rien\s+de\s+tel",
    r"n'est-ce\s+pas", r"si\s+on\s+peut\s+dire",
]

def analyser_ton(texte):
    doc = nlp(texte)
    mots = [token.text.lower() for token in doc if not token.is_punct and not token.is_space]
    phrases = [sent.text for sent in doc.sents]

    score_sarcasme = 0
    occurrences_sarcasme = []

    for mot in LEXIQUE_SARCLASME:
        count = texte.lower().count(mot)
        if count > 0:
            score_sarcasme += count
            occurrences_sarcasme.append({"mot": mot, "count": count})

    for pattern in MARQUEURS_IRONIE:
        matches = re.findall(pattern, texte.lower())
        if matches:
            score_sarcasme += len(matches) * 2
            occurrences_sarcasme.append({"mot": pattern, "count": len(matches)})

    freq_mots = Counter(mots)
    repetitions = {mot: count for mot, count in freq_mots.items()
                   if count > 5 and len(mot) > 3}

    mots_uniques = len(set(mots))
    total_mots = len(mots)
    diversite = round(mots_uniques / total_mots * 100, 1) if total_mots > 0 else 0

    rapport = {
        "score_sarcasme": score_sarcasme,
        "occurrences": occurrences_sarcasme,
        "total_mots": total_mots,
        "mots_uniques": mots_uniques,
        "diversite_lexicale_pct": diversite,
        "nb_phrases": len(phrases),
        "repetitions_lourdes": repetitions,
        "ton_suffisant": score_sarcasme >= 5,
        "alerte_neutre": score_sarcasme < 5,
    }

    return rapport

def afficher_rapport(rapport):
    print("=" * 50)
    print("RAPPORT D'ANALYSE DE TON")
    print("=" * 50)
    print(f"Score de sarcasme : {rapport['score_sarcasme']}")
    print(f"Diversite lexicale : {rapport['diversite_lexicale_pct']}%")
    print(f"Nombre de mots : {rapport['total_mots']}")
    print(f"Ton suffisant : {'OUI' if rapport['ton_suffisant'] else 'NON'}")
    if rapport['alerte_neutre']:
        print("\nALERTE : Ton trop neutre - recriture necessaire.")
    if rapport['repetitions_lourdes']:
        print("\nRepetitions detectees :")
        for mot, count in sorted(rapport['repetitions_lourdes'].items(),
                                  key=lambda x: -x[1])[:10]:
            print(f"  - '{mot}' : {count}x")
    print("=" * 50)

if __name__ == "__main__":
    texte = sys.stdin.read()
    rapport = analyser_ton(texte)
    afficher_rapport(rapport)
    sys.exit(0 if rapport["ton_suffisant"] else 1)
