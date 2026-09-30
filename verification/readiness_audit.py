from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["agent.yaml", "SOUL.md", "README.md", "AGENTS.md", "DUTIES.md", "RULES.md", "EXPLAINABILITY.md", ".env.example", ".gitignore", "requirements.txt", "pytest.ini"]
HEADINGS = ["## Inputs and Data Sources", "## Decision and Reasoning", "## Limits and Constraints"]


def sentences(text: str) -> int:
    return len(re.findall(r"(?<=[.!?])\s+", text.strip())) + (1 if text.strip() else 0)


def main() -> int:
    errors = []
    for item in REQUIRED:
        if not (ROOT / item).is_file(): errors.append(f"missing file: {item}")
    for directory in ["adapters", "config", "contracts", "core", "skills", "tools", "tests", "verification"]:
        if not (ROOT / directory).is_dir(): errors.append(f"missing directory: {directory}")
    doc = (ROOT / "EXPLAINABILITY.md").read_text(encoding="utf-8") if (ROOT / "EXPLAINABILITY.md").exists() else ""
    for heading in HEADINGS:
        if doc.count(heading) != 1: errors.append(f"required heading count invalid: {heading}")
    if "## Inputs\n" in doc or "## Decision\n" in doc or "## Limits\n" in doc:
        errors.append("conflicting exact explainability heading found")
    for heading, next_heading in zip(HEADINGS, HEADINGS[1:] + [None]):
        section = doc.split(heading, 1)[1] if heading in doc else ""
        if next_heading and next_heading in section: section = section.split(next_heading, 1)[0]
        if sentences(section) < 2: errors.append(f"section has fewer than two sentences: {heading}")
    if errors:
        print("READINESS AUDIT: FAIL")
        print("\n".join(f"- {e}" for e in errors))
        return 1
    print("READINESS AUDIT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
