import json
import time
import streamlit as st
from google import genai

MODEL = "gemini-2.5-flash"

st.set_page_config(
page_title="AI Software Company",
page_icon="🤖",
layout="wide"
)

if "GEMINI_API_KEY" not in st.secrets:
    st.error("Gemini API key is missing.")
st.stop()

API_KEY = st.secrets["GEMINI_API_KEY"]

client = genai.Client(api_key=API_KEY)

AGENTS = {
"Product Manager": {
"icon": "📋",
"role": "Product Strategy",
"prompt": """
You are a senior Product Manager.

Analyze the user's software idea and create a complete MVP specification.

Include:

Problem
Target users
Main features
User journey
Functional requirements
Acceptance criteria
Risks and assumptions

Be practical and structured.
"""
},

"UI/UX Designer": {
    "icon": "🎨",
    "role": "UI/UX Design",
    "prompt": """

You are a senior UI/UX Designer.

Use the previous Product Manager output to design the application.

Include:

Main screens
Navigation
Components
User flow
Accessibility
Visual style
UX improvements

Make the design realistic for an MVP.
"""
},

"Developer": {
    "icon": "💻",
    "role": "Software Architecture",
    "prompt": """

You are a senior Python Developer and Software Architect.

Use the previous Product Manager and UI/UX outputs.

Create a technical implementation plan.

Include:

Architecture
Python project structure
Data flow
APIs
Database/data model
Security
Testing
Implementation steps

Do not claim that code was actually executed.
"""
},

"QA Tester": {
    "icon": "🧪",
    "role": "Quality Assurance",
    "prompt": """

You are a senior QA Engineer.

Review the previous Product, UI/UX and Developer outputs.

Include:

Test strategy
Functional test cases
Edge cases
Failure scenarios
Security checks
Acceptance checks

Recommended fixes
"""
},

"Code Reviewer": {
"icon": "🔎",
"role": "Final Technical Review",
"prompt": """
You are a senior Technical Lead.

Review all previous agent outputs.

Include:

Missing requirements
Technical risks
Security risks
Contradictions
Improvements
Final implementation checklist

Give a clear final project summary.
"""
}
}

def run_agent(agent_name, software_idea, previous_context):

    agent = AGENTS[agent_name]

prompt = f"""

{agent["prompt"]}

========================================
SOFTWARE IDEA

{software_idea}

========================================
PREVIOUS AGENT WORK

{previous_context}

========================================
TASK

Work as the {agent_name}.

Use the previous agents' work as context.

Produce a clear professional deliverable.
"""

response = client.models.generate_content(
    model=MODEL,
    contents=prompt
)

if response is None:
    raise RuntimeError("Gemini returned no response.")

if not response.text:
    raise RuntimeError("Gemini returned an empty response.")

    return response.text

with st.sidebar:

    st.title("🤖 AI Software Company")

st.write(
    "Gemini-powered multi-agent software development team."
)

st.divider()

st.subheader("👥 Agent Team")

for name, agent in AGENTS.items():

    st.write(
        f'{agent["icon"]} **{name}**'
    )

    st.caption(
        agent["role"]
    )

st.divider()

st.caption(
    f"Gemini Model: {MODEL}"
)

st.title("🤖 AI Software Company")

st.markdown(
"""

Turn one idea into a complete software blueprint.

📋 Product Manager → 🎨 UI/UX → 💻 Developer → 🧪 QA → 🔎 Code Reviewer
"""
)

st.subheader("🚀 Start Your Project")

software_idea = st.text_area(
"Describe your software idea",
placeholder=(
"Example: Build an AI platform that helps "
"university students find teammates for projects."
),
height=150
)

if st.button(
"🚀 Launch AI Team",
type="primary",
use_container_width=True
):

    if not software_idea.strip():

        st.warning(
             "Please enter your software idea first."
    )

        st.stop()

results = {}

previous_context = ""

progress = st.progress(0)

status = st.empty()

total_agents = len(AGENTS)


for index, agent_name in enumerate(
    AGENTS,
    start=1
):

    agent = AGENTS[agent_name]

    status.info(
        f'{agent["icon"]} {agent_name} is working...'
    )

    try:

        output = run_agent(
            agent_name,
            software_idea,
            previous_context
        )

    except Exception as error:

        st.error(
            f"❌ {agent_name} failed."
        )

        st.exception(error)

        st.stop()

    results[agent_name] = output

    previous_context += (
        "\n\n"
        "========================================\n"
        f"{agent_name}\n"
        "========================================\n"
        f"{output}"
    )

    progress.progress(
        index / total_agents
    )

    time.sleep(0.3)


status.success(
    "🎉 All AI agents completed successfully!"
)

st.session_state["results"] = results

st.session_state["software_idea"] = software_idea

if "results" in st.session_state:

    results = st.session_state["results"]

st.divider()

st.header("🧩 AI Team Results")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Agents",
        len(results)
    )

with col2:

    st.metric(
        "Workflow",
        "Sequential"
    )

with col3:

    st.metric(
        "Shared Context",
        "Enabled"
    )

st.divider()

tabs = st.tabs(
    [
        f'{AGENTS[name]["icon"]} {name}'
        for name in results
    ]
)

for tab, agent_name in zip(
    tabs,
    results
):

    with tab:

        st.subheader(
            f'{AGENTS[agent_name]["icon"]} {agent_name}'
        )

        st.caption(
            AGENTS[agent_name]["role"]
        )

        st.markdown(
            results[agent_name]
        )

st.divider()

st.header("📦 Final Project Report")

final_report = {
    "software_idea": st.session_state["software_idea"],
    "model": MODEL,
    "provider": "Google Gemini",
    "agents": results
}

st.download_button(
    label="📥 Download Complete Report",
    data=json.dumps(
        final_report,
        indent=2,
        ensure_ascii=False
    ),
    file_name="ai_software_company_report.json",
    mime="application/json",
    use_container_width=True
)

st.divider()

st.caption(
"Python + Streamlit + Google Gemini | "
"Multi-Agent Hackathon Project"
)

