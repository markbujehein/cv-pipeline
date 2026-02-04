#!/usr/bin/env python3
"""
Simple CV generator - No templating, just direct YAML to LaTeX generation.
Each variant has a generation function that outputs complete LaTeX.
"""

import yaml
import argparse
from pathlib import Path
from typing import Dict, Any

def escape_latex(text: str) -> str:
    """Escape LaTeX special characters."""
    if not isinstance(text, str):
        text = str(text)
    chars = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
        '\\': r'\textbackslash{}',
    }
    return ''.join(chars.get(c, c) for c in text)

def load_yaml_data(data_dir: Path) -> Dict[str, Any]:
    """Load all YAML files with validation."""
    data = {}
    required_files = ['personal', 'experience', 'skills', 'strengths', 'education', 'certifications']

    for yaml_file in data_dir.glob('*.yaml'):
        with open(yaml_file) as f:
            data[yaml_file.stem] = yaml.safe_load(f)

    # Validate all required files are present
    missing = [f for f in required_files if f not in data]
    if missing:
        raise ValueError(f"Missing required YAML files: {', '.join(missing)}.yaml")

    # Validate required fields in personal.yaml
    personal = data['personal']
    required_personal = ['first_name', 'last_name', 'email', 'phone', 'location', 'website', 'linkedin', 'github', 'taglines']
    missing_personal = [f for f in required_personal if f not in personal]
    if missing_personal:
        raise ValueError(f"Missing required fields in personal.yaml: {', '.join(missing_personal)}")

    # Validate taglines exist for all variants
    required_taglines = ['academic-researcher', 'industrial-scientist']
    missing_taglines = [t for t in required_taglines if t not in personal['taglines']]
    if missing_taglines:
        raise ValueError(f"Missing taglines in personal.yaml: {', '.join(missing_taglines)}")

    return data

