import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_TICK_MARK

def create_rich_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Premium Modern Tech Color Palette (Dark Theme)
    BG_DARK = RGBColor(11, 15, 25)         # #0B0F19
    CARD_DARK = RGBColor(22, 31, 48)       # #161F30
    CARD_LIGHT = RGBColor(30, 41, 59)      # #1E293B
    BORDER_DARK = RGBColor(45, 59, 85)     # #2D3B55

    ACCENT_INDIGO = RGBColor(99, 102, 241) # #6366F1
    ACCENT_CYAN = RGBColor(6, 182, 212)    # #06B6D4
    ACCENT_GREEN = RGBColor(16, 185, 129)  # #10B981
    ACCENT_AMBER = RGBColor(245, 158, 11)  # #F59E0B
    ACCENT_ROSE = RGBColor(244, 63, 94)    # #F43F5E
    ACCENT_PURPLE = RGBColor(168, 85, 247) # #A855F7

    TEXT_WHITE = RGBColor(255, 255, 255)
    TEXT_MUTED = RGBColor(148, 163, 184)   # #94A3B8
    TEXT_LIGHT = RGBColor(203, 213, 225)   # #CBD5E1

    def set_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_DARK
        bg.line.fill.background()

        # Top subtle accent bar
        bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.08))
        bar.fill.solid()
        bar.fill.fore_color.rgb = ACCENT_INDIGO
        bar.line.fill.background()
        return bg

    def add_slide_header(slide, title, category, speaker=""):
        # Category Pill
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.35), Inches(2.6), Inches(0.35))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(30, 27, 75)
        pill.line.color.rgb = ACCENT_INDIGO
        tf = pill.text_frame
        p = tf.paragraphs[0]
        p.text = category.upper()
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = ACCENT_CYAN
        p.alignment = PP_ALIGN.CENTER

        # Speaker Tag
        if speaker:
            sp_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.5), Inches(0.35), Inches(2.0), Inches(0.35))
            sp_pill.fill.solid()
            sp_pill.fill.fore_color.rgb = CARD_LIGHT
            sp_pill.line.color.rgb = BORDER_DARK
            sptf = sp_pill.text_frame
            sp = sptf.paragraphs[0]
            sp.text = speaker
            sp.font.size = Pt(10)
            sp.font.bold = True
            sp.font.color.rgb = TEXT_WHITE
            sp.alignment = PP_ALIGN.CENTER

        # Main Title Text
        tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.7))
        tframe = tb.text_frame
        tframe.word_wrap = True
        tp = tframe.paragraphs[0]
        tp.text = title
        tp.font.size = Pt(22)
        tp.font.bold = True
        tp.font.color.rgb = TEXT_WHITE

    def add_metric_card(slide, left, top, width, height, stat_num, stat_label, subtext, accent=ACCENT_INDIGO):
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_DARK
        box.line.color.rgb = accent
        box.line.width = Pt(1.5)

        tf = box.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE

        p1 = tf.paragraphs[0]
        p1.text = stat_num
        p1.font.size = Pt(28)
        p1.font.bold = True
        p1.font.color.rgb = accent
        p1.alignment = PP_ALIGN.CENTER
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = stat_label
        p2.font.size = Pt(11)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.alignment = PP_ALIGN.CENTER

        if subtext:
            p3 = tf.add_paragraph()
            p3.text = subtext
            p3.font.size = Pt(9)
            p3.font.color.rgb = TEXT_MUTED
            p3.alignment = PP_ALIGN.CENTER
        return box

    def add_flow_step(slide, left, top, width, height, step_num, title, desc, accent=ACCENT_INDIGO):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_DARK
        card.line.color.rgb = BORDER_DARK
        card.line.width = Pt(1.2)

        tf = card.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = f"STEP {step_num}"
        p1.font.size = Pt(9)
        p1.font.bold = True
        p1.font.color.rgb = accent
        p1.space_after = Pt(2)

        p2 = tf.add_paragraph()
        p2.text = title
        p2.font.size = Pt(13)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.space_after = Pt(4)

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(10)
        p3.font.color.rgb = TEXT_MUTED
        return card

    # ==========================================
    # SLIDE 1: TITLE SLIDE (Hero Tech Dashboard)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_bg(s1)

    # Hero Badge
    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.9), Inches(3.2), Inches(0.45))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(30, 27, 75)
    badge.line.color.rgb = ACCENT_INDIGO
    btf = badge.text_frame
    bp = btf.paragraphs[0]
    bp.text = "⚡ CSE326 ACADEMIC TASK CA1"
    bp.font.size = Pt(11)
    bp.font.bold = True
    bp.font.color.rgb = ACCENT_CYAN
    bp.alignment = PP_ALIGN.CENTER

    # Main Big Title
    tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.4), Inches(11.3), Inches(2.3))
    t1_f = tb1.text_frame
    t1_f.word_wrap = True

    p = t1_f.paragraphs[0]
    p.text = "HackNova Portal"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = TEXT_WHITE
    p.space_after = Pt(4)

    p2 = t1_f.add_paragraph()
    p2.text = "Hackathon Project Submission & Jury Evaluation Leaderboard"
    p2.font.size = Pt(22)
    p2.font.bold = True
    p2.font.color.rgb = ACCENT_INDIGO
    p2.space_after = Pt(10)

    p3 = t1_f.add_paragraph()
    p3.text = "PROBLEM IN ONE LINE: University hackathons struggle with chaotic submissions, subjective manual jury mark calculations, and a lack of transparent, real-time rankings."
    p3.font.size = Pt(13)
    p3.font.italic = True
    p3.font.color.rgb = TEXT_LIGHT

    # 3 Member Role Cards (Equal Division)
    m_w = Inches(3.6)
    m_h = Inches(2.6)
    m_top = Inches(4.2)

    # Member 1 Card
    c1 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), m_top, m_w, m_h)
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_DARK
    c1.line.color.rgb = ACCENT_CYAN
    c1.line.width = Pt(1.5)
    c1_tf = c1.text_frame
    c1_tf.word_wrap = True
    cp1 = c1_tf.paragraphs[0]
    cp1.text = "MEMBER 1 (PRESENTER 1)"
    cp1.font.bold = True
    cp1.font.size = Pt(10)
    cp1.font.color.rgb = ACCENT_CYAN
    cp1.space_after = Pt(4)
    cp2 = c1_tf.add_paragraph()
    cp2.text = "Student Name 1"
    cp2.font.bold = True
    cp2.font.size = Pt(16)
    cp2.font.color.rgb = TEXT_WHITE
    cp2.space_after = Pt(2)
    cp3 = c1_tf.add_paragraph()
    cp3.text = "Reg No: [XXXXXXX]\n\n• Slides 1-4 (Intro, Problem, Research)\n• Frontend Wireframing & Layout\n• Participant Submission Form & Validation"
    cp3.font.size = Pt(10)
    cp3.font.color.rgb = TEXT_MUTED

    # Member 2 Card
    c2 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.85), m_top, m_w, m_h)
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_DARK
    c2.line.color.rgb = ACCENT_INDIGO
    c2.line.width = Pt(1.5)
    c2_tf = c2.text_frame
    c2_tf.word_wrap = True
    cp1 = c2_tf.paragraphs[0]
    cp1.text = "MEMBER 2 (PRESENTER 2)"
    cp1.font.bold = True
    cp1.font.size = Pt(10)
    cp1.font.color.rgb = ACCENT_INDIGO
    cp1.space_after = Pt(4)
    cp2 = c2_tf.add_paragraph()
    cp2.text = "Student Name 2"
    cp2.font.bold = True
    cp2.font.size = Pt(16)
    cp2.font.color.rgb = TEXT_WHITE
    cp2.space_after = Pt(2)
    cp3 = c2_tf.add_paragraph()
    cp3.text = "Reg No: [XXXXXXX]\n\n• Slides 5-8 (Insights, HMW, Prototype)\n• 4 Standardized Criteria Rubric Sliders\n• Dynamic Judge Cutoff Filter Engine"
    cp3.font.size = Pt(10)
    cp3.font.color.rgb = TEXT_MUTED

    # Member 3 Card
    c3 = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.7), m_top, m_w, m_h)
    c3.fill.solid()
    c3.fill.fore_color.rgb = CARD_DARK
    c3.line.color.rgb = ACCENT_GREEN
    c3.line.width = Pt(1.5)
    c3_tf = c3.text_frame
    c3_tf.word_wrap = True
    cp1 = c3_tf.paragraphs[0]
    cp1.text = "MEMBER 3 (PRESENTER 3)"
    cp1.font.bold = True
    cp1.font.size = Pt(10)
    cp1.font.color.rgb = ACCENT_GREEN
    cp1.space_after = Pt(4)
    cp2 = c3_tf.add_paragraph()
    cp2.text = "Student Name 3"
    cp2.font.bold = True
    cp2.font.size = Pt(16)
    cp2.font.color.rgb = TEXT_WHITE
    cp2.space_after = Pt(2)
    cp3 = c3_tf.add_paragraph()
    cp3.text = "Reg No: [XXXXXXX]\n\n• Slides 9-12 (Testing, Live Demo, NABC)\n• Finalist Project Gallery & Live Podium\n• GitHub Pages Production Deployment"
    cp3.font.size = Pt(10)
    cp3.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 2: THE PROBLEM (Visual Evidence & Flow)
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_bg(s2)
    add_slide_header(s2, "Slide 2: The Problem — Submission Chaos & Evaluation Bottlenecks", "Empathy & Discovery", "Speaker: Member 1")

    # 3 Stat Cards Across Top
    add_metric_card(s2, Inches(0.8), Inches(1.6), Inches(3.7), Inches(1.8), "72%", "Scoring Blindspots", "Participants have zero visibility into marks breakdown", ACCENT_ROSE)
    add_metric_card(s2, Inches(4.8), Inches(1.6), Inches(3.7), Inches(1.8), "45 Min", "Manual Calculation Delays", "Time spent tallying paper sheets & resolving ties", ACCENT_AMBER)
    add_metric_card(s2, Inches(8.8), Inches(1.6), Inches(3.7), Inches(1.8), "1 in 4", "Formula / Tally Errors", "Hackathons experience delayed or disputed results", ACCENT_INDIGO)

    # Process Breakdown Flow Diagram
    add_flow_step(s2, Inches(0.8), Inches(3.7), Inches(2.7), Inches(3.2), "1", "Google Forms Chaos", "Teams submit broken GitHub links, invalid videos, and miss required fields.\nNo instant verification.", ACCENT_ROSE)
    add_flow_step(s2, Inches(3.8), Inches(3.7), Inches(2.7), Inches(3.2), "2", "Paper Rubrics", "Judges grade 40+ teams by hand. Subjective scoring scales vary wildly between judges.", ACCENT_AMBER)
    add_flow_step(s2, Inches(6.8), Inches(3.7), Inches(2.7), Inches(3.2), "3", "Excel Formula Errors", "Coordinators manually type marks into spreadsheets, resulting in calculation mistakes.", ACCENT_PURPLE)
    add_flow_step(s2, Inches(9.8), Inches(3.7), Inches(2.7), Inches(3.2), "4", "Anxious Delays", "Closing ceremonies get delayed while participants wait without knowing rankings.", ACCENT_CYAN)

    # ==========================================
    # SLIDE 3: THE USERS (3 Persona Cards with Quotes)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_bg(s3)
    add_slide_header(s3, "Slide 3: The Users — Personas & Lived Experiences", "User Personas", "Speaker: Member 1")

    # Persona 1
    p1 = slide_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.7), Inches(3.6), Inches(5.2))
    p1.fill.solid()
    p1.fill.fore_color.rgb = CARD_DARK
    p1.line.color.rgb = ACCENT_CYAN
    p1.line.width = Pt(1.5)
    tf1 = p1.text_frame
    tf1.word_wrap = True
    tp = tf1.paragraphs[0]
    tp.text = "🧑‍💻 ARYAN (1st Year CSE)"
    tp.font.bold = True
    tp.font.size = Pt(13)
    tp.font.color.rgb = ACCENT_CYAN
    tp.space_after = Pt(4)
    tp2 = tf1.add_paragraph()
    tp2.text = "Role: Hackathon Participant"
    tp2.font.bold = True
    tp2.font.size = Pt(11)
    tp2.font.color.rgb = TEXT_WHITE
    tp2.space_after = Pt(12)
    tp3 = tf1.add_paragraph()
    tp3.text = "\"We coded for 24 hours non-stop, submitted our repository into a Google Form, and never received any feedback on why our project didn't qualify!\""
    tp3.font.italic = True
    tp3.font.size = Pt(11)
    tp3.font.color.rgb = RGBColor(224, 231, 255)
    tp3.space_after = Pt(14)
    tp4 = tf1.add_paragraph()
    tp4.text = "Core Needs:\n• Instant submission receipt\n• Live review status tracking\n• Standardized transparent feedback"
    tp4.font.size = Pt(10)
    tp4.font.color.rgb = TEXT_MUTED

    # Persona 2
    p2 = slide_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.85), Inches(1.7), Inches(3.6), Inches(5.2))
    p2.fill.solid()
    p2.fill.fore_color.rgb = CARD_DARK
    p2.line.color.rgb = ACCENT_AMBER
    p2.line.width = Pt(1.5)
    tf2 = p2.text_frame
    tf2.word_wrap = True
    tp = tf2.paragraphs[0]
    tp.text = "⚖️ PROF. SHARMA (Faculty)"
    tp.font.bold = True
    tp.font.size = Pt(13)
    tp.font.color.rgb = ACCENT_AMBER
    tp.space_after = Pt(4)
    tp2 = tf2.add_paragraph()
    tp2.text = "Role: Senior Jury Evaluator"
    tp2.font.bold = True
    tp2.font.size = Pt(11)
    tp2.font.color.rgb = TEXT_WHITE
    tp2.space_after = Pt(12)
    tp3 = tf2.add_paragraph()
    tp3.text = "\"Evaluating 40 teams across innovation, code, and UI while doing mental math on paper rubrics is exhausting and prone to calculation mistakes!\""
    tp3.font.italic = True
    tp3.font.size = Pt(11)
    tp3.font.color.rgb = RGBColor(254, 243, 199)
    tp3.space_after = Pt(14)
    tp4 = tf2.add_paragraph()
    tp4.text = "Core Needs:\n• Sliders that auto-sum to 100\n• Screening cutoff controls\n• Direct access to code & pitch videos"
    tp4.font.size = Pt(10)
    tp4.font.color.rgb = TEXT_MUTED

    # Persona 3
    p3 = slide_card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.9), Inches(1.7), Inches(3.6), Inches(5.2))
    p3.fill.solid()
    p3.fill.fore_color.rgb = CARD_DARK
    p3.line.color.rgb = ACCENT_PURPLE
    p3.line.width = Pt(1.5)
    tf3 = p3.text_frame
    tf3.word_wrap = True
    tp = tf3.paragraphs[0]
    tp.text = "🛡️ PRIYA (Student Lead)"
    tp.font.bold = True
    tp.font.size = Pt(13)
    tp.font.color.rgb = ACCENT_PURPLE
    tp.space_after = Pt(4)
    tp2 = tf3.add_paragraph()
    tp2.text = "Role: Event Organizing Coordinator"
    tp2.font.bold = True
    tp2.font.size = Pt(11)
    tp2.font.color.rgb = TEXT_WHITE
    tp2.space_after = Pt(12)
    tp3 = tf3.add_paragraph()
    tp3.text = "\"Manually sorting spreadsheet columns to determine top 3 winners with a hall full of exhausted students waiting creates massive stress!\""
    tp3.font.italic = True
    tp3.font.size = Pt(11)
    tp3.font.color.rgb = RGBColor(243, 232, 255)
    tp3.space_after = Pt(14)
    tp4 = tf3.add_paragraph()
    tp4.text = "Core Needs:\n• Real-time automated leaderboard\n• Instant top 3 podium visualization\n• Simple zero-server hosting"
    tp4.font.size = Pt(10)
    tp4.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 4: RESEARCH & DATA (Native PPT Bar Chart)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_bg(s4)
    add_slide_header(s4, "Slide 4: Field Research — Survey Numbers & User Demand", "Empirical Data", "Speaker: Member 1")

    # Add Native PowerPoint Bar Chart
    chart_data = CategoryChartData()
    chart_data.categories = ['Standard Rubric', 'Finalist Gallery', 'Auto-Sliders', 'Live Rankings']
    chart_data.add_series('Student & Jury Demand (%)', (88, 92, 80, 95))

    chart_shape = s4.shapes.add_chart(
        XL_CHART_TYPE.COLUMN_CLUSTERED,
        Inches(0.8), Inches(1.8), Inches(6.8), Inches(4.9), chart_data
    )
    chart = chart_shape.chart
    chart.has_legend = False
    chart.has_title = True
    chart.chart_title.text_frame.text = "User Survey Demand (40 Students & 5 Faculty Judges)"
    chart.chart_title.text_frame.paragraphs[0].font.size = Pt(12)
    chart.chart_title.text_frame.paragraphs[0].font.color.rgb = TEXT_WHITE

    # Key Findings Side Cards
    f1 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.0), Inches(1.8), Inches(4.5), Inches(2.3))
    f1.fill.solid()
    f1.fill.fore_color.rgb = CARD_DARK
    f1.line.color.rgb = ACCENT_INDIGO
    f1_tf = f1.text_frame
    f1_tf.word_wrap = True
    p1 = f1_tf.paragraphs[0]
    p1.text = "📌 Finding 1: Sliders > Number Typing"
    p1.font.bold = True
    p1.font.size = Pt(13)
    p1.font.color.rgb = ACCENT_INDIGO
    p1.space_after = Pt(4)
    p2 = f1_tf.add_paragraph()
    p2.text = "80% of faculty judges preferred interactive range sliders because it enforces minimum/maximum limits and removes arithmetic errors."
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_LIGHT

    f2 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.0), Inches(4.4), Inches(4.5), Inches(2.3))
    f2.fill.solid()
    f2.fill.fore_color.rgb = CARD_DARK
    f2.line.color.rgb = ACCENT_GREEN
    f2_tf = f2.text_frame
    f2_tf.word_wrap = True
    p1 = f2_tf.paragraphs[0]
    p1.text = "📌 Finding 2: Need for Screening Filter"
    p1.font.bold = True
    p1.font.size = Pt(13)
    p1.font.color.rgb = ACCENT_GREEN
    p1.space_after = Pt(4)
    p2 = f2_tf.add_paragraph()
    p2.text = "92% demanded a dedicated Finalist Gallery, but insisted that low-scoring or unvetted submissions must NOT appear as finalists."
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_LIGHT

    # ==========================================
    # SLIDE 5: THE INSIGHT & POV (Architecture Diagram)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_bg(s5)
    add_slide_header(s5, "Slide 5: The Insight & Point of View (POV) Architecture", "Define Phase", "Speaker: Member 2")

    # Top Insight Banner
    ib = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(1.5))
    ib.fill.solid()
    ib.fill.fore_color.rgb = RGBColor(26, 32, 60)
    ib.line.color.rgb = ACCENT_INDIGO
    ib.line.width = Pt(1.5)
    itf = ib.text_frame
    itf.word_wrap = True
    ip1 = itf.paragraphs[0]
    ip1.text = "💡 THE CORE INSIGHT: Judges Demand Qualification Threshold Control"
    ip1.font.bold = True
    ip1.font.size = Pt(14)
    ip1.font.color.rgb = ACCENT_CYAN
    ip1.space_after = Pt(4)
    ip2 = itf.add_paragraph()
    ip2.text = "Judges did not just want a digital mark sheet—they wanted the authority to set dynamic cutoff criteria so that weak submissions do not dilute the prestige of the Finalist Showcase."
    ip2.font.size = Pt(11)
    ip2.font.color.rgb = TEXT_WHITE

    # Architecture Logic Diagram (Split Funnel)
    # Left Input Box
    in_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.4), Inches(3.2), Inches(3.6))
    in_box.fill.solid()
    in_box.fill.fore_color.rgb = CARD_DARK
    in_box.line.color.rgb = BORDER_DARK
    in_tf = in_box.text_frame
    in_tf.word_wrap = True
    p = in_tf.paragraphs[0]
    p.text = "📥 ALL SUBMISSIONS"
    p.font.bold = True
    p.font.size = Pt(12)
    p.font.color.rgb = ACCENT_CYAN
    p.space_after = Pt(6)
    p2 = in_tf.add_paragraph()
    p2.text = "• Raw student entries\n• GitHub Repo URLs\n• Pitch Demo Videos\n• Tech Stack Tags\n• Team Credentials"
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MUTED

    # Middle Filter Engine
    mid_box = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.5), Inches(3.4), Inches(4.3), Inches(3.6))
    mid_box.fill.solid()
    mid_box.fill.fore_color.rgb = RGBColor(30, 27, 75)
    mid_box.line.color.rgb = ACCENT_INDIGO
    mid_box.line.width = Pt(2)
    m_tf = mid_box.text_frame
    m_tf.word_wrap = True
    p = m_tf.paragraphs[0]
    p.text = "⚙️ JURY QUALIFICATION ENGINE"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_INDIGO
    p.space_after = Pt(6)
    p2 = m_tf.add_paragraph()
    p2.text = "1. Technical Complexity (25 pts)\n2. Innovation & Novelty (25 pts)\n3. UI/UX Usability (25 pts)\n4. Presentation & Feasibility (25 pts)\n\n🎯 Dynamic Judge Cutoff Slider (50–95 pts)\nDetermines finalist eligibility."
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_WHITE

    # Right Qualified / Filtered Box
    out1 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.3), Inches(3.4), Inches(3.2), Inches(1.65))
    out1.fill.solid()
    out1.fill.fore_color.rgb = RGBColor(6, 78, 59)
    out1.line.color.rgb = ACCENT_GREEN
    o1_tf = out1.text_frame
    o1_tf.word_wrap = True
    p = o1_tf.paragraphs[0]
    p.text = "🏅 SCORE ≥ CUTOFF"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = ACCENT_GREEN
    p.space_after = Pt(2)
    p2 = o1_tf.add_paragraph()
    p2.text = "➔ Finalist Project Gallery\n➔ Highlighted on Live Podium"
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_WHITE

    out2 = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.3), Inches(5.35), Inches(3.2), Inches(1.65))
    out2.fill.solid()
    out2.fill.fore_color.rgb = CARD_DARK
    out2.line.color.rgb = ACCENT_AMBER
    o2_tf = out2.text_frame
    o2_tf.word_wrap = True
    p = o2_tf.paragraphs[0]
    p.text = "⏳ SCORE < CUTOFF"
    p.font.bold = True
    p.font.size = Pt(11)
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(2)
    p2 = o2_tf.add_paragraph()
    p2.text = "➔ General Leaderboard Pool\n➔ Excluded from Finalist Gallery"
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 6: THE CHALLENGE (HMW & 3 Pillars)
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_bg(s6)
    add_slide_header(s6, "Slide 6: The Challenge — Main How Might We Question", "Design Challenge", "Speaker: Member 2")

    # Big Central HMW Banner
    hmw_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(1.8))
    hmw_card.fill.solid()
    hmw_card.fill.fore_color.rgb = RGBColor(30, 27, 75)
    hmw_card.line.color.rgb = ACCENT_INDIGO
    hmw_card.line.width = Pt(2)
    h_tf = hmw_card.text_frame
    h_tf.word_wrap = True
    p1 = h_tf.paragraphs[0]
    p1.text = "❓ OUR MAIN 'HOW MIGHT WE' QUESTION"
    p1.font.bold = True
    p1.font.size = Pt(12)
    p1.font.color.rgb = ACCENT_CYAN
    p1.space_after = Pt(4)
    p2 = h_tf.add_paragraph()
    p2.text = "\"How Might We create a zero-setup, responsive frontend application that simplifies project submissions, empowers judges with standardized rubric sliders and cutoff control, and delivers a live, transparent leaderboard?\""
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = TEXT_WHITE

    # 3 Strategic Challenge Pillars
    add_flow_step(s6, Inches(0.8), Inches(3.7), Inches(3.7), Inches(3.2), "Pillar 1", "Frictionless Submissions", "Must capture Team Name, Project Title, Track, GitHub link, Demo video, and Tech Stack with live input validation.", ACCENT_CYAN)
    add_flow_step(s6, Inches(4.8), Inches(3.7), Inches(3.7), Inches(3.2), "Pillar 2", "Objective Rubric Sliders", "Must cap 4 criteria at 25 points each (100 total) and compute live math to eliminate arithmetic mistakes.", ACCENT_INDIGO)
    add_flow_step(s6, Inches(8.8), Inches(3.7), Inches(3.7), Inches(3.2), "Pillar 3", "Dynamic Finalist Filtering", "Must give judges cutoff slider authority to separate verified finalists from low-effort submissions automatically.", ACCENT_GREEN)

    # ==========================================
    # SLIDE 7: IDEATION MATRIX (2x2 Visual Grid)
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_bg(s7)
    add_slide_header(s7, "Slide 7: Your Ideas — 2x2 Impact vs Feasibility Matrix", "Ideation Phase", "Speaker: Member 2")

    # Quadrant 1 (Top Left: High Impact / Low Feasibility) - REJECTED
    q1 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.7), Inches(2.5))
    q1.fill.solid()
    q1.fill.fore_color.rgb = CARD_DARK
    q1.line.color.rgb = ACCENT_ROSE
    q1_tf = q1.text_frame
    q1_tf.word_wrap = True
    p = q1_tf.paragraphs[0]
    p.text = "❌ Full-Stack Node.js / MongoDB App"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_ROSE
    p.space_after = Pt(4)
    p2 = q1_tf.add_paragraph()
    p2.text = "• Impact: High | Feasibility: Low for static deployment\n• Rejected: Requires expensive backend server hosting\n• Server cold-starts cause live demo lags\n• Violates CA1 zero-server static GitHub Pages criteria"
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_MUTED

    # Quadrant 2 (Top Right: High Impact / High Feasibility) - WINNER 🏆
    q2 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(2.5))
    q2.fill.solid()
    q2.fill.fore_color.rgb = RGBColor(26, 32, 60)
    q2.line.color.rgb = ACCENT_GREEN
    q2.line.width = Pt(2)
    q2_tf = q2.text_frame
    q2_tf.word_wrap = True
    p = q2_tf.paragraphs[0]
    p.text = "🏆 WINNER: HackNova Client-Side Architecture"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = ACCENT_GREEN
    p.space_after = Pt(4)
    p2 = q2_tf.add_paragraph()
    p2.text = "• Pure HTML5 + CSS3 + Vanilla JavaScript ES6\n• Browser LocalStorage preserves all submissions & marks\n• Instant 100% free deployment on GitHub Pages\n• Zero server latency, instant response, easy to explain in Viva!"
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_WHITE

    # Quadrant 3 (Bottom Left: Low Impact / Low Feasibility) - REJECTED
    q3 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.3), Inches(5.7), Inches(2.5))
    q3.fill.solid()
    q3.fill.fore_color.rgb = CARD_DARK
    q3.line.color.rgb = BORDER_DARK
    q3_tf = q3.text_frame
    q3_tf.word_wrap = True
    p = q3_tf.paragraphs[0]
    p.text = "❌ Mobile APK App (Flutter/React Native)"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = TEXT_MUTED
    p.space_after = Pt(4)
    p2 = q3_tf.add_paragraph()
    p2.text = "• Impact: Medium | Feasibility: Low\n• Rejected: Requires judges to install third-party APKs\n• Evaluators on desktop cannot review comfortably\n• Cannot be opened via simple URL"
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_MUTED

    # Quadrant 4 (Bottom Right: Low Impact / High Feasibility) - REJECTED
    q4 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(4.3), Inches(5.7), Inches(2.5))
    q4.fill.solid()
    q4.fill.fore_color.rgb = CARD_DARK
    q4.line.color.rgb = ACCENT_AMBER
    q4_tf = q4.text_frame
    q4_tf.word_wrap = True
    p = q4_tf.paragraphs[0]
    p.text = "❌ Google Forms + Google Sheets Script"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(4)
    p2 = q4_tf.add_paragraph()
    p2.text = "• Impact: Low | Feasibility: High\n• Rejected: Ugly user interface, no branding\n• Formula tampering risks by participants\n• No visual podium or interactive scoring sliders"
    p2.font.size = Pt(10)
    p2.font.color.rgb = TEXT_MUTED

    # ==========================================
    # SLIDE 8: THE PROTOTYPE (Pipeline Evolution)
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_bg(s8)
    add_slide_header(s8, "Slide 8: The Prototype — Evolutionary Development Pipeline", "Prototype Journey", "Speaker: Member 2")

    p_w = Inches(2.7)
    p_h = Inches(5.0)

    # Stage 1
    add_flow_step(s8, Inches(0.8), Inches(1.8), p_w, p_h, "1", "Paper Wireframes",
                  "• Rough pen sketches\n• Basic input fields identified\n• Simple table layout\n• Missing: Role separation, validation", ACCENT_ROSE)

    # Stage 2
    add_flow_step(s8, Inches(3.8), Inches(1.8), p_w, p_h, "2", "Semantic HTML",
                  "• Form & table tags written\n• CSS Grid layout added\n• Responsive styling begun\n• Missing: Multi-role dashboards, dynamic sliders", ACCENT_AMBER)

    # Stage 3
    add_flow_step(s8, Inches(6.8), Inches(1.8), p_w, p_h, "3", "Role Navigation",
                  "• Participant, Judge, Admin views\n• 1-Click demo logins added\n• LocalStorage persistence\n• Missing: Screening cutoff criteria", ACCENT_INDIGO)

    # Stage 4
    add_flow_step(s8, Inches(9.8), Inches(1.8), p_w, p_h, "4", "High-Fidelity",
                  "• 4 Criteria rubric sliders\n• Dynamic Judge cutoff (50-95)\n• Finalist Project Gallery\n• Top 3 Gold/Silver/Bronze Podium", ACCENT_GREEN)

    # ==========================================
    # SLIDE 9: TESTING (Feedback Matrix)
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_bg(s9)
    add_slide_header(s9, "Slide 9: Testing — User Actions & Feedback Matrix", "User Testing", "Speaker: Member 3")

    # Left: What Users Did
    t_left = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    t_left.fill.solid()
    t_left.fill.fore_color.rgb = CARD_DARK
    t_left.line.color.rgb = ACCENT_INDIGO
    tl_tf = t_left.text_frame
    tl_tf.word_wrap = True
    p = tl_tf.paragraphs[0]
    p.text = "🧪 User Testing Scenario & Tasks"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_INDIGO
    p.space_after = Pt(8)
    p2 = tl_tf.add_paragraph()
    p2.text = "• Tested with: 6 classmates & 2 senior mentors.\n\n• Task 1: Register a new project with GitHub repo, live demo URL, and tech tags.\n➔ Result: 100% completed under 45 seconds.\n\n• Task 2: Open Jury scorecard and grade using sliders.\n➔ Result: Evaluators loved live total score computation.\n\n• Task 3: Switch roles via 1-Click Demo buttons.\n➔ Result: Role switching was seamless without password delays."
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_LIGHT

    # Right: Feedback Matrix
    t_right = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    t_right.fill.solid()
    t_right.fill.fore_color.rgb = CARD_DARK
    t_right.line.color.rgb = ACCENT_AMBER
    tr_tf = t_right.text_frame
    tr_tf.word_wrap = True
    p = tr_tf.paragraphs[0]
    p.text = "📋 User Feedback Matrix"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_AMBER
    p.space_after = Pt(8)
    p2 = tr_tf.add_paragraph()
    p2.text = "👍 Praise Received:\n• \"Auto-calculating total score eliminates cognitive arithmetic load.\"\n• \"Podium visual makes the awards announcement thrilling!\"\n\n⚠️ Critical User Pushback:\n• \"If all submitted projects show up in the Finalist Gallery, it ruins the standard! Some teams barely coded.\"\n\n💡 Actionable Iteration:\n• We must create an automated cutoff filter controlled by the Judge!"
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_LIGHT

    # ==========================================
    # SLIDE 10: WHAT CHANGED (Before vs After)
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    set_bg(s10)
    add_slide_header(s10, "Slide 10: What Changed — Before & After User Iterations", "Iteration Matrix", "Speaker: Member 3")

    # Before Card (Red border)
    b_card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
    b_card.fill.solid()
    b_card.fill.fore_color.rgb = CARD_DARK
    b_card.line.color.rgb = ACCENT_ROSE
    b_card.line.width = Pt(1.5)
    b_tf = b_card.text_frame
    b_tf.word_wrap = True
    p = b_tf.paragraphs[0]
    p.text = "⏮️ BEFORE Iteration (Initial Draft)"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = ACCENT_ROSE
    p.space_after = Pt(10)
    p2 = b_tf.add_paragraph()
    p2.text = "1. Unfiltered Finalist Gallery:\nEvery submitted project immediately appeared in the showcase.\n\n2. Fixed Assumptions:\nNo control for judges to raise or lower qualification standards.\n\n3. Auto-Login Glitch:\nBrowser remembered previous sessions and skipped the welcome login card.\n\n4. Raw User Input:\nRisk of XSS script injection from user-typed project titles."
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_MUTED

    # After Card (Green border)
    a_card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
    a_card.fill.solid()
    a_card.fill.fore_color.rgb = RGBColor(26, 32, 60)
    a_card.line.color.rgb = ACCENT_GREEN
    a_card.line.width = Pt(2)
    a_tf = a_card.text_frame
    a_tf.word_wrap = True
    p = a_tf.paragraphs[0]
    p.text = "⏭️ AFTER Iteration (Final HackNova)"
    p.font.bold = True
    p.font.size = Pt(14)
    p.font.color.rgb = ACCENT_GREEN
    p.space_after = Pt(10)
    p2 = a_tf.add_paragraph()
    p2.text = "1. Filtered Finalist Showcase:\nOnly submissions evaluated and approved with score >= cutoff appear.\n\n2. Dynamic Judge Cutoff Slider (50–95 pts):\nJury panel controls the qualification benchmark live.\n\n3. Clean Startup Flow:\nPortal always launches on the Welcome / Login card first.\n\n4. Security Sanitization:\nImplemented escapeHTML() to neutralize all user input risks."
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_WHITE

    # ==========================================
    # SLIDE 11: FINAL SOLUTION & LIVE DEMO
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    set_bg(s11)
    add_slide_header(s11, "Slide 11: Final Solution — Architecture & Live Walkthrough", "Live Verification", "Speaker: Member 3")

    # Workflow Visual Cards Across Top
    add_flow_step(s11, Inches(0.8), Inches(1.7), Inches(2.7), Inches(2.4), "Module 1", "Participant Zone", "Project registration with live repo/demo video validation.", ACCENT_CYAN)
    add_flow_step(s11, Inches(3.8), Inches(1.7), Inches(2.7), Inches(2.4), "Module 2", "Jury Scorecard", "4 criteria sliders (0-25) + Judge Cutoff slider.", ACCENT_INDIGO)
    add_flow_step(s11, Inches(6.8), Inches(1.7), Inches(2.7), Inches(2.4), "Module 3", "Finalist Gallery", "Card grid with tech tags & direct GitHub/demo buttons.", ACCENT_AMBER)
    add_flow_step(s11, Inches(9.8), Inches(1.7), Inches(2.7), Inches(2.4), "Module 4", "Live Leaderboard", "Descending .sort() algorithm with Top 3 Podium.", ACCENT_GREEN)

    # Bottom Live Demo Banner
    demo_box = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.4), Inches(11.7), Inches(2.4))
    demo_box.fill.solid()
    demo_box.fill.fore_color.rgb = RGBColor(30, 27, 75)
    demo_box.line.color.rgb = ACCENT_INDIGO
    demo_box.line.width = Pt(2)
    d_tf = demo_box.text_frame
    d_tf.word_wrap = True
    p1 = d_tf.paragraphs[0]
    p1.text = "🚀 LIVE DEPLOYED WEB APPLICATION DEMONSTRATION"
    p1.font.bold = True
    p1.font.size = Pt(14)
    p1.font.color.rgb = ACCENT_CYAN
    p1.space_after = Pt(6)
    p2 = d_tf.add_paragraph()
    p2.text = "• Live Deployed URL: https://abhinandankumar802103.github.io/CSE326/\n• GitHub Source Code: https://github.com/abhinandankumar802103/CSE326\n\nWalkthrough Highlights for Video:\n1. 1-Click Login ➔ 2. Participant Submission ➔ 3. Jury Sliders Scoring ➔ 4. Cutoff Filtering ➔ 5. Live Podium Ranking"
    p2.font.size = Pt(11)
    p2.font.color.rgb = TEXT_WHITE

    # ==========================================
    # SLIDE 12: REFLECTION & NABC CLOSE
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    set_bg(s12)
    add_slide_header(s12, "Slide 12: Honest Reflection, Roadmap & NABC Framework", "Conclusion", "Speaker: Member 3")

    # NABC 4 Quadrants
    nb_w = Inches(2.7)
    nb_h = Inches(4.8)

    add_flow_step(s12, Inches(0.8), Inches(1.8), nb_w, nb_h, "N", "NEED",
                  "• University hackathons need transparent, zero-error scoring.\n\n• Students want visibility into marks.\n\n• Faculty need fast, automated tallying.", ACCENT_ROSE)
    add_flow_step(s12, Inches(3.8), Inches(1.8), nb_w, nb_h, "A", "APPROACH",
                  "• Responsive client-side web app.\n\n• Standardized 4-criteria rubric sliders.\n\n• Dynamic cutoff filter & real-time leaderboard.\n\n• Free GitHub Pages hosting.", ACCENT_CYAN)
    add_flow_step(s12, Inches(6.8), Inches(1.8), nb_w, nb_h, "B", "BENEFIT",
                  "• 100% automated score calculation.\n\n• Zero mental math or spreadsheet formula errors.\n\n• Public portfolio showcase for finalists.", ACCENT_GREEN)
    add_flow_step(s12, Inches(9.8), Inches(1.8), nb_w, nb_h, "C", "COMPETITION",
                  "• Far superior to Google Forms & Excel spreadsheets.\n\n• No paid backend server costs.\n\n• 3x faster evaluation turnaround time.", ACCENT_AMBER)

    # Save presentation
    output_path = "HackNova_Official_Presentation.pptx"
    prs.save(output_path)
    print("SUCCESS: Rich presentation created and saved to " + output_path)

    # Also try saving to the original filename if not locked
    try:
        prs.save("HackNova_Presentation.pptx")
        print("SUCCESS: Also updated HackNova_Presentation.pptx")
    except Exception as e:
        print("Note: HackNova_Presentation.pptx is currently open in PowerPoint; saved as HackNova_Official_Presentation.pptx")

if __name__ == "__main__":
    create_rich_presentation()
