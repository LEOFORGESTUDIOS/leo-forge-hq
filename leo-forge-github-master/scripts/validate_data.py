from pathlib import Path
import json
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
MAP = {
    "site-config.json":"site-config.schema.json",
    "projects.json":"projects.schema.json",
    "certifications.json":"certifications.schema.json",
    "cyber-range.json":"cyber-range.schema.json",
    "forge-log.json":"forge-log.schema.json",
}
failed = False
for data_name, schema_name in MAP.items():
    data = json.loads((ROOT/"data"/data_name).read_text())
    schema = json.loads((ROOT/"schemas"/schema_name).read_text())
    errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(data),
                    key=lambda e:list(e.absolute_path))
    if errors:
        failed = True
        print(f"{data_name}:")
        for e in errors:
            path = ".".join(map(str,e.absolute_path)) or "<root>"
            print(f"  {path}: {e.message}")
    else:
        print(f"{data_name}: OK")

for cert in json.loads((ROOT/"data/certifications.json").read_text()):
    if cert["status"] == "earned" and (not cert.get("earnedDate") or not cert.get("verificationUrl")):
        failed = True
        print(f"{cert['name']}: earned requires earnedDate and verificationUrl")

for mission in json.loads((ROOT/"data/cyber-range.json").read_text()):
    if mission["status"] == "completed" and mission["progress"] != 100:
        failed = True
        print(f"{mission['id']}: completed requires progress=100")

if failed:
    raise SystemExit(1)
print("All public data validated.")
