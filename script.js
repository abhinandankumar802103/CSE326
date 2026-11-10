/**
 * ====================================================================
 * HACKNOVA - Hackathon Project Submission & Jury Leaderboard
 * Course: CSE326 - Academic Task CA1
 * Description: Client-side Interactive Application with LocalStorage
 * ====================================================================
 * 
 * VIVA TIP FOR 1st SEMESTER STUDENTS:
 * - This file handles all interactivity (clicks, form submits, score calculations).
 * - It uses the browser's "localStorage" API to store data without needing a backend server.
 * - Whenever data changes, we update localStorage and re-render the HTML views.
 */

// Initial Sample Data (Pre-loaded so your project always looks active & impressive)
const INITIAL_DEMO_PROJECTS = [
    {
        id: "proj-101",
        teamName: "NeuralSquad",
        projectTitle: "HealthVision - AI Chest X-Ray Triage",
        category: "AI & Machine Learning",
        techStack: "Python, TensorFlow, Flask, HTML5, CSS3",
        description: "An automated deep learning system designed to help rural clinics detect early signs of pneumonia and tuberculosis from chest X-rays in seconds.",
        repoUrl: "https://github.com/demo/healthvision",
        demoUrl: "https://healthvision-demo.vercel.app",
        submittedAt: "2026-11-08",
        status: "evaluated",
        scores: {
            innovation: 24,
            technical: 23,
            uiux: 22,
            pitch: 24
        },
        totalScore: 93,
        juryFeedback: "Exceptional real-world impact and high technical accuracy. Model inference time is fast and UI is very clear."
    },
    {
        id: "proj-102",
        teamName: "CyberKnights",
        projectTitle: "ChainGuard - Decentralized Identity Vault",
        category: "FinTech & Blockchain",
        techStack: "Solidity, Ethereum, Web3.js, JavaScript",
        description: "A tamper-proof digital credentials and student identity verification vault allowing instant verification while maintaining user privacy.",
        repoUrl: "https://github.com/demo/chainguard",
        demoUrl: "https://chainguard-vault.netlify.app",
        submittedAt: "2026-11-09",
        status: "evaluated",
        scores: {
            innovation: 22,
            technical: 24,
            uiux: 20,
            pitch: 22
        },
        totalScore: 88,
        juryFeedback: "Strong smart contract architecture. User interface could be simplified for non-crypto users."
    },
    {
        id: "proj-103",
        teamName: "EcoCrafters",
        projectTitle: "SmartBin - IoT Waste Segregation",
        category: "Smart City & IoT",
        techStack: "Arduino, C++, JavaScript, Chart.js",
        description: "A smart city trash bin system that classifies wet, dry, and recyclable waste using optical sensors and sends fill-level alerts to municipal trucks.",
        repoUrl: "https://github.com/demo/smartbin-iot",
        demoUrl: "https://smartbin.demo.site",
        submittedAt: "2026-11-09",
        status: "evaluated",
        scores: {
            innovation: 21,
            technical: 20,
            uiux: 21,
            pitch: 20
        },
        totalScore: 82,
        juryFeedback: "Great civic initiative. Clean hardware sensor integration and practical dashboard."
    },
    {
        id: "proj-104",
        teamName: "CodeCrafters",
        projectTitle: "LearnBuddy - Peer-to-Peer Study Hub",
        category: "EdTech & Social Good",
        techStack: "HTML5, CSS3, JavaScript, WebRTC",
        description: "A campus platform connecting university students for live collaborative note-taking and peer tutoring sessions.",
        repoUrl: "https://github.com/demo/learnbuddy",
        demoUrl: "https://learnbuddy.study",
        submittedAt: "2026-11-10",
        status: "pending",
        scores: {
            innovation: 0,
            technical: 0,
            uiux: 0,
            pitch: 0
        },
        totalScore: 0,
        juryFeedback: "",
        isFinalistApproved: false
    },
    {
        id: "proj-105",
        teamName: "CampusRiders",
        projectTitle: "CampusRide - Student Carpooling & Transit",
        category: "Web & Mobile App",
        techStack: "HTML5, CSS3, JavaScript",
        description: "A local carpooling and shuttle tracker for students to share rides to college and reduce campus traffic.",
        repoUrl: "https://github.com/demo/campusride",
        demoUrl: "https://campusride-demo.vercel.app",
        submittedAt: "2026-11-09",
        status: "evaluated",
        scores: {
            innovation: 16,
            technical: 17,
            uiux: 18,
            pitch: 17
        },
        totalScore: 68,
        juryFeedback: "Good basic concept, but needs real-time GPS tracking and stronger security validation to meet finalist standards.",
        isFinalistApproved: false
    }
];

/**
 * Main Application Object
 * Bundles all state and methods to avoid global namespace pollution
 */
