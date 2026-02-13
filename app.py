
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, Flowable, KeepInFrame
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
import os

# --- Configuration ---
FILE_PATH = "Ubaid_Bin_Waris_CV.pdf"
PAGE_SIZE = A4
MARGIN = 10 * mm
COL_GAP = 5 * mm

# --- Colors (extracted from style.css) ---
COLOR_TEAL = colors.HexColor("#449399")
COLOR_DARK_GREY = colors.HexColor("#313c4e")
COLOR_LIGHT_GREY = colors.HexColor("#989da6")
COLOR_TEXT = colors.black
COLOR_TEXT_MUTED = colors.HexColor("#7c7c7c")

# --- Content Data (Preserved from original app.py) ---
PROFILE_DATA = {
    "name": "Ubaid Bin Waris",
    "title": "Computer Science\nFull Stack Developer\nStudent", 
    "image": "resources/me.jpg",
    "contacts": [
        {"icon": "resources/mail.svg", "text": "ubaidwaris34@gmail.com"},
        {"icon": "resources/phone.svg", "text": "+92 3186659417"},
        {"icon": "resources/location.svg", "text": "Rawal Town, Islamabad"},
        {"icon": "resources/linkin.svg", "text": "linkedin.com/in/ubaid-waris-441942284"},
        {"icon": "resources/github.svg", "text": "github.com/UbaidBinWaris"},
        {"icon": "resources/stackoverflow.svg", "text": "stackoverflow.com/users/21611585/ubaid-bin-waris"},
    ]
}

EDUCATION_DATA = [
    {
        "degree": "BSCS",
        "institution": "SZABIST Islamabad",
        "date": "02/2023 - Present",
        "cgpa": "3.65",
        "details": ["Digital Logic Design", "Data Structures and Algorithms", "Software Engineering", "Operating Systems", "Database Management Systems", "Computer Organization and Assembly language"]
    },
    {
        "degree": "FSC",
        "institution": "Islamabad Model Postgraduate College H-8, Islamabad",
        "date": "05/2020 - 07/2022",
        "cgpa": "70%",
        "details": ["Mathematics", "Statistics", "Economics"]
    }
]

CERTIFICATES_DATA = [
    {
        "title": "Web Development",
        "date": "06/2024 - 12/2024",
        "desc": "Skilled in HTML, CSS, and JavaScript, with expertise in creating responsive, interactive web applications, focusing on custom UI components, animations, and optimized user experiences."
    },
    {
        "title": "Mastering C++ language Programming for Beginners",
        "date": "01/2024 - 03/2024",
        "desc": "Having a solid understanding of fundamental programming concepts, mastering C++ basics, and be equipped to write efficient and error-free code"
    },
    {
        "title": "Cyber Security",
        "date": "02/2022 - 08/2022",
        "desc": "Computer Network, cloud computing and Ethical hacking. Designe a network implements a private cloud server on it with Secured environment."
    }
]

LANGUAGES_DATA = [
    {"lang": "Urdu", "level": "Native or Bilingual Proficiency"},
    {"lang": "Punjabi", "level": "Full Professional Proficiency"},
    {"lang": "English", "level": "Limited Working Proficiency"}
]

SKILLS_DATA = [
    "Data Structures and Algorithms", "C/C++", "Object Oriented Design", "Cyber Security", 
    "Cloud Computing", "Computer Networks", "HTML / CSS / Javascript", "MS Tools", 
    "Version Control (Git)", "Problem Solving", "React js", "Mern Stack", "Next js", 
    "Responsive Web Design"
]

EXPERIENCE_DATA = [
    {
        "role": "Intern",
        "company": "Higher Education Commission (HEC) of Pakistan",
        "date": "03/2024 - 06/2024",
        "desc": "Assisted in HR tasks like hiring and record management; later designed and developed responsive web pages for various departments in the IT division."
    },
    {
        "role": "Full Stack Developer",
        "company": "BluCentric",
        "date": "03/2025 - 06/2025",
        "desc": "Developed and maintained web applications on a ViciDial server using PHP and Linux; worked on both front-end and back-end features, optimized system performance, and customized web pages for call center operations."
    }
]