def generate_industrial_scientist(data: Dict[str, Any]) -> str:
    """Generate industrial scientist CV."""
    personal = data['personal']
    experience = data['experience']
    skills = data['skills']
    strengths = data['strengths']
    education = data['education']
    certifications = data.get('certifications', [])

    # Build LaTeX directly
    latex = r'''\documentclass[10pt,a4paper,withhyper]{altacv}

\geometry{left=1cm,right=1cm,top=1.5cm,bottom=1.5cm,columnsep=1.5cm}

\usepackage{paracol}

\iftutex
  \setmainfont{Roboto Slab}
  \setsansfont{Lato}
  \renewcommand{\familydefault}{\sfdefault}
\else
  \usepackage[rm]{roboto}
  \usepackage[defaultsans]{lato}
  \renewcommand{\familydefault}{\sfdefault}
\fi

% INDUSTRIAL SCIENTIST: Innovation & Creativity (Restored Psychology)
\definecolor{SlateGrey}{HTML}{2E2E2E}
\definecolor{LightGrey}{HTML}{666666}
\definecolor{EnergeticOrange}{HTML}{ff6b35}
\definecolor{FriendlyTeal}{HTML}{00d9ff}
\definecolor{CommunityPurple}{HTML}{7c3aed}
\colorlet{name}{EnergeticOrange}
\colorlet{tagline}{CommunityPurple}
\colorlet{heading}{EnergeticOrange}
\colorlet{headingrule}{FriendlyTeal}
\colorlet{subheading}{CommunityPurple}
\colorlet{accent}{FriendlyTeal}
\colorlet{emphasis}{SlateGrey}
\colorlet{body}{LightGrey}

\renewcommand{\namefont}{\Huge\sffamily\bfseries}
\renewcommand{\personalinfofont}{\small}
\renewcommand{\cvsectionfont}{\Large\sffamily\bfseries}
\renewcommand{\cvsubsectionfont}{\large\sffamily}

\renewcommand{\cvItemMarker}{{\small\textbullet}}
\renewcommand{\cvRatingMarker}{\faCircle}

% Override linkedin to show "LinkedIn" text with clickable link
\renewcommand{\linkedin}[1]{%
  \printinfo{\faLinkedin}{LinkedIn}[https://linkedin.com/in/#1]%
}

\begin{document}
'''

    # Personal info
    latex += f"\\name{{{escape_latex(personal['first_name'])} {escape_latex(personal['last_name'])}}}\n"
    latex += f"\\tagline{{{escape_latex(personal['taglines']['industrial-scientist'])}}}\n\n"

    # Contact info
    latex += "\\personalinfo{%\n"
    latex += f"  \\email{{{escape_latex(personal['email'])}}}\n"
    latex += f"  \\phone{{{escape_latex(personal['phone'])}}}\n"
    latex += f"  \\location{{{escape_latex(personal['location'])}}}\n"

    website = personal['website'].replace('https://', '').replace('http://', '')
    latex += f"  \\homepage{{{escape_latex(website)}}}\n"

    linkedin_id = personal['linkedin'].replace('https://www.linkedin.com/in/', '').replace('https://linkedin.com/in/', '').replace('/', '')
    latex += f"  \\linkedin{{{escape_latex(linkedin_id)}}}\n"

    github_user = personal['github'].replace('https://github.com/', '').replace('/', '')
    latex += f"  \\github{{{escape_latex(github_user)}}}\n"
    latex += "}\n\n"

    latex += "\\makecvheader\n\n"
    latex += "\\columnratio{0.6}\n\n"
    latex += "\\begin{paracol}{2}\n\n"

    # Scientific Profile (first strength)
    latex += "\\cvsection{Scientific Profile}\n\n"
    latex += f"\\textbf{{{escape_latex(strengths[0]['title'])}}}\n\n"
    latex += f"{escape_latex(strengths[0]['description'])}\n\n"
    latex += "\\medskip\n\n"

    # Research & Project Experience
    latex += "\\cvsection{Research \\& Projects}\n\n"
    research_exp = [e for e in experience if 'academic-researcher' in e['tags'] or 'industrial-scientist' in e['tags']]
    # Filter out entries that are primarily leadership/trust for the main section
    primary_research = [e for e in research_exp if 'leadership' not in e['tags'] and 'trust' not in e['tags']]
    
    for job in primary_research[:3]:
        latex += f"\\cvevent{{{escape_latex(job['title'])}}}{{{escape_latex(job['company'])}}}"
        latex += f"{{{job['start_date']}--{job['end_date']}}}{{{escape_latex(job['location'])}}}\n"
        latex += "\\begin{itemize}\n"
        for achievement in job["achievements"][:4]:
            latex += f"\\item {escape_latex(achievement)}\n"
        latex += "\\end{itemize}\n\n"
        latex += "\\divider\n\n"

    # Leadership & Volunteering
    latex += "\\cvsection{Leadership \\& Impact}\n\n"
    leadership_exp = [e for e in experience if 'leadership' in e['tags'] or 'volunteer' in e['tags'] or 'trust' in e['tags']]
    for job in leadership_exp[:2]:
        latex += f"\\cvevent{{{escape_latex(job['title'])}}}{{{escape_latex(job['company'])}}}"
        latex += f"{{{job['start_date']}--{job['end_date']}}}{{{escape_latex(job['location'])}}}\n"
        latex += "\\begin{itemize}\n"
        # Fewer achievements for leadership to save space
        for achievement in job["achievements"][:2]:
            latex += f"\\item {escape_latex(achievement)}\n"
        latex += "\\end{itemize}\n\n"
        if job != leadership_exp[1]:
            latex += "\\divider\n\n"

    # Switch to sidebar
    latex += "\\switchcolumn\n\n"

    # Core Strengths (strengths 1-4, skip first as it's in Leadership Profile)
    latex += "\\cvsection{Core Strengths}\n\n"
    for strength in strengths[:4]:
        latex += f"\\cvachievement{{\\faTrophy}}{{{escape_latex(strength['title'])}}}{{{escape_latex(strength['description'])}}}\n\n"
        if strength != strengths[3]:
            latex += "\\divider\n\n"

    # Expertise
    latex += "\\cvsection{Scientific Expertise}\n\n"
    for skill in skills['Scientific Expertise']:
        latex += f"\\cvtag{{{escape_latex(skill)}}}\n"
    latex += "\n\\divider\\medskip\n\n"

    # Programming & Computation
    latex += "\\cvsection{Computation \\& ML}\n\n"
    for skill in skills['Machine Learning & Statistics']:
        latex += f"\\cvtag{{{escape_latex(skill)}}}\n"
    latex += "\n\\divider\\smallskip\n\n"
    for skill in skills['Programming & Computation']:
        latex += f"\\cvtag{{{escape_latex(skill)}}}\n"

    # Education
    latex += "\n\\cvsection{Education}\n\n"
    for edu in education:
        degree = escape_latex(edu['degree'])
        if edu.get('specialization'):
            degree += f" ({escape_latex(edu['specialization'])})"
        latex += f"\\cvevent{{{degree}}}{{{escape_latex(edu['institution'])}}}"
        latex += f"{{{edu['start_date']}--{edu['end_date']}}}{{{escape_latex(edu['location'])}}}\n\n"
        if edu.get('notes'):
            latex += f"{escape_latex(edu['notes'])}\n\n"

    # Certifications
    latex += "\\cvsection{Certifications}\n\n"
    for cert in certifications[:4]:
        latex += f"\\cvtag{{{escape_latex(cert['name'])}}}\n"

    latex += "\n\\end{paracol}\n\n"
    latex += "\\end{document}\n"

    return latex

