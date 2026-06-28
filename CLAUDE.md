# CV Agent — Project Instructions

This project tailors Amy's CV to job descriptions using a dedicated skill.

## Setup

- **Source of truth (data):** `master-cv.md` — Amy's full, fact-checked career history. Never edit this as a side effect of generating a CV.
- **Process (how to tailor):** `.claude/skills/executive-cv-tailor/SKILL.md` — read this whenever Amy asks to tailor her CV, check it against a JD, or produce related materials. Follow it exactly, including the Golden Rules.
- **Other skills:** `.claude/skills/` — use the matching skill based on what Amy asks for:

| Skill | Folder | Use when Amy asks for... |
|---|---|---|
| Executive CV Strategist | `executive-cv-tailor` | Tailor her CV for a specific role or JD |
| LinkedIn Executive Brand | `linkedin-executive-brand` | LinkedIn headline, About section, profile optimisation |
| Cover Letter Strategist | `cover-letter-strategist` | A cover letter or application letter for a role |
| Executive Interview Coach | `executive-interview-coach` | Interview prep, STAR stories, mock interviews |
| Career Positioning Advisor | `career-positioning-advisor` | Which roles to target, gap planning, offer evaluation, negotiation |
| Achievement Library Builder | `achievement-library-builder` | Documenting and quantifying achievements for CVs, interviews, or performance reviews |
- **Photo:** `templates/amy-photo.jpg` — use in the PDF header when present.
- **Templates:** `templates/base-template.docx` if present — use for docx formatting/branding. Otherwise use a clean, professional executive layout.
- **Output:** save generated files to `output/[Company]_[Role]_CV_[date].docx` and matching `.pdf` unless told otherwise.

## House rules

- Never publish or send anything anywhere — output is local files only.
- Never add an education section detail not already in master-cv.md.
- After generating, give Amy a short note (3-5 lines) on what was emphasized, plus any flagged gaps. Don't over-explain.
