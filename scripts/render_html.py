import os, sys, json, glob

TEMPLATE_HTML = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titre}</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@300;700&family=Source+Sans+Pro:wght@400;600&display=swap');

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Merriweather', Georgia, serif;
    font-size: 12pt;
    line-height: 1.8;
    color: #1a1a1a;
    background: #fafafa;
    max-width: 800px;
    margin: 0 auto;
    padding: 40px 20px;
  }}

  @media print {{
    body {{ background: white; padding: 0; max-width: none; }}
    .page-break {{ page-break-before: always; }}
    @page {{ margin: 2.5cm; }}
  }}

  .page-garde {{
    text-align: center;
    padding: 120px 0 60px 0;
  }}

  .page-garde h1 {{
    font-size: 32pt;
    font-weight: 700;
    letter-spacing: 2px;
    margin-bottom: 8px;
  }}

  .page-garde .sous-titre {{
    font-size: 14pt;
    color: #666;
    font-style: italic;
    margin-bottom: 50px;
  }}

  .page-garde .meta {{
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 11pt;
    color: #888;
    margin-top: 60px;
  }}

  .page-garde .separator {{
    width: 60px;
    height: 1px;
    background: #ccc;
    margin: 40px auto;
  }}

  .toc {{
    font-family: 'Source Sans Pro', sans-serif;
  }}

  .toc h2 {{
    font-size: 18pt;
    margin-bottom: 20px;
    text-transform: uppercase;
    letter-spacing: 3px;
  }}

  .toc ul {{
    list-style: none;
  }}

  .toc li {{
    padding: 6px 0;
    border-bottom: 1px dotted #ddd;
  }}

  .toc a {{
    text-decoration: none;
    color: #1a1a1a;
    display: flex;
    justify-content: space-between;
  }}

  .toc a:hover {{ color: #666; }}

  .chapitre {{
    margin-top: 60px;
  }}

  .chapitre-titre {{
    font-size: 22pt;
    font-weight: 700;
    margin-bottom: 6px;
  }}

  .chapitre-numero {{
    font-size: 10pt;
    text-transform: uppercase;
    letter-spacing: 4px;
    color: #999;
    margin-bottom: 30px;
  }}

  .chapitre p {{
    margin-bottom: 1.2em;
    text-align: justify;
    text-indent: 2em;
  }}

  .chapitre p:first-of-type {{
    text-indent: 0;
  }}

  .chapitre p:first-of-type::first-letter {{
    font-size: 3em;
    font-weight: 700;
    float: left;
    line-height: 1;
    margin-right: 8px;
    margin-top: 4px;
    color: #333;
  }}

  .illustration {{
    text-align: center;
    margin: 40px 0;
  }}

  .illustration img {{
    max-width: 100%;
    height: auto;
    border: 1px solid #eee;
    border-radius: 4px;
  }}

  .illustration figcaption {{
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 9pt;
    color: #999;
    margin-top: 6px;
    font-style: italic;
  }}

  .fin {{
    text-align: center;
    margin: 80px 0;
  }}

  .fin .separator {{
    width: 40px;
    height: 1px;
    background: #ccc;
    margin: 20px auto;
  }}

  .fin p {{
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 10pt;
    color: #888;
    font-style: italic;
  }}
</style>
</head>
<body>

<!-- PAGE DE GARDE -->
<div class="page-garde">
  <h1>{titre}</h1>
  <p class="sous-titre">{sous_titre}</p>
  <div class="separator"></div>
  <p class="meta">Histoire n°{rank}<br>{date}</p>
</div>

<div class="page-break"></div>

<!-- TABLE DES MATIÈRES -->
<div class="toc">
  <h2>Table des Matières</h2>
  <ul>
    {table_matiere}
  </ul>
</div>

<div class="page-break"></div>

<!-- CHAPITRES -->
{chapitres}

<!-- FIN -->
<div class="fin">
  <div class="separator"></div>
  <p>Fin de l'histoire n°{rank}</p>
</div>

</body>
</html>"""

def collecter_chapitres(rank):
    base = os.path.join(os.path.dirname(os.path.dirname(__file__)), f"Histoire{rank}")
    chapters_dir = os.path.join(base, "chapters")
    illu_dir = os.path.join(base, "illustrations")
    state_path = os.path.join(base, "world_state", "state.json")

    if not os.path.isdir(chapters_dir):
        print(f"ERREUR: {chapters_dir} introuvable.")
        sys.exit(1)

    state = {}
    if os.path.exists(state_path):
        state = json.load(open(state_path, encoding="utf-8"))

    titre = state.get("titre", "Sans titre")
    sous_titre = state.get("thematique", "")

    fichiers = sorted(glob.glob(os.path.join(chapters_dir, "*.md")))
    items_toc = []
    corps_chapitres = []
    scene_num = 1

    for i, fpath in enumerate(fichiers, 1):
        with open(fpath, encoding="utf-8") as f:
            content = f.read()

        lines = content.strip().splitlines()
        chap_titre = lines[0].lstrip("# ").strip() if lines else f"Chapitre {i}"
        chap_ref = f"ch{i}"

        items_toc.append(f'<li><a href="#{chap_ref}"><span>{chap_titre}</span></a></li>')

        html_chap = f'<div class="chapitre" id="{chap_ref}">'
        html_chap += f'<p class="chapitre-numero">Chapitre {i}</p>'
        html_chap += f'<h2 class="chapitre-titre">{chap_titre}</h2>'

        # Paragraphes
        body = "\n".join(lines[1:]).strip()
        paras = [p.strip() for p in body.split("\n\n") if p.strip()]
        for p in paras:
            html_chap += f"<p>{p}</p>"

        # Illustration
        illu_path = os.path.join(illu_dir, f"scene_{scene_num:02d}.png")
        if os.path.exists(illu_path):
            rel = os.path.relpath(illu_path, base)
            html_chap += f'<figure class="illustration"><img src="../{rel}" alt="Scene {scene_num}"><figcaption>Scene {scene_num}</figcaption></figure>'
        scene_num += 1

        html_chap += "</div>"
        corps_chapitres.append(html_chap)

    toc_html = "\n".join(items_toc)
    chaps_html = "\n<div class='page-break'></div>\n".join(corps_chapitres)

    from datetime import date
    today = date.today().strftime("%d %B %Y")

    html = TEMPLATE_HTML.format(
        titre=titre,
        sous_titre=sous_titre,
        rank=rank,
        date=today,
        table_matiere=toc_html,
        chapitres=chaps_html,
    )

    return html, titre

def exporter(rank):
    html, titre = collecter_chapitres(rank)
    base = os.path.join(os.path.dirname(os.path.dirname(__file__)), f"Histoire{rank}")
    rendu_dir = os.path.join(base, "rendu")
    os.makedirs(rendu_dir, exist_ok=True)

    filepath = os.path.join(rendu_dir, f"roman_{rank}.html")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Rendu HTML : {filepath}")
    print(f"Ouvre-le dans un navigateur et imprime en PDF pour obtenir le livre.")
    return filepath

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python render_html.py <rank>")
        sys.exit(1)
    exporter(sys.argv[1])