const app = {
    // Current state
    currentUser: null,
    projects: [],
    juryCutoffScore: 75, // Default cutoff decided by Judge panel

    /**
     * 1. Application Initialization
     * Called when the webpage finishes loading
     */
    init: function() {
        console.log("⚡ Initializing HackNova Portal...");

        // Load or initialize projects from LocalStorage
        const savedProjects = localStorage.getItem("hacknova_projects");
        if (savedProjects) {
            try {
                this.projects = JSON.parse(savedProjects);
            } catch (e) {
                console.error("Error parsing projects from localStorage", e);
                this.projects = [...INITIAL_DEMO_PROJECTS];
            }
        } else {
            // First time load: seed with initial sample data
            this.projects = [...INITIAL_DEMO_PROJECTS];
            this.saveProjectsToStorage();
        }

        // Load Judge Cutoff Score from LocalStorage
        const savedCutoff = localStorage.getItem("hacknova_jury_cutoff");
        this.juryCutoffScore = savedCutoff ? parseInt(savedCutoff) : 75;
        this.updateCutoffDisplays();

        // Always open the Login Section first when launching the site
        localStorage.removeItem("hacknova_current_user");
        this.currentUser = null;

        const navLinks = document.getElementById("navLinks");
        const userBadge = document.getElementById("userBadge");
        if (navLinks) navLinks.style.display = "none";
        if (userBadge) userBadge.style.display = "none";

        this.showSection("loginSection");

        // Render live leaderboard and gallery initially so data is ready
        this.renderLeaderboard();
        this.renderGallery();
    },

    /**
     * Update all DOM elements that display the Jury Cutoff Score
     */
    updateCutoffDisplays: function() {
        const slider = document.getElementById("judgeCutoffSlider");
        const valDisplay = document.getElementById("judgeCutoffValueDisplay");
        const galleryBadge = document.getElementById("galleryCutoffBadge");
        const ruleScore = document.getElementById("galleryCriteriaRuleScore");

        if (slider) slider.value = this.juryCutoffScore;
        if (valDisplay) valDisplay.textContent = this.juryCutoffScore;
        if (galleryBadge) galleryBadge.textContent = `${this.juryCutoffScore}+ Pts`;
        if (ruleScore) ruleScore.textContent = this.juryCutoffScore;
    },

    /**
     * Judge updates the minimum score criteria for Finalist Gallery
     */
    handleCutoffChange: function(newCutoff) {
        this.juryCutoffScore = parseInt(newCutoff) || 75;
        localStorage.setItem("hacknova_jury_cutoff", this.juryCutoffScore);

        this.updateCutoffDisplays();
        this.renderJudgeProjects();
        this.renderGallery();

        this.showToast(`🎯 Jury Cutoff updated to ${this.juryCutoffScore}+ points`, "⚖️");
    },

    /**
     * 2. Save Projects array into browser LocalStorage
     */
    saveProjectsToStorage: function() {
        localStorage.setItem("hacknova_projects", JSON.stringify(this.projects));
    },

    /**
     * 3. Handle Standard Login Form Submission
     */
    handleLoginFormSubmit: function(event) {
        event.preventDefault();
        const role = document.getElementById("loginRoleSelect").value;
        const username = document.getElementById("loginUsername").value.trim();

        if (!username) {
            this.showToast("Please enter a username or team name.", "⚠️");
            return;
        }

        this.setUserSession({
            username: username,
            role: role,
            title: role.toUpperCase()
        });

        this.showToast(`Welcome, ${username}! Signed in as ${role}.`, "✅");
    },

    /**
     * 4. Quick 1-Click Demo Login (Great for Viva & Presentation)
     */
    quickLogin: function(role, username, subtitle) {
        this.setUserSession({
            username: username,
            role: role,
            title: subtitle || role.toUpperCase()
        });

        this.showToast(`Logged in as ${username} (${role})`, "⚡");
    },

    /**
     * 5. Set & Store User Session
     */
    setUserSession: function(userObj) {
        this.currentUser = userObj;
        localStorage.setItem("hacknova_current_user", JSON.stringify(userObj));
        this.applyUserSession();
    },

    /**
     * 6. Apply UI changes according to user role
     */
    applyUserSession: function() {
        if (!this.currentUser) return;

        const navLinks = document.getElementById("navLinks");
        const userBadge = document.getElementById("userBadge");
        const userNameDisplay = document.getElementById("userNameDisplay");
        const userRoleDisplay = document.getElementById("userRoleDisplay");
        const userAvatar = document.getElementById("userAvatar");

        // Show navigation bar controls
        navLinks.style.display = "flex";
        userBadge.style.display = "flex";

        userNameDisplay.textContent = this.currentUser.username;
        userRoleDisplay.textContent = this.currentUser.role;

        // Set role avatar
        if (this.currentUser.role === "participant") userAvatar.textContent = "🧑‍💻";
        else if (this.currentUser.role === "judge") userAvatar.textContent = "⚖️";
        else if (this.currentUser.role === "admin") userAvatar.textContent = "🛡️";
        else userAvatar.textContent = "👤";

        // Route to the appropriate default screen based on role
        if (this.currentUser.role === "participant") {
            this.showSection("participantSection");
            this.renderParticipantDashboard();
        } else if (this.currentUser.role === "judge") {
            this.showSection("judgeSection");
            this.renderJudgeProjects();
        } else if (this.currentUser.role === "admin") {
            this.showSection("adminSection");
            this.renderAdminDashboard();
        } else {
            // Guest or public viewer
            this.showSection("leaderboardSection");
            this.renderLeaderboard();
        }
    },

    /**
     * 7. User Logout
     */
    logout: function() {
        this.currentUser = null;
        localStorage.removeItem("hacknova_current_user");

        // Hide user info from navbar
        document.getElementById("navLinks").style.display = "none";
        document.getElementById("userBadge").style.display = "none";

        // Reset login form inputs
        const loginForm = document.getElementById("loginForm");
        if (loginForm) loginForm.reset();

        this.showSection("loginSection");
        this.showToast("Signed out successfully.", "👋");
    },

    /**
     * 8. Section / Tab View Switcher
     */
    showSection: function(sectionId) {
        // Remove 'active-view' from all views
        const views = document.querySelectorAll(".view-section");
        views.forEach(view => view.classList.remove("active-view"));

        // Add 'active-view' to target view
        const targetView = document.getElementById(sectionId);
        if (targetView) {
            targetView.classList.add("active-view");
        }

        // Update active class on nav buttons
        const navButtons = document.querySelectorAll(".nav-btn");
        navButtons.forEach(btn => btn.classList.remove("active"));

        if (sectionId === "gallerySection") {
            document.getElementById("navBtnGallery")?.classList.add("active");
            this.renderGallery();
        }
        else if (sectionId === "participantSection") document.getElementById("navBtnParticipant")?.classList.add("active");
        else if (sectionId === "judgeSection") {
            document.getElementById("navBtnJudge")?.classList.add("active");
            this.renderJudgeProjects();
        }
        else if (sectionId === "leaderboardSection") {
            document.getElementById("navBtnLeaderboard")?.classList.add("active");
            this.renderLeaderboard();
        }
        else if (sectionId === "adminSection") {
            document.getElementById("navBtnAdmin")?.classList.add("active");
            this.renderAdminDashboard();
        }

        window.scrollTo({ top: 0, behavior: "smooth" });
    },

    /**
     * Navigate to home (Login if logged out, or default dashboard if logged in)
     */
    navigateToHome: function() {
        if (!this.currentUser) {
            this.showSection("loginSection");
        } else {
            this.applyUserSession();
        }
    },

    /**
     * 9. PARTICIPANT ZONE: Handle Project Submission Form
     */
    handleProjectSubmission: function(event) {
        event.preventDefault();

        const teamName = document.getElementById("teamNameInput").value.trim();
        const projectTitle = document.getElementById("projectTitleInput").value.trim();
        const category = document.getElementById("projectCategorySelect").value;
        const techStack = document.getElementById("techStackInput").value.trim();
        const description = document.getElementById("projectDescriptionInput").value.trim();
        const repoUrl = document.getElementById("repoUrlInput").value.trim();
        const demoUrl = document.getElementById("demoUrlInput").value.trim();

        // Basic validation
        if (!teamName || !projectTitle || !category || !techStack || !description || !repoUrl || !demoUrl) {
            this.showToast("Please complete all required fields.", "⚠️");
            return;
        }

        // Create new project object
        const newProject = {
            id: "proj-" + Date.now().toString().slice(-4),
            teamName: teamName,
            projectTitle: projectTitle,
            category: category,
            techStack: techStack,
            description: description,
            repoUrl: repoUrl,
            demoUrl: demoUrl,
            submittedAt: new Date().toISOString().split("T")[0],
            status: "pending", // Pending evaluation by jury
            scores: {
                innovation: 0,
                technical: 0,
                uiux: 0,
                pitch: 0
            },
            totalScore: 0,
            juryFeedback: ""
        };

        // Add to project list (newest first)
        this.projects.unshift(newProject);
        this.saveProjectsToStorage();

        // Reset form
        document.getElementById("submissionForm").reset();

        // Update views
        this.renderParticipantDashboard();
        this.renderLeaderboard();
        this.renderGallery();

        this.showToast("🎉 Project successfully submitted for Jury evaluation!", "✅");
    },

    /**
     * Render Participant status and existing submission
     */
    renderParticipantDashboard: function() {
        const mySubmissionContent = document.getElementById("mySubmissionContent");
        const statusPill = document.getElementById("participantSubmissionStatus");

        if (!this.currentUser) return;

        // Find if this team has an existing project
        const myProject = this.projects.find(p => 
            p.teamName.toLowerCase() === this.currentUser.username.toLowerCase()
        ) || this.projects[0]; // Fallback to first project for quick demo

        if (myProject) {
            statusPill.innerHTML = myProject.status === "evaluated" 
                ? `<span style="color: #10b981;">Evaluated (${myProject.totalScore}/100)</span>` 
                : `<span style="color: #f59e0b;">Pending Review</span>`;

            mySubmissionContent.innerHTML = `
                <div class="active-project-card">
                    <h4>${this.escapeHTML(myProject.projectTitle)}</h4>
                    <span class="active-project-track">${this.escapeHTML(myProject.category)}</span>
                    <p style="font-size: 0.8rem; color: #64748b; margin-top: 4px;">
                        ${this.escapeHTML(myProject.description.substring(0, 100))}...
                    </p>
                    <div class="active-score-badge">
                        <span>Evaluation Status:</span>
                        <strong style="color: ${myProject.status === 'evaluated' ? '#10b981' : '#f59e0b'}">
                            ${myProject.status === 'evaluated' ? `${myProject.totalScore} / 100 pts` : 'Under Jury Review ⏳'}
                        </strong>
                    </div>
                    ${myProject.juryFeedback ? `
                        <div style="margin-top: 8px; font-size: 0.78rem; background: #f8fafc; padding: 6px; border-radius: 4px; border: 1px solid #e2e8f0;">
                            <strong>Jury Remarks:</strong> "${this.escapeHTML(myProject.juryFeedback)}"
                        </div>
                    ` : ''}
                </div>
            `;
        } else {
            statusPill.innerHTML = `<span>No Submission Yet</span>`;
            mySubmissionContent.innerHTML = `<div class="empty-state-sm">Fill out the form to register your hackathon project.</div>`;
        }
    },

    /**
     * 10. JURY EVALUATION PANEL: Render projects to be evaluated
     */
    renderJudgeProjects: function() {
        const grid = document.getElementById("judgeProjectsGrid");
        const searchInput = document.getElementById("judgeSearchInput");
        const statusFilter = document.getElementById("judgeStatusFilter");
        const pendingCountEl = document.getElementById("juryPendingCount");

        const searchQuery = searchInput ? searchInput.value.toLowerCase().trim() : "";
        const filterValue = statusFilter ? statusFilter.value : "all";

        // Count pending projects
        const pendingTotal = this.projects.filter(p => p.status === "pending").length;
        if (pendingCountEl) pendingCountEl.textContent = pendingTotal;

        // Filter projects
        const filtered = this.projects.filter(p => {
            const matchesSearch = p.projectTitle.toLowerCase().includes(searchQuery) ||
                                  p.teamName.toLowerCase().includes(searchQuery) ||
                                  p.category.toLowerCase().includes(searchQuery);

            const matchesStatus = filterValue === "all" || p.status === filterValue;

            return matchesSearch && matchesStatus;
        });

        if (filtered.length === 0) {
            grid.innerHTML = `
                <div style="grid-column: 1/-1; text-align: center; padding: 3rem; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0;">
                    <p style="font-size: 1.1rem; color: #64748b; margin-bottom: 0.5rem;">🔍 No matching projects found.</p>
                    <span style="font-size: 0.85rem; color: #94a3b8;">Try clearing your search query or switching filters.</span>
                </div>
            `;
            return;
        }

        grid.innerHTML = filtered.map(p => {
            const isEvaluated = p.status === "evaluated";
            const techList = p.techStack.split(",").map(t => `<span class="tech-pill">${this.escapeHTML(t.trim())}</span>`).join("");

            return `
                <div class="project-eval-card">
                    <div>
                        <div class="project-card-header">
                            <h3>${this.escapeHTML(p.projectTitle)}</h3>
                            <span class="track-tag">${this.escapeHTML(p.category)}</span>
                        </div>
                        <div class="team-author">By <strong>${this.escapeHTML(p.teamName)}</strong> • ID: ${p.id}</div>
                        <p class="project-desc">${this.escapeHTML(p.description)}</p>
                        
                        <div class="project-tech-badges">
                            ${techList}
                        </div>

                        <div class="project-links">
                            <a href="${p.repoUrl}" target="_blank" class="link-btn">💻 Code Repo ↗</a>
                            <a href="${p.demoUrl}" target="_blank" class="link-btn">🎥 Live Pitch ↗</a>
                        </div>
                    </div>

                    <div class="project-card-footer">
                        <div class="score-status ${isEvaluated ? 'evaluated' : 'pending'}">
                            ${isEvaluated 
                                ? (p.totalScore >= this.juryCutoffScore && p.isFinalistApproved !== false
                                    ? `⭐ Graded: ${p.totalScore}/100 • 🏅 Finalist`
                                    : `⭐ Graded: ${p.totalScore}/100 • Regular Entry`)
                                : `⏳ Pending Review`}
                        </div>
                        <button class="btn ${isEvaluated ? 'btn-secondary' : 'btn-primary'}" onclick="app.openEvaluationModal('${p.id}')">
                            ${isEvaluated ? '✏️ Update Score' : '⚖️ Evaluate Now'}
                        </button>
                    </div>
                </div>
            `;
        }).join("");
    },

    /**
     * 11. MODAL: Open Evaluation Scorecard for a specific project
     */
    openEvaluationModal: function(projectId) {
        const project = this.projects.find(p => p.id === projectId);
        if (!project) return;

        document.getElementById("evalProjectId").value = project.id;
        document.getElementById("evalModalProjectTitle").textContent = project.projectTitle;
        document.getElementById("evalModalTeamName").textContent = `Team: ${project.teamName} (${project.id})`;
        document.getElementById("evalModalCategory").textContent = project.category;
        document.getElementById("evalModalTech").textContent = project.techStack;
        document.getElementById("evalModalDescription").textContent = project.description;

        document.getElementById("evalModalRepoLink").href = project.repoUrl;
        document.getElementById("evalModalDemoLink").href = project.demoUrl;

        // Populate scoring sliders (default to existing scores or 20 each)
        const scores = project.status === "evaluated" ? project.scores : { innovation: 20, technical: 20, uiux: 20, pitch: 20 };
        document.getElementById("scoreInnovation").value = scores.innovation;
        document.getElementById("scoreTechnical").value = scores.technical;
        document.getElementById("scoreUIUX").value = scores.uiux;
        document.getElementById("scorePitch").value = scores.pitch;

        document.getElementById("evalJuryFeedback").value = project.juryFeedback || "";

        // Reset and set Finalist Checkbox based on project status & jury cutoff
        const checkbox = document.getElementById("evalModalFinalistCheckbox");
        if (checkbox) {
            delete checkbox.dataset.userToggled;
            const currentScore = project.status === "evaluated" ? project.totalScore : 80;
            const meetsCutoff = currentScore >= this.juryCutoffScore;
            checkbox.checked = project.isFinalistApproved !== undefined ? project.isFinalistApproved : meetsCutoff;
        }

        this.updateLiveTotal();

        // Show modal
        document.getElementById("evaluationModal").style.display = "flex";
    },

    /**
     * User manually toggles the Finalist Checkbox inside modal
     */
    handleFinalistCheckboxToggle: function(checked) {
        const checkbox = document.getElementById("evalModalFinalistCheckbox");
        if (checkbox) checkbox.dataset.userToggled = "true";
    },

    /**
     * Update Live Total calculation as jury adjusts sliders
     */
    updateLiveTotal: function() {
        const s1 = parseInt(document.getElementById("scoreInnovation").value) || 0;
        const s2 = parseInt(document.getElementById("scoreTechnical").value) || 0;
        const s3 = parseInt(document.getElementById("scoreUIUX").value) || 0;
        const s4 = parseInt(document.getElementById("scorePitch").value) || 0;

        document.getElementById("valInnovation").textContent = s1;
        document.getElementById("valTechnical").textContent = s2;
        document.getElementById("valUIUX").textContent = s3;
        document.getElementById("valPitch").textContent = s4;

        const total = s1 + s2 + s3 + s4;
        document.getElementById("evalModalTotalScore").textContent = total;

        // Auto-update finalist hint & checkbox if judge has not manually overridden
        const meetsCutoff = total >= this.juryCutoffScore;
        const hintEl = document.getElementById("evalModalCutoffHint");
        const checkbox = document.getElementById("evalModalFinalistCheckbox");

        if (hintEl) {
            hintEl.textContent = meetsCutoff
                ? `Score (${total}) meets current jury cutoff of ${this.juryCutoffScore}+ points`
                : `Score (${total}) is below jury cutoff (${this.juryCutoffScore}+ pts). Can still be manually approved.`;
            hintEl.style.color = meetsCutoff ? "#059669" : "#d97706";
        }

        if (checkbox && !checkbox.dataset.userToggled) {
            checkbox.checked = meetsCutoff;
        }
    },

    /**
     * Close the evaluation modal
     */
    closeEvaluationModal: function() {
        document.getElementById("evaluationModal").style.display = "none";
    },

    /**
     * Save the Jury Evaluation
     */
    handleEvaluationSubmit: function(event) {
        event.preventDefault();

        const projectId = document.getElementById("evalProjectId").value;
        const project = this.projects.find(p => p.id === projectId);
        if (!project) return;

        const s1 = parseInt(document.getElementById("scoreInnovation").value) || 0;
        const s2 = parseInt(document.getElementById("scoreTechnical").value) || 0;
        const s3 = parseInt(document.getElementById("scoreUIUX").value) || 0;
        const s4 = parseInt(document.getElementById("scorePitch").value) || 0;
        const feedback = document.getElementById("evalJuryFeedback").value.trim();

        // Update project state
        project.status = "evaluated";
        project.scores = {
            innovation: s1,
            technical: s2,
            uiux: s3,
            pitch: s4
        };
        project.totalScore = s1 + s2 + s3 + s4;
        project.juryFeedback = feedback;

        // Judge Finalist Approval
        const finalistCheckbox = document.getElementById("evalModalFinalistCheckbox");
        project.isFinalistApproved = finalistCheckbox ? finalistCheckbox.checked : (project.totalScore >= this.juryCutoffScore);

        this.saveProjectsToStorage();
        this.closeEvaluationModal();

        // Refresh views
        this.renderJudgeProjects();
        this.renderLeaderboard();
        this.renderGallery();
        this.renderParticipantDashboard();

        const finalistNote = project.isFinalistApproved ? "🏅 Shortlisted for Finalist Gallery!" : "Added to Leaderboard.";
        this.showToast(`✅ Graded ${project.projectTitle}: ${project.totalScore}/100. ${finalistNote}`, "🏆");
    },

    /**
     * 11B. FINALIST PROJECT GALLERY
     * Renders finalist cards with team name, project demo video link, GitHub repository link, and tech stack tags.
     * Enforces Judge criteria: Only projects evaluated by jury with totalScore >= juryCutoffScore and approved.
     */
    renderGallery: function() {
        const grid = document.getElementById("galleryProjectsGrid");
        const searchInput = document.getElementById("gallerySearchInput");
        const categoryFilter = document.getElementById("galleryCategoryFilter");
        const totalCountEl = document.getElementById("galleryTotalCount");

        if (!grid) return;

        const searchQuery = searchInput ? searchInput.value.toLowerCase().trim() : "";
        const selectedCategory = categoryFilter ? categoryFilter.value : "all";

        // 1. Filter projects strictly by Judge Finalist Criteria
        const qualifiedFinalists = this.projects.filter(p => {
            const isEvaluated = p.status === "evaluated";
            const meetsCutoff = p.totalScore >= this.juryCutoffScore;
            const isApproved = p.isFinalistApproved !== false;
            return isEvaluated && meetsCutoff && isApproved;
        });

        if (totalCountEl) {
            totalCountEl.textContent = qualifiedFinalists.length;
        }

        // 2. Filter qualified finalists by search query and category
        const filtered = qualifiedFinalists.filter(p => {
            const matchesSearch = p.projectTitle.toLowerCase().includes(searchQuery) ||
                                  p.teamName.toLowerCase().includes(searchQuery) ||
                                  p.techStack.toLowerCase().includes(searchQuery) ||
                                  p.category.toLowerCase().includes(searchQuery);

            const matchesCategory = selectedCategory === "all" || p.category === selectedCategory;

            return matchesSearch && matchesCategory;
        });

        if (filtered.length === 0) {
            grid.innerHTML = `
                <div style="grid-column: 1/-1; text-align: center; padding: 3rem; background: #ffffff; border-radius: 12px; border: 1px dashed #cbd5e1;">
                    <p style="font-size: 1.15rem; color: #475569; font-weight: 700; margin-bottom: 0.5rem;">
                        🔍 No projects currently in the Finalist Showcase matching your filter.
                    </p>
                    <p style="font-size: 0.88rem; color: #64748b; max-width: 520px; margin: 0 auto;">
                        <strong>Jury Cutoff Rule:</strong> Submissions require a score of <strong>${this.juryCutoffScore}+ points</strong> set by the Judge to qualify. Currently <strong>${qualifiedFinalists.length}</strong> project(s) meet this benchmark.
                    </p>
                </div>
            `;
            return;
        }

        grid.innerHTML = filtered.map(p => {
            const isEvaluated = p.status === "evaluated";
            const tags = p.techStack.split(",").map(t => `<span class="gallery-tag-chip">${this.escapeHTML(t.trim())}</span>`).join("");

            return `
                <div class="gallery-card">
                    <div>
                        <div class="gallery-card-top-bar">
                            <span class="finalist-tag">🏅 Finalist Entry</span>
                            <span class="track-tag">${this.escapeHTML(p.category)}</span>
                        </div>

                        <div class="gallery-card-content">
                            <h3 class="gallery-project-title">${this.escapeHTML(p.projectTitle)}</h3>
                            <div class="gallery-team-meta">
                                Built by <strong>Team ${this.escapeHTML(p.teamName)}</strong>
                            </div>

                            <p class="gallery-description">
                                ${this.escapeHTML(p.description)}
                            </p>

                            <div class="gallery-tech-section">
                                <span class="gallery-tech-label">Tech Stack Tags:</span>
                                <div class="gallery-tech-tags">
                                    ${tags}
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="gallery-card-footer">
                        <div class="gallery-action-links">
                            <a href="${p.repoUrl}" target="_blank" rel="noopener noreferrer" class="gallery-link-btn btn-github-link">
                                💻 GitHub Repository ↗
                            </a>
                            <a href="${p.demoUrl}" target="_blank" rel="noopener noreferrer" class="gallery-link-btn btn-video-link">
                                🎥 Demo Video Link ↗
                            </a>
                        </div>

                        <div class="gallery-score-row">
                            <span style="color: #64748b;">Jury Status:</span>
                            <span class="score-num">
                                ${isEvaluated ? `⭐ ${p.totalScore} / 100 pts` : `<span style="color: #f59e0b; font-weight: 600;">⏳ Under Review</span>`}
                            </span>
                        </div>
                    </div>
                </div>
            `;
        }).join("");
    },

    /**
     * 12. LEADERBOARD: Sort by totalScore and render podium & table
     */
    renderLeaderboard: function() {
        const tableBody = document.getElementById("leaderboardTableBody");
        const podium = document.getElementById("leaderboardPodium");
        const searchInput = document.getElementById("leaderboardSearchInput");
        const categoryFilter = document.getElementById("leaderboardCategoryFilter");

        if (!tableBody) return;

        const searchQuery = searchInput ? searchInput.value.toLowerCase().trim() : "";
        const selectedCategory = categoryFilter ? categoryFilter.value : "all";

        // Sort projects: Evaluated first with highest totalScore descending, then pending
        const sorted = [...this.projects].sort((a, b) => {
            if (a.status === "evaluated" && b.status !== "evaluated") return -1;
            if (b.status === "evaluated" && a.status !== "evaluated") return 1;
            return b.totalScore - a.totalScore;
        });

        // Filter projects
        const filtered = sorted.filter(p => {
            const matchesSearch = p.projectTitle.toLowerCase().includes(searchQuery) ||
                                  p.teamName.toLowerCase().includes(searchQuery);
            const matchesCategory = selectedCategory === "all" || p.category === selectedCategory;
            return matchesSearch && matchesCategory;
        });

        // 1. Render Top 3 Podium
        const top3Evaluated = sorted.filter(p => p.status === "evaluated").slice(0, 3);
        if (podium) {
            if (top3Evaluated.length >= 3) {
                podium.innerHTML = `
                    <!-- 2nd Place Silver -->
                    <div class="podium-card rank-2">
                        <div class="podium-rank">🥈</div>
                        <span class="track-tag">${this.escapeHTML(top3Evaluated[1].category)}</span>
                        <h3 class="podium-team">${this.escapeHTML(top3Evaluated[1].teamName)}</h3>
                        <p class="podium-project">${this.escapeHTML(top3Evaluated[1].projectTitle)}</p>
                        <div class="podium-score">${top3Evaluated[1].totalScore} pts</div>
                    </div>

                    <!-- 1st Place Gold -->
                    <div class="podium-card rank-1">
                        <div class="podium-rank">🥇</div>
                        <span class="track-tag" style="background: #fef3c7; color: #b45309;">Grand Champion</span>
                        <h3 class="podium-team">${this.escapeHTML(top3Evaluated[0].teamName)}</h3>
                        <p class="podium-project">${this.escapeHTML(top3Evaluated[0].projectTitle)}</p>
                        <div class="podium-score" style="color: #b45309; border-color: #fde68a;">${top3Evaluated[0].totalScore} pts</div>
                    </div>

                    <!-- 3rd Place Bronze -->
                    <div class="podium-card rank-3">
                        <div class="podium-rank">🥉</div>
                        <span class="track-tag">${this.escapeHTML(top3Evaluated[2].category)}</span>
                        <h3 class="podium-team">${this.escapeHTML(top3Evaluated[2].teamName)}</h3>
                        <p class="podium-project">${this.escapeHTML(top3Evaluated[2].projectTitle)}</p>
                        <div class="podium-score">${top3Evaluated[2].totalScore} pts</div>
                    </div>
                `;
            } else {
                podium.innerHTML = `
                    <div style="grid-column: 1/-1; text-align: center; padding: 1.5rem; background: #ffffff; border-radius: 12px; border: 1px dashed #cbd5e1; color: #64748b;">
                        🏆 Top 3 Podium will display here once at least 3 projects are evaluated by the jury.
                    </div>
                `;
            }
        }

        // 2. Render Full Leaderboard Table Rows
        if (filtered.length === 0) {
            tableBody.innerHTML = `
                <tr>
                    <td colspan="9" style="text-align: center; padding: 2.5rem; color: #64748b;">
                        No hackathon entries match your search/filter criteria.
                    </td>
                </tr>
            `;
            return;
        }

        tableBody.innerHTML = filtered.map((p, index) => {
            let rankBadge = `<span class="rank-badge">${index + 1}</span>`;
            if (p.status === "evaluated") {
                if (index === 0) rankBadge = `<span class="rank-badge gold">🥇 1</span>`;
                else if (index === 1) rankBadge = `<span class="rank-badge silver">🥈 2</span>`;
                else if (index === 2) rankBadge = `<span class="rank-badge bronze">🥉 3</span>`;
            }

            const isEvaluated = p.status === "evaluated";

            return `
                <tr>
                    <td class="text-center">${rankBadge}</td>
                    <td class="team-cell">
                        <strong>${this.escapeHTML(p.projectTitle)}</strong>
                        <span>Team: ${this.escapeHTML(p.teamName)}</span>
                    </td>
                    <td>
                        <span class="track-tag">${this.escapeHTML(p.category)}</span>
                    </td>
                    <td class="text-center">${isEvaluated ? p.scores.innovation : '-'}</td>
                    <td class="text-center">${isEvaluated ? p.scores.technical : '-'}</td>
                    <td class="text-center">${isEvaluated ? p.scores.uiux : '-'}</td>
                    <td class="text-center">${isEvaluated ? p.scores.pitch : '-'}</td>
                    <td class="text-center">
                        <span class="score-highlight">${isEvaluated ? p.totalScore : '—'}</span>
                    </td>
                    <td class="text-center">
                        <span class="badge-status ${isEvaluated ? 'evaluated' : 'pending'}">
                            ${isEvaluated ? 'Graded' : 'Pending'}
                        </span>
                    </td>
                </tr>
            `;
        }).join("");
    },

    /**
     * 13. ADMIN PANEL: Compute Hackathon Statistics & Manage Data
     */
    renderAdminDashboard: function() {
        const totalSubmissions = this.projects.length;
        const evaluatedProjects = this.projects.filter(p => p.status === "evaluated");
        const evaluatedCount = evaluatedProjects.length;

        // Highest score calculation
        let highestScore = 0;
        let topTeam = "None";
        if (evaluatedProjects.length > 0) {
            const sorted = [...evaluatedProjects].sort((a, b) => b.totalScore - a.totalScore);
            highestScore = sorted[0].totalScore;
            topTeam = sorted[0].teamName;
        }

        // Average score calculation
        let avgScore = 0;
        if (evaluatedCount > 0) {
            const sum = evaluatedProjects.reduce((acc, curr) => acc + curr.totalScore, 0);
            avgScore = (sum / evaluatedCount).toFixed(1);
        }

        // Update Stat Cards in DOM
        document.getElementById("statTotalSubmissions").textContent = totalSubmissions;
        document.getElementById("statEvaluatedCount").textContent = evaluatedCount;
        document.getElementById("statHighestScore").textContent = `${highestScore}/100`;
        document.getElementById("statTopTeamName").textContent = `Leader: ${topTeam}`;
        document.getElementById("statAverageScore").textContent = avgScore;

        // Render Admin Table
        const tableBody = document.getElementById("adminProjectsTableBody");
        if (tableBody) {
            if (this.projects.length === 0) {
                tableBody.innerHTML = `<tr><td colspan="8" style="text-align: center; padding: 2rem;">No submissions found.</td></tr>`;
                return;
            }

            tableBody.innerHTML = this.projects.map(p => `
                <tr>
                    <td><code>${p.id}</code></td>
                    <td><strong>${this.escapeHTML(p.teamName)}</strong></td>
                    <td>${this.escapeHTML(p.projectTitle)}</td>
                    <td><span class="track-tag">${this.escapeHTML(p.category)}</span></td>
                    <td>
                        <a href="${p.repoUrl}" target="_blank" style="color: #4f46e5; text-decoration: none; margin-right: 6px;">Repo</a>
                        <a href="${p.demoUrl}" target="_blank" style="color: #0ea5e9; text-decoration: none;">Demo</a>
                    </td>
                    <td><strong>${p.status === 'evaluated' ? `${p.totalScore}/100` : '—'}</strong></td>
                    <td>
                        <span class="badge-status ${p.status === 'evaluated' ? 'evaluated' : 'pending'}">
                            ${p.status}
                        </span>
                    </td>
                    <td class="text-center">
                        <button class="action-btn-sm btn-delete" onclick="app.deleteProject('${p.id}')">
                            Delete 🗑️
                        </button>
                    </td>
                </tr>
            `).join("");
        }
    },

    /**
     * Admin Action: Delete a project
     */
    deleteProject: function(projectId) {
        if (!confirm("Are you sure you want to remove this project submission?")) return;

        this.projects = this.projects.filter(p => p.id !== projectId);
        this.saveProjectsToStorage();
        this.renderAdminDashboard();
        this.renderJudgeProjects();
        this.renderLeaderboard();
        this.renderGallery();
        this.showToast("Project entry removed.", "🗑️");
    },

    /**
     * Admin Action: Reset to initial Demo Data
     */
    resetDemoData: function() {
        if (!confirm("Reset all data to default demo hackathon projects?")) return;

        this.projects = [...INITIAL_DEMO_PROJECTS];
        this.saveProjectsToStorage();
        this.renderAdminDashboard();
        this.renderJudgeProjects();
        this.renderLeaderboard();
        this.renderGallery();
        this.renderParticipantDashboard();
        this.showToast("Default sample data restored!", "🔄");
    },

    /**
     * Admin Action: Clear all data
     */
    clearAllData: function() {
        if (!confirm("Warning: This will delete ALL submissions and scores. Proceed?")) return;

        this.projects = [];
        this.saveProjectsToStorage();
        this.renderAdminDashboard();
        this.renderJudgeProjects();
        this.renderLeaderboard();
        this.renderGallery();
        this.showToast("All hackathon data cleared.", "⚠️");
    },

    /**
     * 14. UI Helper: Toast Notifications
     */
    showToast: function(message, icon = "ℹ️") {
        const toast = document.getElementById("toastNotification");
        const msgEl = document.getElementById("toastMessage");
        const iconEl = document.getElementById("toastIcon");

        if (!toast || !msgEl) return;

        msgEl.textContent = message;
        if (iconEl) iconEl.textContent = icon;

        toast.classList.add("show");

        // Clear existing timer if any
        if (this._toastTimer) clearTimeout(this._toastTimer);

        this._toastTimer = setTimeout(() => {
            toast.classList.remove("show");
        }, 3200);
    },

    /**
     * Utility: Prevent XSS / HTML injection in user inputs
     */
    escapeHTML: function(str) {
        if (!str) return "";
        return str
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }
};

// Start application when DOM is ready
document.addEventListener("DOMContentLoaded", () => {
    app.init();
});
