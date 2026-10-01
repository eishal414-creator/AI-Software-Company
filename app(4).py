import os
import json
import time
from typing import Dict

import streamlit as st
import googles.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Software Company",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Custom UI
# -----------------------------
st.markdown(
    """
    <style>
    .main {
        padding-top: 1.5rem;
    }

    .hero {
        padding: 1.8rem;
        border-radius: 20px;
        border: 1px solid rgba(128,128,128,.25);
        margin-bottom: 1.2rem;
    }

    .agent-card {
        padding: 1rem;
        border: 1px solid rgba(128,128,128,.25);
        border-radius: 14px;
        margin-bottom: .7rem;
        background: rgba(128,128,128,.04);
    }

    .metric-card {
        padding: 1rem;
        border: 1px solid rgba(128,128,128,.25);
        border-radius: 14px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Gemini Configuration
# -----------------------------
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

# -----------------------------
# Agent Definitions
# -----------------------------
AGENTS = {
    "Product Manager": {
        "icon": "📋",
        "role": "Product strategy",
        "system": """
You are a senior Product Manager.

Turn the user's software idea into a realistic MVP specification.

Return:
1. Problem
2. Target users
3. Core features
4. User journey
5. Functional requirements
6. Acceptance criteria
7. Assumptions and risks

Be structured, practical and concise.
""",
    },

    "UI/UX Designer": {
        "icon": "🎨",
        "role": "Interface & experience",
        "system": """
You are a senior UI/UX Designer.

Use the Product Manager's plan to design a practical modern interface.

Return:
1. Pages/screens
2. Main components
3. Navigation
4. User flow
5. Accessibility considerations
6. Visual direction
7. Important UX decisions

Keep the design realistic for an MVP.
""",
    },

    "Developer": {
        "icon": "💻",
        "role": "Technical architecture",
        "system": """
You are a senior Python software architect.

Use the product and UX plans to create a realistic implementation plan.

Return:
1. Architecture
2. Python modules
3. Data flow
4. APIs/services
5. Data model
6. Security considerations
7. Testing approach
8. Representative Python project structure

Do not claim that code was executed.
""",
    },

    "QA Tester": {
        "icon": "🧪",
        "role": "Quality assurance",
        "system": """
You are a senior QA engineer.

Review the product, UX and technical plans.

Return:
1. Test strategy
2. Functional test cases
3. Edge cases
4. Failure scenarios
5. Security checks
6. Acceptance checks
7. Risks and recommended fixes

Try to find problems before launch.
""",
    },

    "Code Reviewer": {
        "icon": "🔎",
        "role": "Final technical review",
        "system": """
You are a senior technical lead and code reviewer.

Review all previous agent outputs as one software-team deliverable.

Return:
1. What is consistent
2. Missing requirements
3. Technical risks
4. Security risks
5. Contradictions
6. Highest-priority improvements
7. Final implementation checklist

Give a clear final recommendation for implementation steps.
""",
    },
}


# -----------------------------
# Gemini Agent Function
# -----------------------------
def run_agent(
    client,
    agent_name: str,
    idea: str,
    context: str,
) -> str:

    agent = AGENTS[agent_name]

    prompt = f"""
{agent["system"]}

========================
SOFTWARE IDEA
========================

{idea}

========================
PREVIOUS TEAM CONTEXT
========================

{context if context else "No previous agent output. You are the first specialist."}

========================
YOUR TASK
========================

Produce your specialist deliverable for the software team.

Remember:
- Do not repeat unnecessary information.
- Use clear headings.
- Build on previous agents' work.
- Identify issues when necessary.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
    )

    return response.text


# -----------------------------
# Reset Project
# -----------------------------
def reset_project():
    for key in [
        "results",
        "idea",
        "completed",
    ]:
        st.session_state.pop(key, None)


# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.markdown("## 🤖 AI Software Company")

    st.caption(
        "Gemini-powered multi-agent software team"
    )

    st.divider()

    st.markdown("### 👥 Agent Team")

    for name, data in AGENTS.items():

        st.markdown(
            f"""
            <div class="agent-card">
                <b>{data["icon"]} {name}</b>
                <br>
                <small>{data["role"]}</small>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    if st.button(
        "🗑️ New Project",
        use_container_width=True,
    ):
        reset_project()
        st.rerun()

    st.caption(
        f"Gemini model: {MODEL}"
    )


# -----------------------------
# Hero Section
# -----------------------------
st.markdown(
    """
    <div class="hero">

        <h1>🤖 AI Software Company</h1>

        <p style="font-size:1.05rem;">
        Describe an app idea and let a team of specialized
        Gemini AI agents transform it into a complete
        software blueprint.
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Metrics
# -----------------------------
cols = st.columns(4)

metrics = [
    ("👥", "5", "AI Agents"),
    ("🔗", "Sequential", "Collaboration"),
    ("🧠", "Shared", "Context"),
    ("📦", "1", "Final Report"),
]

for col, (icon, value, label) in zip(
    cols,
    metrics,
):

    with col:

        st.markdown(
            f"""
            <div class="metric-card">

                <h2>
                    {icon} {value}
                </h2>

                <span>
                    {label}
                </span>

            </div>
            """,
            unsafe_allow_html=True,
        )


st.write("")


# -----------------------------
# API Key Check
# -----------------------------
if not API_KEY:

    st.error(
        "❌ GEMINI_API_KEY is missing."
    )

    st.info(
        """
        Add GEMINI_API_KEY to your
        Streamlit Secrets.

        Example:

        GEMINI_API_KEY = "your_key_here"
        """
    )

    st.stop()


# -----------------------------
# Gemini Client
# -----------------------------
client = genai.Client(
    api_key=API_KEY
)


# -----------------------------
# Project Input
# -----------------------------
st.markdown(
    "## 🚀 Start a New Software Project"
)

examples = [
    "Build a food delivery app for university students.",
    "Build an AI study planner for students.",
    "Build a marketplace connecting local service providers with customers.",
    "Build a project management app for university teams.",
]

selected = st.selectbox(
    "Quick Example",
    ["Choose an example..."] + examples,
)

idea = st.text_area(
    "What do you want to build?",

    value=(
        ""
        if selected == "Choose an example..."
        else selected
    ),

    placeholder=(
        "Example: Build an AI platform that "
        "helps students find teammates for "
        "university projects."
    ),

    height=130,
)


# -----------------------------
# Launch Team
# -----------------------------
if st.button(
    "🚀 Launch Gemini AI Team",
    type="primary",
    use_container_width=True,
):

    if not idea.strip():

        st.warning(
            "Please describe your software idea first."
        )

    else:

        st.session_state["idea"] = idea.strip()

        st.session_state["results"] = {}

        st.session_state["completed"] = []

        context = ""

        st.markdown(
            "## ⚡ Agent Activity"
        )

        progress = st.progress(0)

        status = st.empty()

        total_agents = len(AGENTS)

        for index, agent_name in enumerate(
            AGENTS.keys(),
            start=1,
        ):

            data = AGENTS[agent_name]

            status.markdown(
                f"""
                ### {data["icon"]} {agent_name} is working...

                `{data["role"]}`
                """
            )

            try:

                output = run_agent(
                    client,
                    agent_name,
                    idea.strip(),
                    context,
                )

                st.session_state[
                    "results"
                ][agent_name] = output

                st.session_state[
                    "completed"
                ].append(agent_name)

                # Pass this agent's output
                # to the next agent.
                context += (
                    f"\n\n"
                    f"--- {agent_name} ---\n"
                    f"{output}"
                )

            except Exception as exc:

                st.error(
                    f"{agent_name} failed: {exc}"
                )

                break

            progress.progress(
                index / total_agents
            )

            time.sleep(0.25)

        status.success(
            "✅ Gemini AI team workflow completed."
        )


# -----------------------------
# Results
# -----------------------------
if st.session_state.get("results"):

    results: Dict[
        str,
        str
    ] = st.session_state["results"]

    st.divider()

    st.markdown(
        "## 🧩 Team Workspace"
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Agents completed",
        f"{len(results)}/5",
    )

    c2.metric(
        "Collaboration",
        "Sequential",
    )

    c3.metric(
        "Shared context",
        "Enabled",
    )

    # Agent tabs
    tabs = st.tabs(
        [
            f"{AGENTS[name]['icon']} {name}"
            for name in results.keys()
        ]
    )

    for tab, (
        name,
        output,
    ) in zip(
        tabs,
        results.items(),
    ):

        with tab:

            st.markdown(
                f"""
                ### {AGENTS[name]["icon"]}
                {name}
                """
            )

            st.caption(
                AGENTS[name]["role"]
            )

            st.markdown(output)

    # -------------------------
    # Final Report
    # -------------------------
    st.divider()

    st.markdown(
        "## 📦 Final Project Report"
    )

    report = {
        "software_idea":
            st.session_state.get(
                "idea",
                idea,
            ),

        "provider":
            "Google Gemini",

        "model":
            MODEL,

        "agents":
            results,
    }

    st.download_button(
        "📥 Download Complete Team Report",

        data=json.dumps(
            report,
            indent=2,
            ensure_ascii=False,
        ),

        file_name=(
            "gemini_ai_software_company_report.json"
        ),

        mime="application/json",

        use_container_width=True,
    )

    st.success(
        "🎉 The AI software team completed "
        "a collaborative planning cycle."
    )


# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "Hackathon prototype • Python + Streamlit + "
    "Google Gemini • Generated code is reviewed "
    "as text and is not automatically executed."
)
