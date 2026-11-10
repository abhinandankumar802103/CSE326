# ⚡ HackNova — Hackathon Project Submission & Jury Leaderboard Portal

> **Course:** CSE326 — Web Development (Academic Task CA1: Project-Based Assessment)  
> **Student Level:** 1st Semester  
> **Technologies Used:** HTML5, CSS3, JavaScript (Vanilla ES6), Browser LocalStorage  
> **Deployment Target:** GitHub Pages / Vercel / Netlify  

---

## 📌 1. Project Overview & Problem Statement
* **Assigned Problem Statement:** *Hackathon Project Submission And Jury Evaluation Leaderboard*
* **Core Objective:** Develop a responsive, interactive frontend web application that allows hackathon teams to submit their projects, provides a dedicated scoring panel for the jury to evaluate submissions against defined rubrics, and dynamically calculates a real-time leaderboard ranking.

---

## ✨ 2. Key Features Implemented

### 🔐 Multi-Role Authentication & Quick Access
* **Role-Based Access Control:** Separate workflows for **Participants**, **Jury / Judges**, and **Hackathon Admins**.
* **1-Click Demo Login:** Dedicated fast-login buttons for evaluation demonstrations so you don't have to re-type credentials during your viva or video presentation.
* **Persistent Sessions:** Remembers logged-in user state using browser `localStorage`.

### 🧑‍💻 Participant Portal
* **Project Submission Form:** Collects Team Name, Project Title, Hackathon Track/Domain, Tech Stack, Description, GitHub Repo URL, and Live Demo Link.
* **Live Form Validation:** Prevents empty or invalid submissions.
* **My Submission Card:** Instant status display indicating whether the project is *Pending Review* or *Evaluated* with jury remarks.

### 🎨 Finalist Project Gallery (Professor's Core Requirement)
* **Dedicated Showcase View:** Clean responsive cards for shortlisted projects.
* **Team Details:** Displays Team Name, Project Title, Domain/Track, and Project Description.
* **Tech Stack Tags:** Visual badge chips displaying all technologies used (e.g. Python, TensorFlow, React, HTML5, WebRTC).
* **Direct Access Buttons:** 
  * `💻 GitHub Repository Link` (Direct one-click access)
  * `🎥 Project Demo Video Link` (Direct one-click access)
* **Real-time Filter & Search:** Instant search by project name, team, or tech stack, with track filtering.

### ⚖️ Standardized Jury Evaluation Desk (Professor's Core Requirement)
* **Project Queue & Filters:** Filter projects by "Pending Review" or "Already Evaluated", with live text search.
* **Standardized Scoring Rubric with Sliders (Exact 4 Criteria):**
  1. *Technical Complexity (0 – 25 pts)*
  2. *Innovation (0 – 25 pts)*
  3. *UI/UX Design (0 – 25 pts)*
  4. *Presentation (0 – 25 pts)*
* **Real-time Total Calculation:** Live calculated sum out of **100 points**.
* **Jury Feedback Notes:** Field to leave constructive feedback for the team.

### 🏆 Dynamic Live Leaderboard
* **Automatic Sorting:** Dynamically sorts entries in descending order based on jury scores.
* **Podium View:** Highlights the Top 3 entries with 🥇 Gold, 🥈 Silver, and 🥉 Bronze cards.
* **Search & Domain Filter:** Filter rankings by hackathon category (e.g., AI/ML, Web Dev, FinTech, IoT).

### 🛡️ Admin Control Center
* **Key Metric Cards:** Total Submissions, Evaluated Projects, Highest Score, and Average Score.
* **Manage Submissions Table:** View, inspect, or delete entries.
* **Data Management:** Buttons to reload default demo projects or clear records.

---

## 📂 3. Codebase Structure
```text
CSE326/
├── index.html       # Semantic HTML layout, modals, and templates
├── style.css        # Responsive styling, CSS Grid, Flexbox, & design tokens
├── script.js        # Event handling, state management, & LocalStorage logic
└── README.md        # Documentation, deployment guide, & Viva cheat-sheet
```

---

## 🚀 4. How to Run in Visual Studio Code

1. **Open the Project Folder:**
   - Open **VS Code**.
   - Click `File` ➔ `Open Folder...` and select `D:\CSE326`.
