# Mark Buje Hein Sørensen - Professional CV Pipeline

This repository contains my automated CV generation pipeline, tailored for my background in **Nanoscience**, **Machine Learning**, and **Scattering Physics**. It uses LaTeX (via the AltaCV class) and YAML data to create specialized CV variants for different professional contexts.

## CV Variants

The pipeline generates two distinct CV variants, each optimized for specific career goals while integrating **Machine Learning** as a foundational skill:

1.  **Academic Researcher** (PhD Target)
    -   *Color: Steel Blue*
    -   *Focus:* Deep expertise in Neutronics, scattering physics, and hands-on facility experience (ISIS, MAX IV). Optimized for PhD applications.
2.  **Industrial Scientist** (R&D/Job Target)
    -   *Color: Authority Blue*
    -   *Focus:* Applied Nanoscience, computational modeling, and research leadership. Optimized for regular scientist and R&D roles in industry.

## Automated Workflow

This project is optimized for automated generation via **GitHub Actions**. 

1.  **Edit** your data in the `data/` directory.
2.  **Commit and Push** your changes to the `main` branch.
3.  **Download** your generated CVs from the **GitHub Releases** section.

The pipeline automatically validates your data, compiles the LaTeX variants, and runs completeness tests on every push.

## Data Structure

The CV data is managed in the `data/` directory:
- `personal.yaml`: Contact details and variant taglines.
- `education.yaml`: Degrees, specialization, and thesis details.
- `experience.yaml`: Research roles and project experience (tagged for filtering).
- `skills.yaml`: Languages, programming, and laboratory techniques.
- `strengths.yaml`: Core competencies tailored for each profile.
- `certifications.yaml`: Relevant training and certifications.

## Scientific Profile Highlights

- **MSc Thesis:** Investigating novel neutron moderator materials (thymol, p-cymene) using computational and experimental methods (TOSCA, VESUVIO).
- **Facility Experience:** Hands-on work at MAX IV (CoSAXS) and ISIS Neutron and Muon Source.
- **ML Research:** Graphical Neural Networks for high-energy physics data (ALICE@CERN).

## License
MIT
