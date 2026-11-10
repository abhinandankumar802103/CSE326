# 🎙️ HackNova — Page-by-Page 10-Minute Presentation Script (3 Members)

> **Total Duration:** Exactly 10 Minutes (600 Seconds)  
> **Structure:** 12 Slides + Live Demonstration  
> **Team Size:** 3 Members  

---

## ⏱️ Master Timeline Overview

| Section | Speaker | Slides Covered | Timeline | Duration |
| :--- | :--- | :---: | :---: | :---: |
| **Part 1: Empathy & Research** | **Member 1** | Slides 1, 2, 3, 4 | **0:00 – 3:00** | 3 min |
| **Part 2: Insights, HMW & Prototype** | **Member 2** | Slides 5, 6, 7, 8 | **3:00 – 6:00** | 3 min |
| **Part 3: Testing, Live Demo & NABC** | **Member 3** | Slides 9, 10, 11, 12 | **6:00 – 10:00** | 4 min |

---

# 🟢 PART 1: SPEAKER — MEMBER 1 (0:00 – 3:00)

### 📄 SLIDE 1: Title & Introduction
* **Slide on Screen:** Slide 1 (Hero Title, Project Name, Team Roles)
* **Timeline:** **0:00 – 0:45** (45 seconds)
* **Spoken Script:**

> *"A very pleasant day to our respected faculty evaluator and peers.  
> 
> Welcome to our presentation for **CSE326 Web Development Academic Task CA1**. Our project is titled **HackNova: Hackathon Project Submission & Jury Evaluation Leaderboard**.  
> 
> My name is **[Your Name - Member 1]**, and I am presenting alongside my teammates **[Member 2 Name]** and **[Member 3 Name]**.  
> 
> To summarize our core challenge in one sentence:  
> **Traditional hackathons suffer from chaotic submissions, subjective manual jury mark calculations, and a complete lack of transparent, real-time rankings.**  
> 
> Today, we will walk you through our Design Thinking journey from problem discovery to our live deployed solution on GitHub Pages."*

---

### 📄 SLIDE 2: The Problem
* **Slide on Screen:** Slide 2 (Problem Context, 3 Stat Cards, 4-Step Process Flow)
* **Timeline:** **0:45 – 1:30** (45 seconds)
* **Spoken Script:**

> *"*(Look at Slide 2)*  
> Let us examine where this problem happens. In university coding hackathons, 100 or more students work tirelessly for 24 to 36 hours. But when the submission deadline strikes, chaos ensues.  
> 
> Look at the striking evidence on screen:  
> • First, **72% of participants** report having zero visibility into how their marks were tallied.  
> • Second, faculty judges spend **up to 45 minutes** doing manual arithmetic across paper rubrics and Excel sheets to resolve ties.  
> • And third, **1 in every 4 hackathons** experiences delayed awards ceremonies due to spreadsheet formula errors.  
> 
> As shown in our process diagram, submissions move from chaotic Google Forms to paper rubrics, leading to formula mistakes and long, anxious delays for tired students."*

---

### 📄 SLIDE 3: The Users
* **Slide on Screen:** Slide 3 (3 Persona Cards: Aryan, Prof. Sharma, Priya with Quotes)
* **Timeline:** **1:30 – 2:15** (45 seconds)
* **Spoken Script:**

> *"*(Look at Slide 3)*  
> Through our empathy research, we identified three core user personas:  
> 
> 1. **Aryan, a 1st-year student participant**, who told us:  
> *'We coded 24 hours non-stop, submitted our repo into a Google Form, and never got any feedback on why our project didn't qualify!'* Aryan needs instant submission receipts and transparent scoring criteria.  
> 
> 2. **Prof. Sharma, our faculty jury member**, who shared:  
> *'Evaluating 40 teams across innovation, code, and UI while doing mental math on paper rubrics is exhausting and prone to calculation mistakes.'* He needs sliders that auto-sum to 100.  
> 
> 3. And **Priya, our student event lead**, who said:  
> *'Manually sorting spreadsheet columns to announce the top 3 teams with a hall full of students waiting creates massive stress.'* She needs a real-time dynamic leaderboard."*

