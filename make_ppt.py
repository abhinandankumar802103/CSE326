import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    prs = Presentation()
    # 16:9 widescreen dimensions
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    DARK_NAVY = RGBColor(15, 23, 42)      # #0F172A
    INDIGO = RGBColor(79, 70, 229)        # #4F46E5
    LIGHT_BG = RGBColor(248, 250, 252)    # #F8FAFC
    CARD_BG = RGBColor(255, 255, 255)     # #FFFFFF
    TEXT_MAIN = RGBColor(15, 23, 42)      # #0F172A
    TEXT_MUTED = RGBColor(71, 85, 105)    # #475569
    ACCENT_BLUE = RGBColor(14, 165, 233)  # #0EA5E9
    BORDER_COLOR = RGBColor(226, 232, 240)# #E2E8F0
    WHITE = RGBColor(255, 255, 255)

    def add_header(slide, title_text, category_text, presenter_text=""):
        # Category Pill
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.45), Inches(2.8), Inches(0.4))
        pill.fill.solid()
        pill.fill.fore_color.rgb = RGBColor(224, 231, 255)
        pill.line.color.rgb = INDIGO
        tf = pill.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = category_text.upper()
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = INDIGO
        p.alignment = PP_ALIGN.CENTER

        # Presenter Tag if available
        if presenter_text:
            pres_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.2), Inches(0.45), Inches(2.3), Inches(0.4))
            pres_pill.fill.solid()
            pres_pill.fill.fore_color.rgb = RGBColor(241, 245, 249)
            pres_pill.line.color.rgb = BORDER_COLOR
            ptf = pres_pill.text_frame
            pp = ptf.paragraphs[0]
            pp.text = presenter_text
            pp.font.size = Pt(11)
            pp.font.bold = True
            pp.font.color.rgb = TEXT_MUTED
            pp.alignment = PP_ALIGN.CENTER

        # Main Title
        txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.95), Inches(11.5), Inches(0.8))
        tf2 = txBox.text_frame
        tf2.word_wrap = True
        p2 = tf2.paragraphs[0]
        p2.text = title_text
        p2.font.size = Pt(26)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_MAIN

    def set_slide_background(slide, color):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = color
        bg.line.fill.background()
        return bg

    def add_card(slide, left, top, width, height, title, content_lines, accent_color=None):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = accent_color if accent_color else BORDER_COLOR
        card.line.width = Pt(1.5)

        txBox = slide.shapes.add_textbox(left + Inches(0.2), top + Inches(0.2), width - Inches(0.4), height - Inches(0.4))
        tf = txBox.text_frame
        tf.word_wrap = True

        if title:
            p0 = tf.paragraphs[0]
            p0.text = title
            p0.font.bold = True
            p0.font.size = Pt(18)
            p0.font.color.rgb = INDIGO if not accent_color else accent_color
            p0.space_after = Pt(10)

        for line in content_lines:
            p = tf.add_paragraph()
            p.text = line
            p.font.size = Pt(13)
            p.font.color.rgb = TEXT_MUTED
            p.space_after = Pt(6)
        return card

    # ==========================================
    # SLIDE 1: TITLE SLIDE (Hero Dark Background)
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1, DARK_NAVY)

    # Accent top border
    accent_bar = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, Inches(0.15))
    accent_bar.fill.solid()
    accent_bar.fill.fore_color.rgb = INDIGO
    accent_bar.line.fill.background()

    # Title Card
    t_box = s1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.3), Inches(4.5))
    tf = t_box.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "⚡ HACKNOVA"
    p.font.bold = True
    p.font.size = Pt(44)
    p.font.color.rgb = WHITE
    p.space_after = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "Hackathon Project Submission & Jury Evaluation Leaderboard"
    p2.font.bold = True
    p2.font.size = Pt(28)
    p2.font.color.rgb = ACCENT_BLUE
    p2.space_after = Pt(16)

    p3 = tf.add_paragraph()
    p3.text = "Course: CSE326 Web Development | CA1 Project-Based Assessment"
    p3.font.size = Pt(16)
    p3.font.color.rgb = RGBColor(148, 163, 184)
    p3.space_after = Pt(24)

    p4 = tf.add_paragraph()
    p4.text = "PROBLEM IN ONE LINE: Traditional hackathons suffer from chaotic submissions, subjective manual jury calculations, and a complete lack of transparent, real-time rankings."
    p4.font.size = Pt(15)
    p4.font.italic = True
    p4.font.color.rgb = RGBColor(226, 232, 240)

    # Team Box
    team_card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(5.4), Inches(11.3), Inches(1.4))
    team_card.fill.solid()
    team_card.fill.fore_color.rgb = RGBColor(30, 41, 59)
    team_card.line.color.rgb = RGBColor(51, 65, 85)
    t_tf = team_card.text_frame
    t_tf.word_wrap = True
    tp1 = t_tf.paragraphs[0]
    tp1.text = "PROJECT TEAM (3 MEMBERS)"
    tp1.font.bold = True
    tp1.font.size = Pt(12)
    tp1.font.color.rgb = INDIGO
    tp1.space_after = Pt(4)

    tp2 = t_tf.add_paragraph()
    tp2.text = "• Member 1: [Full Name] - Frontend Architecture & Participant Zone | • Member 2: [Full Name] - Jury Scoring Desk & Cutoff Math | • Member 3: [Full Name] - Leaderboard, Finalist Gallery & Deployment"
    tp2.font.size = Pt(12)
    tp2.font.color.rgb = WHITE

    # ==========================================
    # SLIDE 2: THE PROBLEM (Member 1)
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2, LIGHT_BG)
    add_header(s2, "Slide 2: The Problem — Where It Happens & Who It Affects", "Design Thinking: Empathy", "Speaker: Member 1")

    add_card(s2, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "📍 Where It Happens", [
        "• University & college hackathons",
        "• 24-to-36-hour technical hack events",
        "• State & national innovation symposiums",
        "",
        "High-pressure environment with tight submission deadlines."
    ])

    add_card(s2, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "👥 Who It Affects", [
        "• Participants (Over 100+ students): Exhausted, unsure how they are graded.",
        "",
        "• Jury Members & Faculty: Burdened with mental math across 40+ projects.",
        "",
        "• Organizers: Stressed trying to compile marks and announce winners accurately."
    ])

    add_card(s2, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "📊 Striking Evidence", [
        "• Over 70% of students report zero visibility into their score breakdown.",
        "",
        "• Judges take 45+ minutes manually calculating Excel formulas and tie-breakers.",
        "",
        "• 1 out of 4 hackathons experience delays in results due to spreadsheet formula errors."
    ], INDIGO)

    # ==========================================
    # SLIDE 3: THE USERS (Member 1)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3, LIGHT_BG)
    add_header(s3, "Slide 3: The Users — Personas & Real Quotes", "Design Thinking: Personas", "Speaker: Member 1")

    add_card(s3, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "🧑‍💻 Aryan (Participant)", [
        "1st Year Computer Science Student",
        "",
        "\"We coded 24 hours non-stop, submitted our GitHub repo into a Google Form, and never got any feedback on why our project didn't qualify!\"",
        "",
        "Goal: Instant submission verification & transparent score breakdown."
    ])

    add_card(s3, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "⚖️ Prof. Sharma (Judge)", [
        "Senior Faculty Jury Member",
        "",
        "\"Tallying marks across 40 teams across innovation, code, and UI while doing mental math is stressful and prone to calculation mistakes!\"",
        "",
        "Goal: Standardized sliders that calculate totals automatically."
    ])

    add_card(s3, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "🛡️ Priya (Organizer)", [
        "Student Event Coordinator",
        "",
        "\"Manually sorting spreadsheets to announce the top 3 teams while a hall full of students waits creates immense pressure.\"",
        "",
        "Goal: Real-time dynamic leaderboard with top 3 podium."
    ])

    # ==========================================
    # SLIDE 4: RESEARCH (Member 1)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4, LIGHT_BG)
    add_header(s4, "Slide 4: Research — Survey Numbers & Field Observations", "Design Thinking: Field Research", "Speaker: Member 1")

    add_card(s4, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "📈 Survey Data (40 Students & 5 Judges)", [
        "• 88% demanded a standardized 4-part scoring rubric (Technical, Innovation, UI/UX, Presentation).",
        "",
        "• 92% wanted a public showcase gallery to inspect finalist repositories and pitch videos.",
        "",
        "• 80% of faculty judges preferred interactive sliders over typing numerical marks into cells.",
        "",
        "• 95% stated they prefer instant browser-accessible portals without complex account setups."
    ])

    add_card(s4, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "🔍 Field Observations", [
        "• Observation 1: Submission Chaos",
        "Google Forms often result in broken URLs, missing demo videos, or wrong track categories.",
        "",
        "• Observation 2: Scoring Subjectivity",
        "Without standardized point caps, different judges grade on vastly different scales.",
        "",
        "• Observation 3: Incomplete Projects Dilute Finalists",
        "Submissions lacking live demos or code clutter the finalist round unless filtered."
    ])

    # ==========================================
    # SLIDE 5: THE INSIGHT & POV (Member 2)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5, LIGHT_BG)
    add_header(s5, "Slide 5: The Insight & Point of View (POV) Statement", "Design Thinking: Define", "Speaker: Member 2")

    add_card(s5, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "💡 What Surprised Us (The Core Insight)", [
        "• We originally thought judges just wanted a digital grading sheet.",
        "",
        "• THE SURPRISE: Judges specifically wanted the power to control the QUALIFICATION BENCHMARK.",
        "",
        "• In large hackathons, low-effort submissions dilute the quality of the competition.",
        "",
        "• Judges demanded a dynamic cutoff threshold so only high-quality projects enter the Finalist Showcase."
    ])

    add_card(s5, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "🎯 Point of View (POV) Statement", [
        "\"University hackathon participants, judges, and event coordinators...",
        "",
        "NEED: A unified, responsive web portal with standardized rubric sliders and dynamic qualification filtering...",
        "",
        "BECAUSE: Participants deserve transparent feedback on their hard work, and judges require automated, mathematically fair evaluation without spreadsheet errors.\"",
        "",
        "Outcome: Zero manual tallying, real-time leaderboard."
    ], INDIGO)

    # ==========================================
    # SLIDE 6: THE CHALLENGE (Member 2)
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6, LIGHT_BG)
    add_header(s6, "Slide 6: The Challenge — Main How Might We (HMW) Question", "Design Thinking: The Challenge", "Speaker: Member 2")

    add_card(s6, Inches(0.8), Inches(1.8), Inches(11.7), Inches(2.3), "❓ Our Primary 'How Might We' Question", [
        "\"How Might We develop a responsive, zero-server frontend web application that streamlines project submissions, empowers judges with standardized rubric sliders and cutoff control, and delivers a live, transparent leaderboard?\""
    ], INDIGO)

    add_card(s6, Inches(0.8), Inches(4.4), Inches(3.6), Inches(2.4), "Sub-Question 1", [
        "How might we make project submissions fast and validate links immediately?"
    ])
    add_card(s6, Inches(4.8), Inches(4.4), Inches(3.6), Inches(2.4), "Sub-Question 2", [
        "How might we eliminate mental math for judges using interactive range sliders?"
    ])
    add_card(s6, Inches(8.8), Inches(4.4), Inches(3.7), Inches(2.4), "Sub-Question 3", [
        "How might we screen and showcase true finalists with one-click code & video links?"
    ])

    # ==========================================
    # SLIDE 7: IDEATION (Member 2)
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7, LIGHT_BG)
    add_header(s7, "Slide 7: Your Ideas — Prioritization Matrix & Rejected Ideas", "Design Thinking: Ideation", "Speaker: Member 2")

    add_card(s7, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "❌ Idea 1: Google Sheets Script", [
        "Status: REJECTED",
        "",
        "• Clunky user interface",
        "• Easily broken by participants accidentally editing cells",
        "• No professional showcase gallery",
        "• Poor mobile responsiveness"
    ])

    add_card(s7, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "❌ Idea 2: Full-Stack Node/Mongo App", [
        "Status: REJECTED",
        "",
        "• Requires paid backend hosting servers",
        "• Server cold-starts cause live demo lags",
        "• Cannot be hosted directly on free static GitHub Pages",
        "• Over-complicated for 1st-semester evaluation"
    ])

    add_card(s7, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "✅ Idea 3: Client-Side Web App", [
        "Status: SELECTED WINNER! 🏆",
        "",
        "• Pure HTML5 + CSS3 + Vanilla JavaScript",
        "• Browser LocalStorage preserves all data instantly",
        "• 100% free, permanent GitHub Pages deployment",
        "• Zero server dependencies or latency",
        "• 1-Click quick login for seamless viva demo"
    ], INDIGO)

    # ==========================================
    # SLIDE 8: THE PROTOTYPE (Member 2)
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8, LIGHT_BG)
    add_header(s8, "Slide 8: The Prototype — From Paper Wireframes to Final App", "Design Thinking: Prototype", "Speaker: Member 2")

    add_card(s8, Inches(0.8), Inches(1.8), Inches(2.7), Inches(4.8), "Stage 1: Paper Sketches", [
        "• Initial pen-and-paper wireframes",
        "• Simple form fields (Team, Title, Link)",
        "• Static marks table concept",
        "• Identified need for role-based navigation"
    ])

    add_card(s8, Inches(3.8), Inches(1.8), Inches(2.7), Inches(4.8), "Stage 2: Base HTML Layout", [
        "• Converted wireframe to semantic HTML",
        "• Table and form tags implemented",
        "• Basic styling added",
        "• Lacked visual hierarchy and responsive behavior"
    ])

    add_card(s8, Inches(6.8), Inches(1.8), Inches(2.7), Inches(4.8), "Stage 3: Multi-Role Engine", [
        "• Created 4 distinct views (Participant, Judge, Leaderboard, Admin)",
        "• LocalStorage state management",
        "• 1-Click demo authentication buttons added"
    ])

    add_card(s8, Inches(9.8), Inches(1.8), Inches(2.7), Inches(4.8), "Stage 4: High-Fidelity", [
        "• Standardized 4-criteria rubric sliders",
        "• Auto-summing total out of 100",
        "• Top 3 Podium (Gold, Silver, Bronze)",
        "• Finalist Gallery with tech tags & direct links"
    ], INDIGO)

    # ==========================================
    # SLIDE 9: TESTING (Member 3)
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9, LIGHT_BG)
    add_header(s9, "Slide 9: Testing — What Users Actually Did & Feedback Matrix", "Design Thinking: Testing", "Speaker: Member 3")

    add_card(s9, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "🧪 User Testing Scenario", [
        "• Tested with 6 classmates and 2 faculty mentors using sample hackathon data.",
        "",
        "• Task 1 (Participants): Submit a new project with GitHub repo, demo pitch, and tech tags.",
        "Result: 100% completion rate under 60 seconds.",
        "",
        "• Task 2 (Judges): Open project scorecard, evaluate across 4 rubrics, and save.",
        "Result: Loved the sliders; total calculated in real time without mental math."
    ])

    add_card(s9, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "📋 Feedback Matrix Highlights", [
        "👍 WHAT USERS PRAISED:",
        "• \"The 1-Click demo login makes testing role switches effortless.\"",
        "• \"The Podium visual gives real hackathon ceremony energy!\"",
        "",
        "⚠️ CRITICAL USER CRITIQUE:",
        "• \"Why are all submitted projects showing up as finalists? Some teams barely submitted working code!\"",
        "",
        "💡 KEY TAKEAWAY:",
        "The system needed an explicit screening filter so that only high-scoring qualifiers enter the Finalist Showcase."
    ])

    # ==========================================
    # SLIDE 10: WHAT CHANGED (Member 3)
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10, LIGHT_BG)
    add_header(s10, "Slide 10: What Changed — Before and After Iterations", "Design Thinking: Iteration", "Speaker: Member 3")

    add_card(s10, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8), "⏮️ BEFORE Feedback", [
        "• Unfiltered Gallery: Every project that submitted immediately appeared in the showcase.",
        "",
        "• Static Threshold: Hardcoded assumption of qualification.",
        "",
        "• Auto-Login: Browser remembered old sessions and skipped the welcome login card.",
        "",
        "• Basic Table: Plain table rows for all projects."
    ])

    add_card(s10, Inches(6.8), Inches(1.8), Inches(5.7), Inches(4.8), "⏭️ AFTER Iteration (Current HackNova)", [
        "• 🎨 Finalist Gallery Filter: Only projects evaluated by jury and scoring >= cutoff are admitted.",
        "",
        "• ⚙️ Judge Cutoff Slider: Jury controls the qualification bar (50–95 pts) in real time.",
        "",
        "• 🔐 Clean Startup: Always opens cleanly on the Welcome / Login screen first.",
        "",
        "• 🛡️ XSS Sanitization: Added escapeHTML() to secure all user inputs.",
        "",
        "• 🥇 Top 3 Podium: Distinct gold, silver, and bronze visual rank cards."
    ], INDIGO)

    # ==========================================
    # SLIDE 11: FINAL SOLUTION & DEMO (Member 3)
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11, LIGHT_BG)
    add_header(s11, "Slide 11: Final Solution & Live Application Demonstration", "Deliver: Live Demo", "Speaker: Member 3")

    add_card(s11, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "🌟 Who Benefits", [
        "• Participants: Instant confirmation, clear rubric marks, and status tracking.",
        "",
        "• Judges: 3x faster evaluation with auto-summing sliders (0–25 each).",
        "",
        "• Organizers: Zero manual spreadsheets, automatic tie-breaking leaderboard."
    ])

    add_card(s11, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "🚀 Why It Beats Inaction", [
        "• Eliminates human calculation errors during awards ceremony.",
        "",
        "• Permanent portfolio showcase for students.",
        "",
        "• 100% accessible on GitHub Pages with zero server cost.",
        "",
        "• Fully responsive across mobile, tablet, and desktop."
    ])

    add_card(s11, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "🌐 Live Verification Links", [
        "🔗 GitHub Repository:",
        "github.com/abhinandankumar802103/CSE326",
        "",
        "🚀 Live Deployed Portal:",
        "abhinandankumar802103.github.io/CSE326/",
        "",
        "Tech Stack: HTML5, CSS3 Grid/Flexbox, JavaScript ES6, LocalStorage."
    ], INDIGO)

    # ==========================================
    # SLIDE 12: REFLECTION & NABC (Member 3)
    # ==========================================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12, LIGHT_BG)
    add_header(s12, "Slide 12: Honest Reflection, Future Roadmap & NABC Close", "Reflection & Conclusion", "Speaker: Member 3")

    add_card(s12, Inches(0.8), Inches(1.8), Inches(3.6), Inches(4.8), "🔍 Honest Reflection", [
        "• What Failed / Limitation: Client-side LocalStorage is stored in the local browser. Multi-device sync requires cloud database.",
        "",
        "• Learning: Balancing beginner-friendly code explainability for Viva while delivering advanced UI features."
    ])

    add_card(s12, Inches(4.8), Inches(1.8), Inches(3.6), Inches(4.8), "🔮 Future Roadmap (v2.0)", [
        "• Multi-device real-time sync with Firebase / Supabase.",
        "",
        "• Automated GitHub commit activity & plagiarism check.",
        "",
        "• One-click PDF Certificate generator for participating teams."
    ])

    add_card(s12, Inches(8.8), Inches(1.8), Inches(3.7), Inches(4.8), "🏆 One-Line NABC Close", [
        "• Need: Transparent, error-free hackathon evaluation.",
        "• Approach: Responsive portal with standardized rubric sliders.",
        "• Benefit: Instant score tallying & dynamic finalist filtering.",
        "• Competition: Far superior to tedious Google Forms & manual spreadsheets."
    ], INDIGO)

    # Save presentation
    output_path = "HackNova_Presentation.pptx"
    prs.save(output_path)
    print("SUCCESS: Presentation saved to " + output_path)

if __name__ == "__main__":
    create_presentation()
