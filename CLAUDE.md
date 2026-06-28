# CV Agent — Project Instructions

This project tailors Amy's CV to job descriptions using a dedicated skill.

## Setup

- **Source of truth (data):** `master-cv.md` — Amy's full, fact-checked career history. Never edit this as a side effect of generating a CV.
- **Process (how to tailor):** `.claude/skills/executive-cv-tailor/SKILL.md` — read this whenever Amy asks to tailor her CV, check it against a JD, or produce related materials. Follow it exactly, including the Golden Rules.
- **Other skills:** `.claude/skills/` — use the matching skill when Amy asks for LinkedIn copy (`linkedin-executive-brand`), a cover letter (`cover-letter-strategist`), interview prep (`executive-interview-coach`), career advice (`career-positioning-advisor`), or achievement documentation (`achievement-library-builder`).
- **Photo:** `templates/amy-photo.jpg` — use in the PDF header when present.
- **Templates:** `templates/base-template.docx` if present — use for docx formatting/branding. Otherwise use a clean, professional executive layout.
- **Output:** save generated files to `output/[Company]_[Role]_CV_[date].docx` and matching `.pdf` unless told otherwise.

## House rules

- Never publish or send anything anywhere — output is local files only.
- Never add an education section detail not already in master-cv.md.
- After generating, give Amy a short note (3-5 lines) on what was emphasized, plus any flagged gaps. Don't over-explain.