def generate_academic_researcher(data: Dict[str, Any]) -> str:
    """Generate academic researcher CV."""
    personal = data['personal']
    experience = data['experience']
    skills = data['skills']
    strengths = data['strengths']
    education = data['education']
    certifications = data.get('certifications', [])

    latex = r'''\documentclass[10pt,a4paper,withhyper]{altacv}

\geometry{left=1cm,right=1cm,top=1.5cm,bottom=1.5cm,columnsep=1.5cm}

\usepackage{paracol}

\iftutex
  \setmainfont{Roboto}
  \setsansfont{Roboto}
  \setmonofont{Roboto Mono}
  \renewcommand{\familydefault}{\sfdefault}
\else
  \usepackage{roboto}
  \usepackage[T1]{fontenc}
  \renewcommand{\familydefault}{\sfdefault}
\fi

% ACADEMIC RESEARCHER: Stability & Precision (Restored Psychology)
\definecolor{SlateGrey}{HTML}{2E2E2E}
\definecolor{LightGrey}{HTML}{666666}
\definecolor{SteelBlue}{HTML}{4682b4}
\definecolor{IndustrialGrey}{HTML}{6c757d}
\definecolor{SystemGreen}{HTML}{059669}
\colorlet{name}{SlateGrey}
\colorlet{tagline}{SteelBlue}
\colorlet{heading}{SteelBlue}
\colorlet{headingrule}{IndustrialGrey}
\colorlet{subheading}{SteelBlue}
\colorlet{accent}{SystemGreen}
\colorlet{emphasis}{SlateGrey}
\colorlet{body}{LightGrey}

\renewcommand{\namefont}{\Huge\sffamily\bfseries}
\renewcommand{\personalinfofont}{\footnotesize\ttfamily}
\renewcommand{\cvsectionfont}{\LARGE\sffamily\bfseries}
\renewcommand{\cvsubsectionfont}{\large\sffamily\bfseries}

\renewcommand{\cvItemMarker}{{\small\textbullet}}
\renewcommand{\cvRatingMarker}{\faCircle}

\renewcommand{\linkedin}[1]{%
  \printinfo{\faLinkedin}{LinkedIn}[https://linkedin.com/in/#1]%
}

\begin{document}
'''

    # Personal info
    latex += f"\\name{{{escape_latex(personal['first_name'])} {escape_latex(personal['last_name'])}}}\n"
    latex += f"\\tagline{{{escape_latex(personal['taglines']['academic-researcher'])}}}\n\n"

    latex += "\\personalinfo{%\n"
    latex += f"  \\email{{{escape_latex(personal['email'])}}}\n"
    latex += f"  \\phone{{{escape_latex(personal['phone'])}}}\n"
    latex += f"  \\location{{{escape_latex(personal['location'])}}}\n"

    website = personal['website'].replace('https://', '').replace('http://', '')
    latex += f"  \\homepage{{{escape_latex(website)}}}\n"

    linkedin_id = personal['linkedin'].replace('https://www.linkedin.com/in/', '').replace('https://linkedin.com/in/', '').replace('/', '')
    latex += f"  \\linkedin{{{escape_latex(linkedin_id)}}}\n"

    github_user = personal['github'].replace('https://github.com/', '').replace('/', '')
    latex += f"  \\github{{{escape_latex(github_user)}}}\n"
    latex += "}\n\n"

    latex += "\\makecvheader\n\n"
    latex += "\\columnratio{0.6}\n\n"
    latex += "\\begin{paracol}{2}\n\n"

    # Technical Profile
    latex += "\\cvsection{Technical Profile}\n\n"
    latex += f"{escape_latex(strengths[0]['description'])}\n\n"
    latex += "\\medskip\n\n"

    # Infrastructure & Research Experience
    latex += "\\cvsection{Research \\& Infrastructure}\n\n"
    primary_research = [e for e in experience if 'academic-researcher' in e['tags'] and 'trust' not in e['tags']]
    
    for job in primary_research[:3]:
        latex += f"\\cvevent{{{escape_latex(job['title'])}}}{{{escape_latex(job['company'])}}}"
        latex += f"{{{job['start_date']}--{job['end_date']}}}{{{escape_latex(job['location'])}}}\n"
        latex += "\\begin{itemize}\n"
        for achievement in job["achievements"][:4]:
            latex += f"\\item {escape_latex(achievement)}\n"
        latex += "\\end{itemize}\n\n"
        latex += "\\divider\n\n"

    # Positions of Trust & Leadership
    latex += "\\cvsection{Leadership \\& Trust}\n\n"
    leadership_exp = [e for e in experience if 'trust' in e['tags'] or 'leadership' in e['tags']]
    for job in leadership_exp[:2]:
        latex += f"\\cvevent{{{escape_latex(job['title'])}}}{{{escape_latex(job['company'])}}}"
        latex += f"{{{job['start_date']}--{job['end_date']}}}{{{escape_latex(job['location'])}}}\n"
        latex += "\\begin{itemize}\n"
        for achievement in job["achievements"][:2]:
            latex += f"\\item {escape_latex(achievement)}\n"
        latex += "\\end{itemize}\n\n"
        if job != leadership_exp[1]:
            latex += "\\divider\n\n"

    latex += "\\switchcolumn\n\n"

    # Core Competencies (first 4 strengths)
    latex += "\\cvsection{Core Competencies}\n\n"
    for strength in strengths[:3]:
        latex += f"\\cvachievement{{\\faCogs}}{{{escape_latex(strength['title'])}}}{{{escape_latex(strength['description'])}}}\n\n"
        if strength != strengths[3]:
            latex += "\\divider\n\n"

    # Scattering Expertise
    latex += "\\cvsection{Scattering Expertise}\n\n"
    for skill in skills['Scientific Expertise']:
        latex += f"\\cvtag{{{escape_latex(skill)}}}\n"
    latex += "\n\\divider\\smallskip\n\n"

    latex += "\\textbf{Computational \\& ML Stack}\n\n"
    for skill in skills['Machine Learning & Statistics']:
        latex += f"\\cvtag{{{escape_latex(skill)}}}\n"
    latex += "\n\\divider\\smallskip\n\n"
    for skill in skills['Programming & Computation']:
        latex += f"\\cvtag{{{escape_latex(skill)}}}\n"

    # Education
    latex += "\n\\cvsection{Education}\n\n"
    for edu in education:
        degree = escape_latex(edu['degree'])
        latex += f"\\cvevent{{{degree}}}{{{escape_latex(edu['institution'])}}}"
        latex += f"{{{edu['start_date']}--{edu['end_date']}}}{{{escape_latex(edu['location'])}}}\n\n"
        if edu.get('notes'):
            latex += f"{escape_latex(edu['notes'])}\n\n"

    # Certifications
    latex += "\\cvsection{Certifications}\n\n"
    for cert in certifications[:4]:
        latex += f"\\cvtag{{{escape_latex(cert['name'])}}}\n"

    latex += "\n\\end{paracol}\n\n"
    latex += "\\end{document}\n"

    return latex

