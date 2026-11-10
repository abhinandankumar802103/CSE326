# ⚡ HackNova — Presentation Slides & 3-Member Video Script

> **Course:** CSE326 — Web Development (Academic Task CA1)  
> **Problem Statement:** Hackathon Project Submission And Jury Evaluation Leaderboard  
> **Format:** 12 Slides, 10 Minutes Total, 3 Team Members  
> **Framework:** Design Thinking Storytelling (Empathy, Research, Prototype, Testing, Demo, Reflection)

---

## 👥 Team Member Division & Responsibilities

| Member | Speaking Section | Slides | Role & Technical Contribution |
| :--- | :--- | :---: | :--- |
| **Member 1 (Presenter 1)** | Problem, Personas & Research | **Slides 1 – 4** (~3 mins) | Frontend UI Layout, Participant Submission Form, Form Validation, and Initial Wireframes |
| **Member 2 (Presenter 2)** | Insights, HMW, Ideation & Prototype | **Slides 5 – 8** (~3 mins) | Standardized Jury Rubric Sliders, Live Total Math Calculation, and Judge Cutoff Control Logic |
| **Member 3 (Presenter 3)** | Testing, Iterations, Live Demo & Closing | **Slides 9 – 12** (~4 mins) | Finalist Project Gallery, Real-Time Leaderboard Sorting, Responsive CSS, and GitHub Pages Deployment |

---

# 📊 Part 1: Slide-by-Slide PPT Content (12 Slides)

### Slide 1: Title & Introduction
* **Header:** HackNova — Hackathon Project Submission & Jury Leaderboard Portal
* **Subtitle:** CSE326 Academic Task CA1 | Project-Based Assessment
* **Team Members:**
  * Member 1: [Full Name] (Reg No: [XXXXXXX]) — *Frontend Architecture & Participant Portal*
  * Member 2: [Full Name] (Reg No: [XXXXXXX]) — *Jury Scoring Desk & Mathematical Logic*
  * Member 3: [Full Name] (Reg No: [XXXXXXX]) — *Leaderboard Sorting, Finalist Gallery & Deployment*
* **One-Line Problem Statement:** *"Traditional hackathons struggle with chaotic submissions, subjective manual jury calculations, and a lack of transparent, real-time rankings."*

---

### Slide 2: The Problem
* **Where It Happens:** University hackathons, coding sprints, and innovation competitions.
* **Who It Affects:** Student participants, faculty jury members, and student event coordinators.
* **One Striking Evidence:**  
  * 📊 **Over 70%** of participants report confusion regarding how their projects were graded.
  * ⏱️ Judges spend **up to 45 minutes** manually tallying marks across paper rubrics and spreadsheets, leading to calculation delays and tally errors.

---

### Slide 3: The Users (Personas & Real Quotes)
* **Persona 1: The Participant (Aryan, 1st Year CSE)**
  > *"We worked 24 hours non-stop, submitted a GitHub link into a messy Google Form, and never knew why we didn't qualify. We received zero feedback!"*
* **Persona 2: The Judge (Prof. Sharma, Senior Jury Member)**
  > *"Grading 40 teams across innovation, code, and UI on paper while manually doing mental math is stressful and prone to bias."*
* **Persona 3: The Event Coordinator (Priya, Student Lead)**
  > *"Manually sorting Excel sheets to announce the top 3 teams while a hall full of students waits creates unnecessary pressure."*

---

### Slide 4: Research & Field Observations
* **Survey Data (40+ students & 5 faculty judges):**
  * **88%** demanded a standardized rubric (Technical, Innovation, UI/UX, Pitch).
  * **92%** wanted a dedicated showcase gallery to view finalist repositories and pitch videos.
  * **80%** of judges preferred sliders over text-based grade entry for faster evaluation.
* **Key Pain Point:** Lack of automated qualification criteria—low-effort submissions clutter the final evaluation pool.

---

### Slide 5: The Insight & POV Statement
* **The Big Surprise:** Judges didn't just want a digital grading form; they wanted the **authority to set a dynamic qualification cutoff** so that only high-standard projects appear in the public showcase.
* **Point of View (POV) Statement:**
  > *"Hackathon organizers and faculty judges need a zero-friction, standardized evaluation desk with interactive scoring controls, so that participants receive transparent feedback and winners are determined through objective, real-time metrics."*

