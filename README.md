# 🤖 AI Software Company — Hackathon Edition

A polished **multi-agent AI application** built with Python and Streamlit.

The application acts like a virtual software company. Give it a software idea and five specialized AI agents collaborate sequentially to turn the idea into a software blueprint.

## ✨ What makes it multi-agent?

This is not five independent chatbots.

The workflow is:

```text
                    USER
                      │
                      ▼
              ┌───────────────┐
              │ Product Agent │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   UX Agent    │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Developer     │
              │    Agent      │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   QA Agent    │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Code Reviewer │
              └───────┬───────┘
                      │
                      ▼
                FINAL REPORT
```

Each agent receives the previous agents' outputs as **shared context**.

---

# 👥 Agent Team

### 📋 1. Product Manager
Transforms the raw idea into:

- Problem definition
- Target users
- MVP features
- User journey
- Requirements
- Acceptance criteria

### 🎨 2. UI/UX Designer
Uses the product plan to create:

- Screens
- Components
- Navigation
- User flow
- Accessibility considerations
- Visual direction

### 💻 3. Developer
Uses the product + UX plans to create:

- Technical architecture
- Python modules
- Data flow
- APIs
- Data model
- Security considerations
- Testing approach

### 🧪 4. QA Tester
Reviews the plans and creates:

- Test strategy
- Functional test cases
- Edge cases
- Failure scenarios
- Security checks
- Acceptance checks

### 🔎 5. Code Reviewer
Reviews the complete team output and identifies:

- Missing requirements
- Contradictions
- Technical risks
- Security risks
- Priority improvements
- Final implementation checklist

---

# 📁 Files

```text
ai_software_company/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 💻 Run Locally

## Step 1 — Install Python

Install Python 3.10 or newer.

Check:

```bash
python --version
```

---

## Step 2 — Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Step 4 — Configure your API key

Create a file called:

```text
.env
```

inside the project folder.

Add:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

Never upload `.env` to GitHub.

Create `.gitignore` with:

```text
.env
venv/
__pycache__/
```

---

# ▶️ Step 5 — Run the app

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

# 🧪 How to Demo It

Use a simple but impressive example:

> I want to build an AI platform that helps university students find teammates for projects.

Click:

**🚀 Launch AI Team**

Then show the judges the workflow.

### Product Manager

The first agent turns the raw idea into a structured product.

### UI/UX Designer

The second agent receives the product plan and designs the interface.

### Developer

The third agent receives both previous outputs and turns them into a technical architecture.

### QA Tester

The fourth agent tries to find bugs, edge cases and risks.

### Code Reviewer

The final agent reviews the entire team's work and creates the final implementation checklist.

This demonstrates **agent-to-agent context passing**.

---

# 🚀 Deploy on Streamlit Community Cloud

## 1. Create a GitHub repository

Create a repository such as:

```text
ai-software-company
```

Upload:

```text
app.py
requirements.txt
README.md
```

Do not upload:

```text
.env
```

---

## 2. Open Streamlit Community Cloud

Open Streamlit Community Cloud and sign in using GitHub.

Create a new app.

Select:

```text
Repository: your GitHub repository
Branch: main
Main file: app.py
```

Deploy the application.

---

# 🔐 3. Add the API key to Streamlit Secrets

Open your deployed app's settings and find **Secrets**.

Add:

```toml
OPENAI_API_KEY = "your_api_key_here"
OPENAI_MODEL = "gpt-4o-mini"
```

Save the secrets and restart/redeploy the application.

The app reads the secret through the environment.

---

# 🎨 UI Features

The hackathon edition includes:

- Modern dashboard
- Agent team sidebar
- Agent role cards
- Project input area
- Example projects
- Live progress bar
- Agent activity status
- Sequential workflow
- Individual agent tabs
- Shared-context collaboration
- Team metrics
- Downloadable JSON report
- New Project button
- Responsive Streamlit layout

---

# 🏆 Ideas for an even stronger hackathon version

If you have extra time, add:

### 1. Agent retry loop

If QA finds a problem:

```text
QA → Developer → QA
```

instead of ending immediately.

### 2. Human approval

Add:

```text
Agent proposal
      ↓
Human approval
      ↓
Next agent
```

This is useful before allowing an agent to perform real actions.

### 3. Parallel agents

For research-heavy tasks:

```text
             ┌→ Market Research
User → PM ───┼→ Competitor Research
             └→ User Research
                    ↓
              Synthesis Agent
```

### 4. Persistent projects

Add SQLite/PostgreSQL so users can save project sessions.

### 5. Code generation

Add a separate Developer/Builder stage that produces project files.

**Important:** Do not automatically execute arbitrary AI-generated code. Use a sandbox/container and human approval.

### 6. Visual architecture

Generate a visual diagram showing how the agents communicate.

### 7. Agent memory

Allow agents to remember project-specific decisions throughout a session.

---

# ⚠️ Security

This is a hackathon prototype.

Before production, add:

- Authentication
- Rate limiting
- Logging
- Database security
- Input validation
- Cost controls
- Secret management
- Sandboxed code execution
- Human approval for destructive actions

The current Developer agent only **generates a technical plan/code structure as text**. It does not execute arbitrary generated code.

---

# 🧰 Tech Stack

- Python
- Streamlit
- OpenAI API
- python-dotenv
- Multi-agent sequential orchestration

---

# 🎤 30-second hackathon pitch

> "We built an AI Software Company where specialized AI agents work together like a real development team. A Product Manager first understands the user's idea, then a UX Designer turns it into an interface, a Developer creates the architecture, QA tries to break the solution, and finally a Code Reviewer evaluates the entire project. Unlike separate chatbots, every agent receives the previous team's work as context, allowing them to collaborate toward one final software blueprint."

---

## License

Hackathon prototype. Modify and extend as needed.
