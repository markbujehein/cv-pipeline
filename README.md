# Mark Buje Hein Sørensen - Professional CV Pipeline

This repository contains my automated CV generation pipeline, tailored for my background in **Nanoscience**, **Machine Learning**, and **Scattering Physics**. It uses LaTeX (via the AltaCV class) and YAML data to create specialized CV variants for different professional contexts.

## CV Variants

The pipeline generates three distinct CV variants, each optimized with specific colors and content filtering:

1.  **Nanoscientist** (Leadership & Research focus)
    -   *Color: Authority Blue*
    -   *Focus:* Academic achievements, research leadership, and broad scientific expertise.
2.  **Machine Learning Engineer** (Technical & Applied focus)
    -   *Color: Energetic Orange*
    -   *Focus:* GNNs, applied statistics, and computational modeling for scientific discovery.
3.  **Scattering Physicist** (Experimental & Precision focus)
    -   *Color: Steel Blue*
    -   *Focus:* Deep expertise in Neutronics, Neutron Compton Scattering (NCS), and hands-on facility experience (ISIS, MAX IV).

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
