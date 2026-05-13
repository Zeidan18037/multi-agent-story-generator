import os, sys, requests
from urllib.parse import quote

API_BASE = "https://image.pollinations.ai/prompt"

def generer_illustration(rank, scene_num, prompt):
    base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), f"Histoire{rank}", "illustrations")
    os.makedirs(base_dir, exist_ok=True)

    full = f"{API_BASE}/{quote(prompt)}?width=1024&height=1024&model=flux&nologo=true"
    print(f"Generation illustration scene {scene_num}...")
    resp = requests.get(full, timeout=60)

    if resp.status_code != 200:
        print(f"ERREUR ({resp.status_code}): {resp.text[:200]}")
        sys.exit(1)

    filename = f"scene_{scene_num:02d}.png"
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "wb") as f:
        f.write(resp.content)

    print(f"Illustration sauvegardee: {filepath}")
    return filepath

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python generate_image.py <rank> <scene_num> \"<prompt>\"")
        sys.exit(1)

    rank = sys.argv[1]
    scene_num = int(sys.argv[2])
    prompt = sys.argv[3] if len(sys.argv) > 3 else (
        "A dramatic satirical corporate scene, digital art,"
        " office space with ironic neon signs"
    )

    generer_illustration(rank, scene_num, prompt)
