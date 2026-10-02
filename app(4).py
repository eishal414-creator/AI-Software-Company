import json
import time

import streamlit as st
from google import genai

# ============================================================

# CONFIGURATION

# ============================================================

MODEL = "gemini-2.5-flash"

# ============================================================

# PAGE CONFIG

# ============================================================

st.set_page_config(
page_title="AI Software Company",
page_icon="🤖",
layout="wide",
)

# ============================================================

# GET GEMINI API KEY

# ============================================================

try:
API_KEY = st.secrets["GEMINI_API_KEY"]
except Exception:
API_KEY = None

if not API_KEY:
st.error("❌ Gemini API key is missing.")

```
st.info(
    """
    Open your Streamlit app settings and add this secret:

    GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

    Do not put your real API key directly inside app.py.
    """
)

st.stop()
```

# ============================================================

# GEMINI CLIENT

# ============================================================

try:
client = genai.Client(
api_key=API_KEY
)

except Exception as error:
st.error("❌ Gemini client could not be created.")
st.exception(error)
st.stop()

# ============================================================

# AGENTS

# ============================================================

AGENTS = {

```
"Product Manager": {
    "icon": "📋",
    "role": "Product Strategy",

    "prompt": """
```

You are a senior Product Manager.

Analyze the user's software idea and create a practical MVP specification.

Include:

1. Problem
2. Target users
3. Main features
4. User journey
5. Functional requirements
6. Acceptance criteria
7. Risks and assumptions

Be clear, practical and structured.
"""
},

```
"UI/UX Designer": {
    "icon": "🎨",
    "role": "UI/UX Design",

    "prompt": """
```

You are a senior UI/UX Designer.

Use the previous Product Manager output to design the application.

Include:

1. Main screens
2. Navigation
3. Components
4. User flow
5. Accessibility
6. Visual style
7. UX improvements

Make the design realistic for an MVP.
"""
},

```
"Developer": {
    "icon": "💻",
    "role": "Software Architecture",

    "prompt": """
```

You are a senior Python Developer and Software Architect.

Use the previous Product Manager and UI/UX outputs.

Create a technical implementation plan.

Include:

1. Architecture
2. Python project structure
3. Data flow
4. APIs
5. Database/data model
6. Security
7. Testing
8. Implementation steps

Do not claim that code was actually executed.
"""
},

```
"QA Tester": {
    "icon": "🧪",
    "role": "Quality Assurance",

    "prompt": """
```

You are a senior QA Engineer.

Review the previous Product, UI/UX and Developer outputs.

Find potential problems.

Include:

1. Test strategy
2. Functional test cases
3. Edge cases
4. Failure scenarios
5. Security checks
6. Acceptance checks
7. Recommended fixes
   """
   },

   "Code Reviewer": {
   "icon": "🔎",
   "role": "Final Technical Review",

   ```
    "prompt": """
   ```

You are a senior Technical Lead.

Review all previous agent outputs.

Create the final technical review.

Include:

1. Missing requirements
2. Technical risks
3. Security risks
4. Contradictions
5. Improvements
6. Final implementation checklist

Give a clear final project summary.
"""
}
}

# ============================================================

# GEMINI FUNCTION

# ============================================================

def run_agent(agent_name, software_idea, previous_context):

```
agent = AGENTS[agent_name]

prompt = f"""
```

{agent["prompt"]}

==================================================
SOFTWARE IDEA
=============

{software_idea}

==================================================
PREVIOUS AGENT WORK
===================

{previous_context}

==================================================
TASK
====

Work as the {agent_name}.

Use the previous agents' work as context.

Do not ignore important information.

Produce a clear professional deliverable.
"""

```
response = client.models.generate_content(
    model=MODEL,
    contents=prompt,
)

if response is None:
    raise RuntimeError(
        "Gemini returned no response."
    )

text = getattr(
    response,
    "text",
    None
)

if not text:
    raise RuntimeError(
        "Gemini returned an empty response."
    )

return text
```

# ============================================================

# SIDEBAR

# ============================================================

with st.sidebar:

```
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
```

# ============================================================

# HEADER

# ============================================================

st.title("🤖 AI Software Company")

st.markdown(
"""

### Turn one idea into a complete software blueprint.

A team of specialized AI agents works together:

**📋 Product Manager → 🎨 UI/UX → 💻 Developer → 🧪 QA → 🔎 Code Reviewer**
"""
)

# ============================================================

# USER INPUT

# ============================================================

st.subheader("🚀 Start Your Project")

software_idea = st.text_area(
"Describe your software idea",

```
placeholder=(
    "Example: Build an AI platform that helps "
    "university students find teammates for projects."
),

height=150,
```

)

# ============================================================

# RUN TEAM

# ============================================================

if st.button(
"🚀 Launch AI Team",
type="primary",
use_container_width=True,
):

```
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


# ========================================================
# RUN AGENTS
# ========================================================

for index, agent_name in enumerate(
    AGENTS.keys(),
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
            previous_context,
        )

        results[agent_name] = output

        previous_context += (
            "\n\n"
            "==============================\n"
            f"{agent_name}\n"
            "==============================\n"
            f"{output}"
        )

    except Exception as error:

        st.error(
            f"❌ {agent_name} failed."
        )

        st.exception(error)

        st.stop()


    progress.progress(
        index / total_agents
    )

    time.sleep(0.3)


status.success(
    "🎉 All AI agents completed successfully!"
)


# ========================================================
# SAVE RESULTS
# ========================================================

st.session_state["results"] = results

st.session_state["software_idea"] = software_idea
```

# ============================================================

# DISPLAY RESULTS

# ============================================================

if "results" in st.session_state:

```
results = st.session_state["results"]

st.divider()

st.header("🧩 AI Team Results")


# ========================================================
# METRICS
# ========================================================

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


# ========================================================
# TABS
# ========================================================

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


# ========================================================
# FINAL REPORT
# ========================================================

st.divider()

st.header("📦 Final Project Report")


final_report = {
    "software_idea":
        st.session_state["software_idea"],

    "model":
        MODEL,

    "provider":
        "Google Gemini",

    "agents":
        results,
}


st.download_button(
    label="📥 Download Complete Report",

    data=json.dumps(
        final_report,
        indent=2,
        ensure_ascii=False,
    ),

    file_name=(
        "ai_software_company_report.json"
    ),

    mime="application/json",

    use_container_width=True,
)
```

# ============================================================

# FOOTER

# ============================================================

st.divider()

st.caption(
"Python + Streamlit + Google Gemini | "
"Multi-Agent Hackathon Project"
)

### 3. Streamlit Sec
