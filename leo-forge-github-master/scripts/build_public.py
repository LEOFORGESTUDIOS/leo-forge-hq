from pathlib import Path
import json, shutil
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/"public/api"
OUT.mkdir(parents=True, exist_ok=True)
files = ["site-config.json","projects.json","certifications.json","cyber-range.json","forge-log.json"]
for name in files:
    shutil.copy2(ROOT/"data"/name, OUT/name)
index = {
    "service":"Leo Forge Public Data",
    "website":"https://www.leoforgestudios.com",
    "generatedAt":datetime.now(timezone.utc).isoformat(),
    "feeds":[f"api/{x}" for x in files]
}
(OUT/"index.json").write_text(json.dumps(index, indent=2)+"\n")
print("Built public API.")
