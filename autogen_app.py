# autogen_app.py
import json
from agents.niche_scout import run_niche_scout
from agents.seo_writer import run_seo_writer

# Load niche topics
with open("config/niche_config.json") as f:
    niches = json.load(f)

for topic in niches["topics"]:
    print(f"🔍 Exploring topic: {topic}")
    findings = run_niche_scout(topic)
    post = run_seo_writer(findings)
    
    filename = f"{topic.replace(' ', '_').lower()}.md"
    with open(filename, "w", encoding="utf-8") as out:
        out.write(post)
    print(f"✅ Saved: {filename}")