PROJECTS_DATA = [
    {
        "title": "Music Web Application",
        "date": "01/2025 - 02/2025",
        "desc": "Built a responsive music web app using HTML, CSS, and JavaScript, featuring custom music player controls, playlist management, and volume adjustment."
    },
    {
        "title": "Car Challan System C++",
        "date": "02/2024 - 03/2024",
        "desc": "Developed a DSA-based system with encrypted file handling for police officers to manage car challans. Includes warnings and towing actions if challans exceed 10, with code modularized across multiple files."
    }
]

INTERESTS_DATA = ["Competative Programming", "Linux"]


# --- PDF Generation ---

def create_badge(text):
    # Create a small Table that looks like a badge
    ps = ParagraphStyle(name='BadgeText', fontSize=8, textColor=colors.white, alignment=TA_CENTER)
    p = Paragraph(text, ps)
    # Background color is handled by cell style
    t = Table([[p]], colWidths=[None]) # Auto width? Reportlab tables need fixed width usually or carefully calculated
    # Workaround: Use a Flowable or just a Table with a background
    # Since widths are variable, it's tricky. We'll use a fixed width or just text with background.
    # Simpler approach: Just text for now.
    # Better approach: A Table with a background color for the cell.
    # We will estimate width based on text length.
    width = len(text) * 4.5 + 10 # heuristic
    t = Table([[p]], colWidths=[width])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), COLOR_LIGHT_GREY),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('ROUNDEDCORNERS', [2, 2, 2, 2]), # Note: ReportLab 3.6+ supports rounded corners on rects but maybe not tables easily without custom drawing.
        # Fallback to simple background rect.
    ]))
    return t

class CircularImage(Flowable):
    def __init__(self, img_path, size=125):
        Flowable.__init__(self)
        self.img_path = img_path
        self.size = size

    def draw(self):
        from reportlab.lib.utils import ImageReader
        try:
            img = ImageReader(self.img_path)
            self.canv.saveState()
            path = self.canv.beginPath()
            # Circle center at (size/2, size/2) with radius size/2
            radius = self.size / 2
            path.circle(radius, radius, radius)
            self.canv.clipPath(path, stroke=0)
            # Draw image
            self.canv.drawImage(self.img_path, 0, 0, width=self.size, height=self.size, mask='auto', preserveAspectRatio=True, anchor='c')
            self.canv.restoreState()
            # Draw border
            self.canv.setStrokeColor(COLOR_TEAL)
            self.canv.setLineWidth(4)
            self.canv.circle(radius, radius, radius, stroke=1, fill=0)
        except Exception as e:
            print(f"Error drawing image: {e}")

    def wrap(self, availWidth, availHeight):
        return (self.size, self.size)