---

### 📄 SLIDE 4: Field Research & Survey Chart
* **Slide on Screen:** Slide 4 (Survey Column Chart & 2 Key Finding Cards)
* **Timeline:** **2:15 – 3:00** (45 seconds)
* **Spoken Script:**

> *"*(Look at Slide 4)*  
> We backed our empathy interviews with quantitative field research, surveying **40 hackathon students and 5 faculty evaluators**.  
> 
> As shown on the column chart:  
> • **88%** demanded a standardized 4-criteria rubric.  
> • **92%** wanted a public showcase gallery to inspect finalist code and pitch videos.  
> • **80% of faculty judges** preferred range sliders over typing marks into cells because sliders enforce scoring caps and eliminate arithmetic errors.  
> • And **95%** wanted an instant, live-ranked leaderboard.  
> 
> Most importantly, our survey revealed that unvetted, low-effort submissions dilute the competition—proving the urgent need for a qualification screening filter.  
> 
> I now hand over to **[Member 2 Name]** to explain our core insight, design challenge, and prototype evolution."*

---

# 🔵 PART 2: SPEAKER — MEMBER 2 (3:00 – 6:00)

### 📄 SLIDE 5: The Insight & POV Statement
* **Slide on Screen:** Slide 5 (Core Insight Banner & Funnel Architecture Diagram)
* **Timeline:** **3:00 – 3:45** (45 seconds)
* **Spoken Script:**

> *"Thank you, [Member 1]. My name is **[Member 2 Name]**, and my primary technical contribution was developing the standardized scoring rubric and the mathematical evaluation engine.  
> 
> *(Look at Slide 5)*  
> When analyzing our survey, we uncovered a fascinating surprise:  
> **Judges didn't just want a digital grading form—they demanded control over the qualification benchmark.** They explained that in large hackathons, allowing low-effort submissions to appear alongside top finalist entries ruins the quality of the competition.  
> 
> This shaped our Point of View statement:  
> **Hackathon organizers and faculty judges need a unified web portal with standardized rubric sliders and dynamic qualification filtering, because participants deserve transparent feedback and rankings must be mathematically fair.**  
> 
> As illustrated in our architecture diagram, all submissions pass through our **Jury Qualification Engine**, where projects scoring at or above the judge's cutoff enter the Finalist Showcase, while lower-scoring projects remain in the general leaderboard pool."*

---

### 📄 SLIDE 6: The Challenge (HMW Question)
* **Slide on Screen:** Slide 6 (Central HMW Banner & 3 Strategic Pillars)
* **Timeline:** **3:45 – 4:30** (45 seconds)
* **Spoken Script:**

> *"*(Look at Slide 6)*  
> This led us to our central Design Challenge question:  
> **'How Might We create a zero-setup, responsive frontend application that simplifies project submissions, empowers judges with standardized rubric sliders and cutoff control, and delivers a live, transparent leaderboard?'**  
> 
> To tackle this, we established three non-negotiable design pillars:  
> • **Pillar 1: Frictionless Submissions** — A clean form capturing team name, track, GitHub URL, and demo video link with instant input validation.  
> • **Pillar 2: Objective Rubric Sliders** — Four standardized criteria capped at 25 points each: Innovation, Technical Complexity, UI/UX Design, and Presentation, summing to 100 points with real-time math.  
> • **Pillar 3: Dynamic Finalist Filtering** — Giving judges live cutoff slider control (from 50 to 95 points) to govern finalist eligibility automatically."*

---

### 📄 SLIDE 7: Ideation (2x2 Matrix & Rejected Ideas)
* **Slide on Screen:** Slide 7 (2x2 Impact vs. Feasibility Matrix)
* **Timeline:** **4:30 – 5:15** (45 seconds)
* **Spoken Script:**