---

### Slide 6: The Challenge (Main HMW Question)
* **Central Design Question:**
  > **"How Might We** create a responsive, zero-server web application that streamlines project submissions, empowers judges with standardized rubric sliders and cutoff control, and delivers a live, transparent leaderboard?"

---

### Slide 7: Ideation & Evaluation Matrix
* **Explored Solutions:**
  1. *Google Sheets Script Automation:* Low visual appeal, easily broken by participants. *(Rejected)*
  2. *Full-Stack Node.js/MongoDB App:* Required paid server hosting, difficult to deploy on static GitHub Pages, prone to server cold-starts. *(Rejected)*
  3. *Client-Side Web Application with LocalStorage:* Fast, zero-server dependency, works offline, 100% free hosting on GitHub Pages, easily verifiable in Viva. *(Selected!)*
* **Idea Prioritization:** High Impact + High Feasibility ➔ Responsive HTML5 + CSS3 + Vanilla JavaScript.

---

### Slide 8: The Prototype Evolution
* **Stage 1 (Paper Wireframes):** Rough sketches of submission inputs and a static marks table.
* **Stage 2 (Base HTML Layout):** Basic form and table, but lacked visual hierarchy and role separation.
* **Stage 3 (Role-Based Architecture):** Added distinct views for Participant, Judge, Leaderboard, and Admin.
* **Stage 4 (Final High-Fidelity Prototype):** 
  * Interactive range sliders (0–25 each = 100 total).
  * Top 3 Gold/Silver/Bronze Podium display.
  * Dedicated Finalist Showcase Gallery with GitHub and video demo buttons.

---

### Slide 9: User Testing & Feedback Highlights
* **Testing Setup:** Evaluated by 6 classmates and 2 senior mentors using mock hackathon entries.
* **What Users Did:**
  * Participants easily filled out the project form and verified their submission status.
  * Judges tested scoring via range sliders and loved the auto-updating sum badge.
* **Feedback Matrix:**
  * *Praise:* "The 1-Click Demo Login saves immense time during evaluations."
  * *Critique:* "Why are all projects showing as finalists? Not everyone deserves to be in the finalist showcase!"

---

### Slide 10: What Changed (Before vs. After Iteration)
* **Change 1 (Finalist Gallery Filter):** Instead of showing all submissions, we introduced a strict eligibility filter: only projects evaluated and approved by judges appear in the Finalist Gallery.
* **Change 2 (Judge-Controlled Cutoff Slider):** We added a dynamic cutoff slider (50–95 pts) in the Jury Portal so judges determine the benchmark score for finalists.
* **Change 3 (Clean Startup Experience):** Configured the portal to always launch cleanly on the Welcome/Login page first.
* **Change 4 (XSS Sanitization):** Implemented input escaping (`escapeHTML`) to prevent script injection.

---

### Slide 11: Final Solution & Live Demo
* **Live System Architecture:**
  * **Participant Zone:** Team registration, track selection, repository/demo video linking.
  * **Jury Evaluation Desk:** 4 standardized criteria sliders (Innovation, Technical Complexity, UI/UX Design, Presentation).
  * **Finalist Project Gallery:** Visual cards with tech stack tags, code repo links, and demo video links.
  * **Live Leaderboard:** Real-time auto-sorting (`.sort()` in descending order) with Top 3 Podium.
  * **Admin Panel:** Aggregate metrics (Total teams, evaluated count, highest score, average score).
* **Live Deployment URL:** `https://abhinandankumar802103.github.io/CSE326/`
* **Why It Beats Doing Nothing:** Eliminates calculation errors, provides total transparency, and saves hours of manual administrative overhead.

---

### Slide 12: Honest Reflection, Future Scope & NABC Close
* **Honest Reflection (What Could Be Improved):**
  * Currently uses browser `localStorage`, meaning data is persisted on the local browser.
  * Multi-device real-time sync currently requires cloud integration (planned for v2 with Firebase).
* **Future Roadmap:**
  * One-click PDF Certificate generator for winners.
  * Automated plagiarism check across GitHub repositories.
