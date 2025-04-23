# autogen-dp-solar-loop
Autogen
/autogen-dp-solar-loop
│
├── config/
│   ├── niche_config.json        ← Seed topics (e.g., “home solar ROI”, “off-grid kits”)
│   └── agent_loop_config.json   ← Defines chaining (NicheScout → SEOWriter)
│
├── agents/
│   ├── niche_scout.py           ← Scrapes trends, Reddit, Amazon, etc.
│   └── seo_writer.py            ← Converts findings into markdown blog posts
│
├── autogen_app.py               ← Bootstraps the loop and triggers task flow
└── requirements.txt             ← Modal + Autogen + scraping libs
