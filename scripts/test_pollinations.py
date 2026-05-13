import requests, os

BASE = os.path.dirname(os.path.dirname(__file__))
url = "https://image.pollinations.ai/prompt/test%20image%20corporate%20satire?width=1024&height=1024&model=flux&nologo=true"
r = requests.get(url, timeout=30)
print(f"Status: {r.status_code}")
print(f"Type: {r.headers.get('Content-Type','N/A')}")
print(f"Size: {len(r.content)} bytes")
if r.status_code == 200:
    d = os.path.join(BASE, "Histoire2", "illustrations")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "test_pollinations.png"), "wb") as f:
        f.write(r.content)
    print("TEST OK")