def main():
    parser = argparse.ArgumentParser(
        description='CV Generator - Direct YAML to LaTeX conversion',
        epilog='Generates LaTeX CV from YAML data with built-in validation'
    )
    parser.add_argument('--variant', required=True,
                       choices=['academic-researcher', 'industrial-scientist'],
                       help='CV variant to generate')
    parser.add_argument('--data-dir', required=True, type=Path,
                       help='Directory containing YAML data files')
    parser.add_argument('--output', required=True, type=Path,
                       help='Output .tex file path')
    args = parser.parse_args()

    try:
        # Validate data directory exists
        if not args.data_dir.exists():
            print(f"Error: Data directory not found: {args.data_dir}", file=sys.stderr)
            return 1

        # Load and validate data
        print(f"Loading YAML data from {args.data_dir}...")
        data = load_yaml_data(args.data_dir)
        print(f"Loaded data files: {', '.join(sorted(data.keys()))}")

        # Generate based on variant
        generators = {
            'industrial-scientist': generate_industrial_scientist,
            'academic-researcher': generate_academic_researcher,
        }

        print(f"Generating LaTeX for variant: {args.variant}")
        latex_output = generators[args.variant](data)

        # Validate output is not empty
        if not latex_output.strip():
            print("Error: Generated empty LaTeX output", file=sys.stderr)
            return 1

        # Validate LaTeX structure
        if '\\begin{document}' not in latex_output or '\\end{document}' not in latex_output:
            print("Error: Invalid LaTeX structure - missing document markers", file=sys.stderr)
            return 1

        # Write output
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(latex_output)

        lines = latex_output.count('\n')
        size = len(latex_output.encode('utf-8'))
        print(f"✓ Generated {args.output}")
        print(f"  Lines: {lines}")
        print(f"  Size: {size} bytes")

        return 0

    except ValueError as e:
        print(f"Validation Error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    import sys
    sys.exit(main())