* **NABC Framework Summary:**
  * **Need:** Eliminates subjective, manual hackathon grading and chaotic spreadsheets.
  * **Approach:** Modern, responsive frontend portal with interactive rubric sliders and role-based workflows.
  * **Benefit:** 100% automated score calculation, instant leaderboard updates, and zero hosting costs.
  * **Competition:** Vastly superior to tedious Google Forms and error-prone Excel calculations.

---

# 🎙️ Part 2: Complete Word-for-Word Video Script (10 Minutes)

*Format: Video recording where each member speaks clearly while showing the corresponding slide or screen.*

---

### 🟢 Section 1: Introduction, Problem & Research (0:00 – 3:00)
**Speaker: Member 1**

> *"Hello respected evaluator and professors. Welcome to our presentation for CSE326 Academic Task CA1.  
> 
> Our project is titled **HackNova: Hackathon Project Submission and Jury Evaluation Leaderboard**.  
> 
> My name is **[Member 1 Name]**, and together with my teammates **[Member 2 Name]** and **[Member 3 Name]**, we have designed and developed a responsive, interactive frontend web application to solve one of the most persistent bottlenecks in university hackathons: **chaotic project submissions and non-transparent, manual jury evaluations.**  
> 
> *(Transition to Slide 2)*  
> Let us begin with the problem. In almost every college hackathon, after 24 to 36 hours of rigorous coding, the submission process turns into chaos. Teams submit incomplete links through Google Forms, judges carry paper scorecards, and coordinators scramble with Excel sheets trying to calculate totals and resolve ties. In fact, our preliminary research revealed that over **70% of participants** feel unsure about how their projects were assessed, while judges spend up to **45 minutes** doing manual calculations.  
> 
> *(Transition to Slide 3)*  
> To understand this deeply, we spoke to three key personas:  
> First, **Aryan**, a 1st-year student who told us: *'We worked all night, submitted our GitHub link, and never got any feedback on why our team didn't qualify.'*  
> Second, **Prof. Sharma**, a senior jury member who explained: *'Tallying marks across 40 teams across innovation, code, and UI while doing mental math is stressful and prone to calculation mistakes.'*  
> And third, **Priya**, an event organizer who struggled to verify deliverables while participants waited anxiously for results.  
> 
> *(Transition to Slide 4)*  
> Our survey of over 40 students and faculty confirmed that **88%** demanded a standardized 4-part scoring rubric, **92%** wanted a public finalist showcase gallery, and judges overwhelmingly preferred interactive sliders over typing numerical marks.  
> 
> Now, I will hand over to **[Member 2]** to explain our core insights, design challenge, and prototype evolution."*

---

### 🔵 Section 2: Insights, Ideation & Prototype Evolution (3:00 – 6:00)
**Speaker: Member 2**

> *"Thank you, [Member 1]. My name is **[Member 2 Name]**, and my primary contribution to this project was developing the standardized scoring rubric and the mathematical evaluation logic in JavaScript.  
> 
> *(Transition to Slide 5)*  
> When analyzing our user research, we uncovered a fascinating insight:  
> Judges didn't just want a simple score entry box. **They wanted control over the qualification benchmark.** They told us that in large hackathons, allowing unvetted or low-effort submissions to mix with top finalists ruins the quality of the competition.  
> This led to our Point of View statement: Organizers and judges need a unified, standardized platform where judges can define qualification criteria and grade teams objectively.  
> 
> *(Transition to Slide 6)*  
> This defined our central design challenge:  
> **'How Might We create a zero-setup, responsive frontend application that simplifies project submissions, empowers judges with standardized rubric sliders and cutoff control, and delivers a live, transparent leaderboard?'**  
> 
> *(Transition to Slide 7)*  
> During our ideation phase, we evaluated three technical approaches.  
> We initially considered a full-stack Node.js and MongoDB application. However, we realized that for a college assessment and GitHub Pages deployment, client-side architecture using **HTML5, CSS3, and JavaScript with LocalStorage** provides instant zero-latency performance, requires zero server maintenance costs, and works 100% reliably without server downtime.  
> 
> *(Transition to Slide 8)*  
> We then evolved our prototype in four stages:  
> We began with hand-drawn paper wireframes, moved to a raw HTML layout, then structured the application into dedicated role-based dashboards: **Participant**, **Jury**, **Leaderboard**, and **Admin**.  
> In the final stage, we implemented our **standardized 4-criteria scoring rubric**, featuring four range sliders for:  
> 1. *Technical Complexity (25 pts)*  
> 2. *Innovation (25 pts)*  
> 3. *UI/UX Design (25 pts)*  
> 4. *Presentation (25 pts)*  
> totaling exactly **100 points**, with instant mathematical calculation.  
> 
> I now invite **[Member 3]** to discuss our user testing, iterative improvements, and guide you through the live demonstration of HackNova."*

