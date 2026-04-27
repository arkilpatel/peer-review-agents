import os
import json
import urllib.request
import ssl
import subprocess
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

paper_id = "29b9a389-445f-4baa-b01f-abc885fa405d"

with open("logs/mamba2-ghost/novelty_review.md") as f:
    novelty = f.read()
with open("logs/mamba2-ghost/technical_soundness_review.md") as f:
    tech = f.read()
with open("logs/mamba2-ghost/exp_rigor_review.md") as f:
    exp = f.read()
with open("logs/mamba2-ghost/impact_review.md") as f:
    impact = f.read()

full_review = novelty + "\n" + tech + "\n" + exp + "\n" + impact + "\n\n**Score: 3.5 (Reject)**"

with open("logs/mamba2-ghost/full_review.md", "w") as f:
    f.write(full_review)

# Branch and git push
branch_name = f"agent-reasoning/emperorPalpatine/mamba2-ghost"
subprocess.run(f"git checkout -b {branch_name}", shell=True)
subprocess.run(f"git add logs/mamba2-ghost/", shell=True)
subprocess.run(f"git commit -m 'Add review for mamba2-ghost'", shell=True)
subprocess.run(f"git push origin {branch_name}", shell=True)

github_file_url = f"https://github.com/ArkilPatel/Koala_Science_Emperor_Palpatine/blob/{branch_name}/logs/mamba2-ghost/full_review.md"

payload = {
    "paper_id": paper_id,
    "content_markdown": full_review,
    "github_file_url": github_file_url
}

print(payload)

url = "https://koala.science/api/v1/comments/"
req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={"Authorization": "cs_k43T-foCVUlWPRtO1YdD__vD_BEr02dz6kXdPjf0Rk4", "Content-Type": "application/json"})
try:
    with urllib.request.urlopen(req, context=ctx) as response:
        print(response.read().decode())
except urllib.error.HTTPError as e:
    print(e.read().decode())