def create_pdf():
    doc = SimpleDocTemplate(
        FILE_PATH,
        pagesize=A4,
        topMargin=MARGIN,
        bottomMargin=MARGIN,
        leftMargin=MARGIN,
        rightMargin=MARGIN
    )
    
    styles = getSampleStyleSheet()
    # Custom Styles
    s_normal = ParagraphStyle('Normal_Custom', parent=styles['Normal'], fontSize=9, leading=11, fontName='Helvetica', textColor=COLOR_TEXT)
    s_name = ParagraphStyle('Name', parent=styles['Normal'], fontSize=24, leading=28, fontName='Helvetica', spaceAfter=2)
    s_title = ParagraphStyle('Title', parent=styles['Normal'], fontSize=12, leading=14, fontName='Helvetica', textColor=COLOR_TEAL)
    s_contact = ParagraphStyle('Contact', parent=styles['Normal'], fontSize=9, leading=18, fontName='Helvetica', alignment=TA_RIGHT)
    
    s_header_text = ParagraphStyle('SectionHeader', parent=styles['Normal'], fontSize=12, leading=14, fontName='Helvetica-Bold', textColor=COLOR_TEXT, spaceBefore=10, spaceAfter=5, textTransform='uppercase')
    
    s_subhead = ParagraphStyle('Subhead', parent=styles['Normal'], fontSize=10, leading=12, fontName='Helvetica-Bold', spaceBefore=2)
    s_subhead_sm = ParagraphStyle('SubheadSmall', parent=styles['Normal'], fontSize=9, leading=11, fontName='Helvetica-Bold', spaceBefore=1)
    s_meta = ParagraphStyle('Meta', parent=styles['Normal'], fontSize=8, leading=10, fontName='Helvetica-Oblique', textColor=COLOR_TEXT_MUTED)
    s_desc = ParagraphStyle('Desc', parent=styles['Normal'], fontSize=9, leading=11, fontName='Helvetica')
    s_bullet = ParagraphStyle('Bullet', parent=s_desc, bulletIndent=0, leftIndent=10, firstLineIndent=0)

    elements = []

    # --- Header ---
    # Layout: Name/Title (Left), Image (Center), Contact (Right)
    # Contact items with icons
    
    contact_flows = []
    for c in PROFILE_DATA['contacts']:
        # Try to load SVG icon
        icon_path = c['icon']
        icon_flow = Spacer(10,10)
        if os.path.exists(icon_path):
            try:
                drawing = svg2rlg(icon_path)
                # Scale down
                scale_factor = 10 / drawing.height
                drawing.width = drawing.width * scale_factor
                drawing.height = drawing.height * scale_factor
                drawing.scale(scale_factor, scale_factor)
                icon_flow = drawing
            except:
                pass
        
        # Row for contact: Text | Icon
        # Note: ReportLab Tables align left by default.
        # We want Text aligned right, then icon.
        row_data = [[Paragraph(c['text'], s_contact), icon_flow]]
        t_contact = Table(row_data, colWidths=[None, 15])
        t_contact.setStyle(TableStyle([
            ('ALIGN', (0,0), (0,0), 'RIGHT'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 1),
            ('TOPPADDING', (0,0), (-1,-1), 1),
        ]))
        contact_flows.append(t_contact)

    # Assemble Header Table
    name_flow = [
        Paragraph(PROFILE_DATA['name'], s_name),
        Paragraph(PROFILE_DATA['title'].replace('\n','<br/>'), s_title)
    ]
    
    image_flow = [CircularImage(PROFILE_DATA['image'], size=100)] # Slightly smaller than CSS 125px to fit
    
    # 3 Columns: 35%, 20%, 45%
    header_data = [[name_flow, image_flow, contact_flows]]
    header_table = Table(header_data, colWidths=[70*mm, 40*mm, 80*mm])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (1,0), (1,0), 'CENTER'), # Image center
        ('ALIGN', (2,0), (2,0), 'RIGHT'),  # Contacts right
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    
    elements.append(header_table)
    elements.append(Spacer(1, 5*mm))
    
    # Divider Line
    # elements.append(Paragraph("<hr/>", s_normal)) # ReportLab paragraph doesn't support hr well like this
    # Use a Table with a bottom border or a drawing
    line_table = Table([[""]], colWidths=[190*mm], rowHeights=[1])
    line_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 1, COLOR_DARK_GREY),
    ]))
    elements.append(line_table)
    elements.append(Spacer(1, 5*mm))

    # --- Main Content (2 Columns) ---
    
    # Left Column Content
    left_content = []
    
    # Education
    left_content.append(Paragraph("EDUCATION", s_header_text))
    for edu in EDUCATION_DATA:
        # Degree (Bold)
        left_content.append(Paragraph(edu['degree'], s_subhead))
        # Institution
        left_content.append(Paragraph(edu['institution'], s_subhead_sm))
        # Meta: Date | CGPA
        left_content.append(Paragraph(f"<font color='{COLOR_TEAL.hexval()}'>{edu['date']}</font>   <font color='{COLOR_TEAL.hexval()}'>{edu['cgpa']}</font>", s_meta))
        # Subject
        # left_content.append(Paragraph("Computer Science", s_meta)) # Hardcoded in data?
        # Details list
        if edu.get('details'):
            for det in edu['details']:
                left_content.append(Paragraph(f"• {det}", s_bullet))
        left_content.append(Spacer(1, 3*mm))

    # Certificates
    left_content.append(Paragraph("CERTIFICATES", s_header_text))
    for cert in CERTIFICATES_DATA:
        left_content.append(Paragraph(cert['title'], s_subhead))
        left_content.append(Paragraph(f"<font color='{COLOR_TEAL.hexval()}'>{cert['date']}</font>", s_meta))
        left_content.append(Paragraph(cert['desc'], s_normal))
        left_content.append(Spacer(1, 3*mm))

    # Languages
    left_content.append(Paragraph("LANGUAGES", s_header_text))
    for lang in LANGUAGES_DATA:
        left_content.append(Paragraph(f"<b>{lang['lang']}</b>", s_normal))
        left_content.append(Paragraph(f"<font color='{COLOR_TEAL.hexval()}'>{lang['level']}</font>", s_meta))
        left_content.append(Spacer(1, 2*mm))

    
    # Right Column Content
    right_content = []
    
    # Skills (Badges)
    right_content.append(Paragraph("SKILLS", s_header_text))
    # Group skills into rows of badges
    skill_badges = []
    current_row = []
    current_width = 0
    max_width = 90 * mm # Approx width of right col
    
    # Simplified: Just flow them as inline text with background? Paragraphs can't do inline bg easily.
    # We will use a Table of badges.
    # Actually, let's just make a flow of Table/Spacer/Table/Spacer...
    # Or cleaner: Just use text bullets for simplicity if badges are too hard, 
    # BUT user wants "that template". Badges are key.
    # Multi-row table.
    
    # Let's try to fit 3 badges per row or adapt.
    # Simple approach: A list of badges wrapped in a logic to break lines.
    # Since I can't easily measure text width in logic without font metrics, 
    # I'll just put 2-3 per row.
    badge_rows = []
    row = []
    for i, skill in enumerate(SKILLS_DATA):
        row.append(create_badge(skill))
        if len(row) >= 2: # 2 per row to be safe
            badge_rows.append(row)
            row = []
    if row:
        badge_rows.append(row)
    
    # Create a table for these rows
    for r in badge_rows:
        # Create a nested table for the row
        t_row = Table([r], colWidths=[None]*len(r))
        t_row.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'TOP')]))
        t_row.hAlign = 'LEFT'
        right_content.append(t_row)
        right_content.append(Spacer(1, 2))
    
    right_content.append(Spacer(1, 3*mm))

    # Experience
    right_content.append(Paragraph("EXPERIENCES", s_header_text))
    for exp in EXPERIENCE_DATA:
        right_content.append(Paragraph(exp['role'], s_subhead))
        right_content.append(Paragraph(exp['company'], s_subhead_sm))
        right_content.append(Paragraph(f"<font color='{COLOR_TEAL.hexval()}'>{exp['date']}</font>", s_meta))
        right_content.append(Paragraph(exp['desc'], s_normal))
        right_content.append(Spacer(1, 3*mm))

    # Projects
    right_content.append(Paragraph("PERSONAL PROJECTS", s_header_text))
    for proj in PROJECTS_DATA:
        right_content.append(Paragraph(proj['title'], s_subhead))
        right_content.append(Paragraph(f"<font color='{COLOR_TEAL.hexval()}'>{proj['date']}</font>", s_meta))
        right_content.append(Paragraph(proj['desc'], s_normal))
        right_content.append(Spacer(1, 3*mm))
        
    # Interests
    right_content.append(Paragraph("INTERESTS", s_header_text))
    # Horizontal list
    int_text = ""
    for interest in INTERESTS_DATA:
         # Create a badge-like look with border? Or just list.
         # Template has badges for interests too.
         pass
    
    # Reuse badge logic for interests
    int_rows = []
    r = []
    for intel in INTERESTS_DATA:
        r.append(create_badge(intel))
    if r:
        t_int = Table([r], colWidths=[None]*len(r))
        t_int.hAlign = 'LEFT'
        right_content.append(t_int)

    # Assemble Two-Column Layout
    # Left Col ~ 45%, Right Col ~ 50%, Gap 5%
    # Total Width 190mm. 
    # Left: 85mm, Right: 95mm, Gap: 10mm
    
    # We need to wrap content in lists to put in a Table cell
    main_data = [[left_content, right_content]]
    main_table = Table(main_data, colWidths=[90*mm, 100*mm])
    main_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('LEFTPADDING', (1,0), (1,0), 5*mm), # Gap implemented as padding on right cell
    ]))
    
    elements.append(main_table)

    doc.build(elements)
    print(f"Generated {FILE_PATH}")

if __name__ == "__main__":
    create_pdf()