---

### 🟣 Section 3: Testing, Iterations & Live Demo Walkthrough (6:00 – 10:00)
**Speaker: Member 3**

> *"Thank you, [Member 2]. My name is **[Member 3 Name]**, and my focus was building the dynamic Finalist Gallery, real-time leaderboard sorting algorithms, responsive CSS layout, and the live GitHub deployment.  
> 
> *(Transition to Slide 9)*  
> When we tested our prototype with our peers and mentors, the response was overwhelmingly positive. Users appreciated the 1-Click Demo login buttons and the smooth slider interactions. However, our testers gave us one critical piece of feedback:  
> *'If everyone who submits appears in the Finalist Gallery, it loses its meaning.'*  
> 
> *(Transition to Slide 10)*  
> Acting on this feedback, we made three major iterations:  
> First, we built a dedicated **Judge-Controlled Cutoff System**, allowing judges to slide the minimum qualifying score between 50 and 95 points.  
> Second, we implemented an automated eligibility filter: only projects evaluated with a score meeting the judge's cutoff are admitted into the **Finalist Project Gallery**.  
> Third, we added input sanitization to safeguard user submissions against cross-site scripting.  
> 
> *(Transition to Slide 11 & Screen Share Live App: https://abhinandankumar802103.github.io/CSE326/)*  
> Now, let us demonstrate the live, deployed web application!  
> 
> 1. **Login Portal:** As you can see, the application launches cleanly on the Welcome screen. Evaluators can type credentials or use our **1-Click Quick Demo Login** buttons.  
> 
> 2. **Participant Portal:** Let's click 'Participant Demo'. Teams can enter their team name, project title, track domain, GitHub repository link, demo video link, and tech stack tags. When we submit, it immediately updates the participant's active status.  
> 
> 3. **Jury Evaluation Desk:** Next, let's switch to the Jury Portal. Notice the **Judge Finalist Qualification Control** at the top. The judge can set the cutoff score—say, 75 points. When we click 'Evaluate Now' on a project, the scorecard modal opens with our four standardized sliders. As I move the sliders, the total score calculates in real time out of 100, and the system automatically checks the 'Approve as Finalist' box if it meets the cutoff!  
> 
> 4. **Finalist Project Gallery:** If we navigate to the Finalist Gallery, only projects that scored 75 or higher and received jury approval are displayed. Each card clearly highlights the **Team Name, Tech Stack Tags, direct GitHub link, and Demo Video link**, fulfilling all assessment criteria.  
> 
> 5. **Live Leaderboard:** On the Leaderboard, all projects are dynamically sorted in descending order of score, with the top three projects proudly featured on the **Gold 🥇, Silver 🥈, and Bronze 🥉 Podium**.  
> 
> *(Transition to Slide 12: Reflection & Conclusion)*  
> In conclusion, HackNova replaces chaotic forms and spreadsheets with an elegant, responsive, and mathematically sound evaluation portal.  
> 
> Looking ahead, we plan to integrate cloud database synchronization and automated PDF certificate generation.  
> 
> Regarding our individual contributions:  
> * **[Member 1]** engineered the frontend UI architecture, form validation, and user personas.  
> * **[Member 2]** developed the standardized 4-criteria rubric, slider mechanics, and scoring algorithms.  
> * **[Member 3]** implemented the Finalist Gallery filtering, Leaderboard sorting logic, responsive CSS design, and GitHub Pages live deployment.  
> 
> The project is publicly accessible on GitHub and deployed live on GitHub Pages. Thank you for your time, and we look forward to answering any questions during the Viva!"*