> *"*(Look at Slide 7)*  
> In our ideation phase, we mapped potential technical solutions across an **Impact vs. Feasibility Matrix**:  
> 
> 1. We rejected **Google Sheets automation** because it has poor UI, easily broken formulas, and zero mobile responsiveness.  
> 2. We considered a **Full-Stack Node.js and MongoDB application**, but rejected it because it requires expensive server hosting, suffers from server cold-start delays during presentations, and cannot be hosted statically on GitHub Pages.  
> 3. We also rejected a **Mobile APK** because forcing judges to install third-party apps on their phones creates unnecessary friction.  
> 
> 🏆 **Our Winning Choice:** A high-performance client-side web application built with **HTML5, CSS3, and Vanilla JavaScript with LocalStorage**. It delivers zero-latency performance, requires zero backend server costs, runs permanently on GitHub Pages, and is 100% transparent for Viva evaluation."*

---

### 📄 SLIDE 8: The Prototype Evolution
* **Slide on Screen:** Slide 8 (4-Stage Pipeline Diagram from Paper to Final)
* **Timeline:** **5:15 – 6:00** (45 seconds)
* **Spoken Script:**

> *"*(Look at Slide 8)*  
> We engineered our prototype across four progressive stages:  
> 
> • **Stage 1 (Paper Wireframes):** We sketched initial input fields, project card layouts, and basic table columns.  
> • **Stage 2 (Semantic HTML):** We translated wireframes into structured HTML with CSS Grid, but quickly identified a lack of role-based navigation.  
> • **Stage 3 (Multi-Role Navigation Engine):** We architected distinct dashboards for **Participants**, **Judges**, and **Admins**, integrating browser `localStorage` for instant persistence without a database.  
> • **Stage 4 (High-Fidelity System):** We introduced our 4 standardized rubric sliders, dynamic live total math, our Top 3 Gold/Silver/Bronze Podium, and the Finalist Project Showcase.  
> 
> I now invite **[Member 3 Name]** to discuss our user testing results, key design iterations, and lead our live working demonstration."*

---

# 🟣 PART 3: SPEAKER — MEMBER 3 (6:00 – 10:00)

### 📄 SLIDE 9: Testing & Feedback Matrix
* **Slide on Screen:** Slide 9 (Testing Tasks, Results & Feedback Matrix)
* **Timeline:** **6:00 – 6:45** (45 seconds)
* **Spoken Script:**

> *"Thank you, [Member 2]. My name is **[Member 3 Name]**, and my primary focus was building the dynamic Finalist Gallery, real-time leaderboard sorting algorithms, responsive CSS layout, and the live GitHub deployment.  
> 
> *(Look at Slide 9)*  
> We rigorously tested our prototype with **6 classmates and 2 senior mentors**.  
> The results were compelling:  
> • Participants registered projects with GitHub and demo video links in under 45 seconds.  
> • Judges evaluated projects via sliders with zero calculation confusion.  
> • Evaluators praised our **1-Click Demo Login** buttons, which eliminate the hassle of typing demo passwords.  
> 
> However, our testers gave us one critical piece of pushback:  
> **'Why are all submitted projects appearing in the Finalist Gallery? Incomplete or low-effort submissions should not be called finalists!'**  
> We immediately recognized this as a vital flaw to fix."*

---

### 📄 SLIDE 10: What Changed (Before vs. After)
* **Slide on Screen:** Slide 10 (Side-by-Side Comparison: Red Before vs. Green After)
* **Timeline:** **6:45 – 7:30** (45 seconds)
* **Spoken Script:**

> *"*(Look at Slide 10)*  
> Acting directly on that user feedback, we implemented three major iterative improvements:  
> 
> • **First, Filtered Finalist Showcase:** Instead of showing all raw submissions, only projects that are evaluated by the jury and meet the cutoff score are admitted into the **Finalist Project Gallery**.  
> • **Second, Dynamic Judge Cutoff Slider:** We gave the jury real-time authority to adjust the minimum qualifying benchmark between **50 and 95 points**.  
> • **Third, Clean Startup Experience:** We fixed the session startup so the application always launches cleanly on the Welcome & Login screen first.  
> • **Fourth, Input Sanitization:** We added client-side `escapeHTML` methods to prevent any cross-site scripting vulnerabilities.  
> 
> Now, let us move from slides to our live working application!"*

