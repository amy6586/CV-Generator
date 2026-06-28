---
name: executive-cv-tailor
description: Tailor Amy Raygada's CV to a specific job description for Director/Head of Data & AI, Data Governance, AI Strategy, Enterprise Transformation, and Consulting Partner-level roles. Use whenever Amy pastes or uploads a job description and asks for a tailored CV, asks how well her CV matches a role, asks for a LinkedIn headline/about section for a specific role, or asks for a gap analysis against a JD. Always use this skill rather than freeform CV editing — it enforces truthfulness rules and a consistent executive positioning process.
---

# Executive CV Tailoring — Data & AI Leadership

A skill for producing tailored, evidence-based executive CVs and related materials, scoped to Amy's actual career history in `master-cv.md`.

## Golden rules (never break these)

- Never invent projects, metrics, titles, or responsibilities not present in `master-cv.md` or explicitly stated by Amy in the conversation.
- Never change job titles or dates.
- If something needed for a strong match isn't in `master-cv.md`, say so and ask — don't guess, don't paper over it.
- Every claim in the output must trace back to evidence in `master-cv.md` or Amy's direct input.
- Apply Amy's voice rules throughout: no em dashes, short sentences, direct and practitioner-grounded, no AI-sounding phrasing or corporate filler. Avoid generic high-gloss executive-resume verbs ("architected," "spearheaded," "transformed") unless that specific word is the most accurate, plain description of what happened — precision beats impressiveness.

## Target roles

Default optimization targets, used to calibrate seniority framing and keyword emphasis (not used to invent experience):

- Director of Data & AI
- Data Transformation Director / Manager
- Head of Data Strategy
- Head of Data Governance / Director of Data Governance
- Enterprise Data Lead
- Director of AI Strategy
- Enterprise AI Transformation Lead
- Principal Data Strategist
- Chief Data Officer
- VP Data
- Consulting Partner (Data & AI)

If Amy provides a specific JD, optimize for that role specifically — the list above is the default lens when no JD is given, not a constraint on top of one.

## Workflow

### 1. Read the job description (if provided)

Extract:
- Core responsibilities
- Required competencies and seniority signals
- Leadership expectations (team size, geographic scope, P&L ownership)
- Technologies and frameworks named
- Industry context
- Likely ATS keywords (exact terms used in the JD)

### 2. Match against master-cv.md

Build a quick internal comparison — JD requirement vs. evidence in master-cv.md vs. gap. Don't necessarily show this full table to Amy unless she asks for the gap analysis explicitly; for a standard "tailor my CV" request, use it internally to decide what to surface and how, then go straight to the output.

If asked for a gap analysis, present as a table:

| Requirement | Evidence | Gap | Recommendation |

### 3. Select and frame content

- Pull from master-cv.md's tagged sections (`[leadership]`, `[delivery]`, `[commercial]`, `[thought-leadership]`, `[technical]`, `[governance]`, `[qa-engineering]`) based on JD fit.
- Surface "hidden executive value" — things in master-cv.md that are true but underplayed. Examples already known to apply to Amy: building a testing team from 2 to 14 people (Intertec) is organizational leadership, not a footnote. Running OKRs that improved goal completion by 75% (SMG) is operational leadership, not just process work. Look for this pattern — real scope stated too modestly — rather than inventing new scope.
- Lead with whichever of Amy's four concurrent roles (Thoughtworks Deputy Director, Thoughtworks Principal Strategist, Data Masterclass Coach, Cosmodata Founder) best matches the JD's seniority and orientation. Default lead is Thoughtworks Deputy Director unless the JD is clearly an independent-advisory or founder-type role.
- Earlier QA/engineering career (2010-2021) stays condensed by default — expand only if the JD specifically values deep technical/QA pedigree or a "built a team from the ground up" narrative.

### 4. Rewrite bullets

Each bullet should communicate, as plainly as possible: what the problem or context was, what Amy did, and what the outcome or scale was. Don't pad with corporate phrasing to hit a formula — if a bullet is true and clear in eight words, leave it at eight words.

Avoid weak filler ("responsible for," "helped with," "worked on") in favor of plain, accurate description of what Amy actually did — but don't replace one cliché set (weak verbs) with another (inflated verbs). The fix for "responsible for managing the team" is "managed the team" or "built the team from 2 to 14 people," not "spearheaded organizational transformation."

### 5. Output

Default output for a standard "tailor my CV for this JD" request:
- One tailored CV (docx and/or pdf, per Amy's standing preference for both depending on application)
- A short LinkedIn headline option matched to the role, only if asked

Everything else — cover letter, elevator pitch, executive biography, STAR interview stories, competency matrix — is opt-in. Don't generate these unless Amy asks for them specifically. If it seems like one would help, mention it briefly at the end rather than producing it unprompted.

### 6. Self-check before delivering (internal, don't show this to Amy as output)

- Did I invent any metric, project, or scope not in master-cv.md?
- Did I change any title or date?
- Does every bullet trace to real evidence?
- Does this sound like Amy, or does it sound like a generic AI-generated executive resume?
- Did I flag any gap I couldn't fill, rather than papering over it?

If any answer is wrong, fix before delivering.

## Notes

- master-cv.md is the only factual source. It's already structured and tagged for this purpose — read it fully before tailoring anything.
- The "Recent Commercial/BD Activity" section in master-cv.md is not yet LinkedIn-verified. Flag this to Amy if a tailored CV leans heavily on it, so she can confirm specifics (deal stage, exact company names) before sending anything external.
- German B1 is a real, recent credential not yet on LinkedIn — don't add it to an external CV without checking with Amy first.
