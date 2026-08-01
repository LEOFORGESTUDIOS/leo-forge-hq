# Airo integration

Replace `YOUR_GITHUB_ORG`.

Base URL:

`https://YOUR_GITHUB_ORG.github.io/leo-forge-hq/api`

Paste into Airo:

```text
Connect the Leo Forge website to:
https://YOUR_GITHUB_ORG.github.io/leo-forge-hq/api

Map projects.json to Projects and Proof of Work.
Map certifications.json to The Forge Path.
Map cyber-range.json to Cyber Range Operations.
Map forge-log.json to The Forge Log.
Map site-config.json to brand metadata.

Load asynchronously, escape displayed text, and use local fallbacks if GitHub is unavailable.
Never display records where public is false.
Never show an earned stamp unless status is earned and both earnedDate and verificationUrl exist.
Never show a write-up button unless publicWriteupAllowed is true and a URL exists.
Do not expose private repositories.
Do not replace the Airo-hosted website.
```
