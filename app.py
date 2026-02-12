# Generate Professional CV PDF for Ubaid Bin Waris
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import HRFlowable

file_path = "Ubaid_Bin_Waris_CV.pdf"
doc = SimpleDocTemplate(file_path)
elements = []

styles = getSampleStyleSheet()

# Custom Styles
title_style = styles["Heading1"]
section_style = styles["Heading2"]
normal_style = styles["BodyText"]

# Header
elements.append(Paragraph("<b>UBAID BIN WARIS</b>", title_style))
elements.append(Spacer(1, 0.2 * inch))
elements.append(Paragraph("Islamabad, Pakistan", normal_style))
elements.append(Paragraph("LinkedIn: linkedin.com/in/ubaidbinwaris", normal_style))
elements.append(Paragraph("GitHub: github.com/UbaidBinWaris", normal_style))
elements.append(Paragraph("Portfolio: uabidbinwaris.dev", normal_style))
elements.append(Spacer(1, 0.3 * inch))
elements.append(HRFlowable(width="100%", thickness=1, color=colors.grey))
elements.append(Spacer(1, 0.2 * inch))

# Profile
elements.append(Paragraph("PROFILE", section_style))
elements.append(Spacer(1, 0.1 * inch))
profile_text = """
Results-driven Full Stack & Cloud Engineer with 3+ years of hands-on experience 
in backend development, scalable SaaS systems, automation platforms, and cloud deployments. 
Experienced in full software lifecycle including system architecture, REST API development, 
database modeling, AWS infrastructure setup, DevOps automation, security hardening, and SEO optimization.
Strong foundation in Data Structures, Operating Systems, and system-level programming (C++ & Assembly).
"""
elements.append(Paragraph(profile_text, normal_style))
elements.append(Spacer(1, 0.3 * inch))

# Education
elements.append(Paragraph("EDUCATION", section_style))
elements.append(Spacer(1, 0.1 * inch))
elements.append(Paragraph("<b>Bachelor of Science in Computer Science</b>", normal_style))
elements.append(Paragraph("Islamabad, Pakistan", normal_style))
elements.append(Spacer(1, 0.2 * inch))

# Experience Section
elements.append(Paragraph("PROFESSIONAL EXPERIENCE", section_style))
elements.append(Spacer(1, 0.1 * inch))

experience_points = [
    "<b>Full Stack Developer – GixiAI (Aug 2025 – Present)</b>",
    "• Designed AI-powered automation systems and REST APIs.",
    "• Managed AWS EC2 deployment, Nginx setup, SSL, DNS, and PM2 configuration.",
    "• Implemented secure authentication, rate limiting, and optimized database queries.",
    "",
    "<b>Full Stack Developer – BluCentric (Feb 2025 – May 2025)</b>",
    "• Built full-stack applications using Next.js and SQL.",
    "• Implemented JWT authentication and RBAC systems.",
    "• Designed and documented scalable API architecture.",
    "",
    "<b>Web Developer – HH Tech Hub (Jun 2025 – Jul 2025)</b>",
    "• Developed responsive UI components and optimized performance & SEO.",
    "",
    "<b>Web Development Intern – HEC (Jun 2023 – Aug 2023)</b>",
    "• Contributed to frontend improvements and system documentation."
]

for point in experience_points:
    elements.append(Paragraph(point, normal_style))
    elements.append(Spacer(1, 0.1 * inch))

elements.append(Spacer(1, 0.2 * inch))

# Projects Section
elements.append(Paragraph("PROJECTS", section_style))
elements.append(Spacer(1, 0.1 * inch))

projects_points = [
    "<b>Real Estate Management System (SaaS)</b> – Multi-role CRM, property management, AWS deployment, SSL & security hardening.",
    "<b>GixiAI Automation Platform</b> – Backend automation engine, concurrent task processing, AWS infrastructure setup.",
    "<b>LetsFixHome.com</b> – Lead generation system with CRM storage & server-side tracking.",
    "<b>MedicalInfoPhD.com</b> – Appointment booking system with admin dashboard & secure deployment.",
    "<b>Dental Clinic Website</b> – Appointment scheduling with SEO optimization.",
    "<b>Echo Chat Application</b> – Real-time messaging using Socket.io & MongoDB.",
    "<b>University Management System</b> – SQL-based CRUD dashboard.",
    "<b>Smart Car Challan System (C++)</b> – Encrypted file-based record system."
]

for project in projects_points:
    elements.append(Paragraph(project, normal_style))
    elements.append(Spacer(1, 0.1 * inch))

elements.append(Spacer(1, 0.2 * inch))

# Skills Section
elements.append(Paragraph("SKILLS", section_style))
elements.append(Spacer(1, 0.1 * inch))

skills_text = """
Programming: JavaScript, TypeScript, Java (Spring Boot), PHP, C++, C, SQL<br/>
Frontend: React.js, Next.js, Tailwind CSS<br/>
Backend: Node.js, Express.js, Laravel, Spring Boot, REST APIs, JWT<br/>
Databases: MongoDB, MySQL, PostgreSQL<br/>
Cloud & DevOps: AWS EC2, Ubuntu Server, Nginx, PM2, SSL, DNS, CI/CD<br/>
Security: Authentication systems, secure headers, rate limiting
"""
elements.append(Paragraph(skills_text, normal_style))
elements.append(Spacer(1, 0.2 * inch))

# Languages
elements.append(Paragraph("LANGUAGES", section_style))
elements.append(Spacer(1, 0.1 * inch))
elements.append(Paragraph("Urdu – Native Proficiency", normal_style))
elements.append(Paragraph("English – Professional Working Proficiency", normal_style))

# Build PDF
doc.build(elements)

file_path