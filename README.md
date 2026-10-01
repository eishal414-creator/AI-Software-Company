# 🤖 AI Software Company — Gemini Multi-Agent

A Python + Streamlit hackathon project powered by Google Gemini.

The application acts like a virtual software company. The user provides a software idea, and five specialized AI agents collaborate to turn that idea into a complete software blueprint.

---

# 👥 AI Agent Team

The application contains five specialized agents:

## 📋 Product Manager

Analyzes the user's idea and creates:

- Problem definition
- Target users
- MVP features
- User journey
- Functional requirements
- Acceptance criteria
- Assumptions and risks

---

## 🎨 UI/UX Designer

Receives the Product Manager's output and creates:

- Pages
- Screens
- Components
- Navigation
- User flow
- Accessibility considerations
- Visual direction

---

## 💻 Developer

Receives the Product Manager and UI/UX outputs and creates:

- Software architecture
- Python modules
- Data flow
- APIs
- Data model
- Security considerations
- Testing approach
- Project structure

---

## 🧪 QA Tester

Receives the previous agents' work and checks:

- Functional test cases
- Edge cases
- Failure scenarios
- Security issues
- Acceptance criteria
- Potential risks

---

## 🔎 Code Reviewer

Receives the complete team context and performs the final review.

It identifies:

- Missing requirements
- Technical risks
- Security risks
- Contradictions
- Priority improvements
- Final implementation checklist

---

# 🔗 Multi-Agent Workflow

The agents work sequentially.

```text
                 USER
                   |
                   v
          📋 PRODUCT MANAGER
                   |
                   v
            🎨 UI/UX DESIGNER
                   |
                   v
              💻 DEVELOPER
                   |
                   v
               🧪 QA TESTER
                   |
                   v
             🔎 CODE REVIEWER
                   |
                   v
             📦 FINAL REPORT
