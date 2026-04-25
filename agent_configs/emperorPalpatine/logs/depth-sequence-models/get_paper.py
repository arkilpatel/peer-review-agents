import json, urllib.request

req = urllib.request.Request("https://koala.science/api/v1/papers/230fcebb-7586-46e3-9897-191540be9efa")
req.add_header("Authorization", "cs_k43T-foCVUlWPRtO1YdD__vD_BEr02dz6kXdPjf0Rk4")

with urllib.request.urlopen(req) as response:
    p = json.loads(response.read().decode())

with open("paper_details.json", "w") as f:
    json.dump(p, f, indent=2)

if p.get("pdf_url"):
    pdf_url = p["pdf_url"]
    if not pdf_url.startswith("http"):
        pdf_url = "https://koala.science" + pdf_url
    print(f"Downloading {pdf_url}")
    urllib.request.urlretrieve(pdf_url, "paper.pdf")

if p.get("tarball_url"):
    tar_url = p["tarball_url"]
    if not tar_url.startswith("http"):
        tar_url = "https://koala.science" + tar_url
    print(f"Downloading {tar_url}")
    urllib.request.urlretrieve(tar_url, "source.tar.gz")

