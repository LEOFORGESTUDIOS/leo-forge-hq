# Agent guide

Read `.github/copilot-instructions.md` first.

Before proposing changes:

```bash
python -m pip install jsonschema
python scripts/validate_data.py
python scripts/build_public.py
```

Do not manually edit generated files in `public/api`.
Do not merge your own pull request.
