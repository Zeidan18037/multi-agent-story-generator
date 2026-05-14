import os, sys, glob
from playwright.sync_api import sync_playwright

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rank = sys.argv[1] if len(sys.argv) > 1 else "2"
html_path = os.path.join(BASE, f"Histoire{rank}", "rendu", f"roman_{rank}.html")
pdf_path = os.path.join(BASE, f"Histoire{rank}", "rendu", f"roman_{rank}.pdf")

if not os.path.exists(html_path):
    print(f"ERREUR: {html_path} introuvable")
    sys.exit(1)

# detecter automatiquement le chromium playwright
pw_browsers = os.path.expanduser("~\\AppData\\Local\\ms-playwright")
chromium_dirs = glob.glob(os.path.join(pw_browsers, "chromium-*"))
chromium_path = None
for d in sorted(chromium_dirs, reverse=True):
    candidate = os.path.join(d, "chrome-win64", "chrome.exe")
    if os.path.exists(candidate):
        chromium_path = candidate
        break

with sync_playwright() as p:
    if chromium_path:
        browser = p.chromium.launch(executable_path=chromium_path, headless=True)
    else:
        browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(f"file:///{html_path.replace(os.sep, '/')}", wait_until="networkidle")
    page.pdf(path=pdf_path, format="A4", print_background=True,
             margin={"top": "20mm", "bottom": "20mm", "left": "15mm", "right": "15mm"})
    browser.close()

print(f"PDF genere: {pdf_path}")
