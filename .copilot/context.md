# Copilot Context: CV-Pipeline

## Project Purpose
Automated CV and cover letter generation for a scientific/technical career, with strict separation of content (YAML/JSON/MD in data/) and layout (LaTeX/Jinja2 in templates/). Supports multiple CV variants (Academic, Industrial) and is optimized for GitHub Actions automation, data validation, and completeness checks.

## Directory Structure & Roles

- **data/**  
  All user content.  
  - `personal.yaml`, `education.yaml`, `experience.yaml`, `skills.yaml`, `strengths.yaml`, `certifications.yaml`: Core data sources for CVs.
  - `cover-letter-template.yaml`: Modular cover letter content.
  - `university_curriculum/`:  
    - `aau_bsc_eng_course_descriptions.json`, `ucph_course_descriptions.json`: Course metadata.
    - `passed_courses.md`: Completed courses.
    - `academic_core/`: Academic meta-profile, grade requirements, learning objectives.
    - `Curricula/`, `Grades/`: PDFs and records of academic progress.
    - Multiple course description PDFs.

- **templates/**  
  All layout logic.  
  - `altacv-class/`, `cloud-engineer/`, `devops-engineer/`, `modern-cv-class/`, `software-developer/`:  
    - LaTeX classes, Jinja2 templates, and assets for each CV variant.
    - Subfolders may contain legacy or example files.

- **scripts/**  
  All automation logic.  
  - `generate.py`, `generate_ats.py`, `generate_old.py`: Main entry points for document generation.
  - `test_data_completeness.py`: Data validation.

- **output/**  
  All generated files.  
  - `generated/`: Output TeX, class, and config files.

- **docs/**  
  Authoring and tailoring guides.  
  - `ACHIEVEMENT_EXAMPLES.md`, `ATS_GUIDE.md`, `CONTENT_GUIDE.md`, `COVER_LETTER_GUIDE.md`, `TAILORING_GUIDE.md`:  
    - Best practices for content, ATS optimization, and customization.

- **.gitignore**  
  - Ignores: output/, LaTeX/Python/IDE artifacts, node_modules/, temp/backup files, and data/university_curriculum (for privacy).

## Workflow

1. Edit content in `data/`.
2. Select or modify a template in `templates/`.
3. Run a script from `scripts/` (locally or via GitHub Actions).
4. Retrieve generated files from `output/generated/` or GitHub Releases.

## Agent Guidance

- Never hardcode user data; always source from `data/`.
- Templates must be generic and reusable.
- Scripts must validate data completeness and fail clearly on missing/invalid fields.
- For new content, add to `data/`; for new layouts, add to `templates/`; for new logic, add to `scripts/`.
- Refer to `docs/` for content and tailoring best practices.

## CV Variants

- **Academic Researcher**: Focus on neutronics, scattering physics, facility experience.
- **Industrial Scientist**: Focus on applied nanoscience, computational modeling, leadership.

## Security & Privacy

- Academic records, in data/university_curriculum, are ignored by git for privacy.
- All generated files and build artifacts are ignored.

---
This file is for Copilot and coding agents. It encodes the real structure, workflow, and best practices of this repository for accurate, context-aware assistance.