2. **Run in Browser:**
   - **Method A (Easiest):** Right-click `index.html` in VS Code and choose **"Open with Live Server"** (if the Live Server extension is installed).
   - **Method B:** Or simply double-click `index.html` in Windows File Explorer to open it in Chrome, Edge, or Firefox.

---

## 🌐 5. How to Deploy to GitHub Pages (Mandatory for CA1)

1. **Create a GitHub Repository:**
   - Go to [github.com](https://github.com) and create a new public repository named `hacknova-portal`.
2. **Push your code to GitHub:**
   In your VS Code terminal (or Git Bash), run:
   ```bash
   git init
   git add .
   git commit -m "Initial commit for CA1 project"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/hacknova-portal.git
   git push -u origin main
   ```
3. **Turn on GitHub Pages:**
   - In your GitHub repository, click on **Settings** (top right tab).
   - On the left sidebar, click **Pages**.
   - Under **Build and deployment > Branch**, select `main` and folder `/(root)`, then click **Save**.
   - Wait 1–2 minutes; GitHub will give you your live URL:  
     `https://YOUR_USERNAME.github.io/hacknova-portal/`
   - Paste this URL in your mandatory CA1 Excel submission sheet!

---

## 🎓 6. VIVA Preparation Guide (10 Marks)
*Be ready to answer these common viva questions with confidence:*

### Q1: Why did you use `localStorage` instead of a traditional backend database?
> **Answer:** "Since our project is a responsive client-side application hosted on GitHub Pages, browser `localStorage` allows us to persist project submissions, jury scores, and user login state across page refreshes without needing a separate backend server or paid database."

### Q2: How does the Leaderboard automatically rank the projects?
> **Answer:** "In `script.js`, inside the `renderLeaderboard()` function, we use JavaScript's native `.sort()` method. We sort the project array in descending order (`b.totalScore - a.totalScore`), placing evaluated projects with the highest scores at the top."

### Q3: How is responsive design implemented?
> **Answer:** "We used CSS3 Flexbox and CSS Grid layouts alongside media queries (`@media (max-width: 768px)`). On smaller screens, grids convert to single-column layouts, table containers become scrollable, and navigation collapses neatly."

### Q4: How is data sanitized against Cross-Site Scripting (XSS)?
> **Answer:** "We implemented an `escapeHTML()` helper function in `script.js` that converts special characters like `<`, `>`, `&`, and quotes into their safe HTML entities before injecting user input into the DOM."

### Q5: How does the Jury evaluation calculate scores in real time?
> **Answer:** "Each slider input has an `oninput` event listener that invokes `app.updateLiveTotal()`. This function reads the numeric values of all 4 criteria sliders (Innovation, Technical Execution, UI/UX, Presentation), adds them up, and updates the total score badge immediately."

### Q6: How does the Finalist Eligibility filter work?
> **Answer:** "In our application, the Judge panel has dynamic control over the minimum qualification benchmark (via a cutoff slider in the Jury Portal, defaulting to 75/100). Submissions that score below this threshold or are still pending review are kept out of the Finalist Showcase, ensuring only high-caliber, jury-approved projects are featured."

---

## 🎥 7. Video Presentation Outline (5 Marks)
*Suggested 3–4 minute recording flow:*

1. **Introduction (30s):**
   - Introduce yourself/team, course code (CSE326), and problem statement: *Hackathon Project Submission and Jury Evaluation Leaderboard*.
2. **Participant Submission Demo (1 min):**
   - Click "Participant Demo" on the login screen.
   - Fill out a new sample project and click *Submit*.
   - Show how the project appears under *My Active Submission*.
3. **Jury Evaluation Demo (1 min):**
   - Switch to "Jury / Judge Portal".
   - Open the newly submitted project in the scorecard modal.
   - Adjust the 4 rubric sliders and show live total score updating to 100.
   - Add feedback and click *Save Score*.
4. **Live Leaderboard & Admin Demo (1 min):**
   - Open the *Leaderboard* to show the newly graded project dynamically ranked.
   - Show the 🥇 Gold, 🥈 Silver, 🥉 Bronze podium cards.
   - Switch to *Admin Panel* to show the updated statistics (Average score, Total submissions).
5. **Conclusion & Technologies Used (30s):**
   - Mention pure HTML5, CSS3, JavaScript, and GitHub Pages hosting.