---

### 📄 SLIDE 11: Final Solution & LIVE APPLICATION DEMO
* **Slide on Screen:** Slide 11 ➔ **[Switch screen share to live browser: https://abhinandankumar802103.github.io/CSE326/]**
* **Timeline:** **7:30 – 9:15** (1 minute 45 seconds)
* **Spoken Script:**

> *"*(Switch screen to live browser)*  
> Our project is deployed live on GitHub Pages at:  
> `abhinandankumar802103.github.io/CSE326/`.  
> 
> Let us walk through the workflow:  
> 
> 1. **Login Screen:** As you can see, the portal opens cleanly on the Welcome screen. Evaluators can type credentials or click any **1-Click Demo Login** button. Let's click **'Participant Demo'**.  
> 
> 2. **Participant Portal:** Here, teams can submit their team name, project title, track category, GitHub repository link, demo video link, and tech stack tags. On submission, the form validates inputs and immediately updates the team's active submission status card.  
> 
> 3. **Jury Evaluation Desk:** Now, let's switch to the **Jury Portal**. Notice the **Judge Finalist Qualification Control** at the top. The judge can set the cutoff score—say, 75 points.  
> When we click **'Evaluate Now'** on a project, the scorecard modal opens with our four standardized sliders:  
> *Innovation (25), Technical Complexity (25), UI/UX (25), and Presentation (25).*  
> As I move the sliders, the total score calculates live out of 100 points, and the system automatically updates the 'Approve as Finalist' checkbox if it meets the cutoff! Let's save the evaluation.  
> 
> 4. **Finalist Project Gallery:** Next, let's click on **'Finalist Gallery'**. Notice that only projects scoring 75 or higher and approved by the jury appear here! Each card displays the **Team Name, Tech Stack Tags, direct GitHub Repo button, and Demo Video Link**. Projects scoring below the cutoff stay in the general pool and do not clutter the finalist showcase.  
> 
> 5. **Live Leaderboard:** Finally, on the Leaderboard, all projects are dynamically sorted in descending order of score using JavaScript's `.sort()` algorithm. The top three teams are proudly featured on the **Gold 🥇, Silver 🥈, and Bronze 🥉 Podium**!"*

---

### 📄 SLIDE 12: Reflection, Roadmap, NABC & Closing
* **Slide on Screen:** **[Switch back to Slide 12]** (NABC 4-Quadrant Grid & Team Summary)
* **Timeline:** **9:15 – 10:00** (45 seconds)
* **Spoken Script:**

> *"*(Look at Slide 12)*  
> To conclude with an honest reflection:  
> While our client-side `localStorage` engine provides instant zero-server reliability, data is local to the browser. In Version 2.0, we plan to integrate cloud database synchronization via Firebase and add an automated PDF certificate generator for winning teams.  
> 
> To summarize our project using the **NABC Framework**:  
> • **Need:** University hackathons require transparent, error-free project evaluation.  
> • **Approach:** A responsive web portal featuring standardized 4-part rubric sliders and dynamic cutoff screening.  
> • **Benefit:** 100% automated score calculations, instant podium rankings, and permanent portfolio showcases for students.  
> • **Competition:** Vastly superior to tedious Google Forms and error-prone Excel spreadsheets.  
> 
> Regarding our individual contributions:  
> • **[Member 1]** engineered the frontend UI architecture, form validation, and user research.  
> • **[Member 2]** developed the 4-criteria rubric sliders, mathematical scoring engine, and cutoff logic.  
> • **[Member 3]** implemented the Finalist Gallery filtering, Leaderboard sorting algorithms, responsive CSS styling, and GitHub Pages deployment.  
> 
> Our complete source code is public on GitHub, and our live application is running on GitHub Pages.  
> Thank you so much for your time and attention. We are now open for any questions during the Viva!"*

---
*(End of Presentation — Exactly 10:00 Minutes)*
