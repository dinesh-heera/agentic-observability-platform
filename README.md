# agentic-observability-platform

# 🧠 Agentic AI-Powered Observability Platform (LangGraph + Chainlit + Splunk + AppD)

This is a modular, scalable **AI-powered observability assistant** that takes natural language prompts from users and automates:

- 🔍 Intent classification
- 📊 Splunk query generation & execution
- 🧠 LLM-based root cause analysis (RCA)
- 🧾 JIRA ticket creation with RCA
- 📸 Splunk APM dashboard screenshots (via Playwright)
- 🔄 Full context retention across chat history

---

## Key Features

| Feature | Description |
|--------|-------------|
| ✅ **LangGraph agent orchestration** | Intent-based branching & agent sequencing |
| 💬 **Chainlit chat interface** | Interactive, real-time prompt experience |
| 🤖 **LLM-based RCA** | Generates RCA summaries based on telemetry |
| 📈 **Splunk Cloud** | Executes SPL queries on logs/metrics |
| 📊 **Splunk APM + EPM** | Health check, traceability, dashboard insights |
| 📉 **AppDynamics Integration** | App node health and metrics |
| 🧾 **JIRA Automation** | Auto-create detailed RCA-linked tickets |
| 📸 **Playwright APM screenshots** | Get dashboards & display inline in chat |
| 🧠 **MCP (Model Context Protocol)** | Retains historical context for smarter responses |
| 🔁 **Retries + Logging** | Resilient execution with error tracking |

---

## 🏗️ Architecture Overview

```mermaid
flowchart TD
    U(User Prompt) -->|Chat| Chainlit
    Chainlit --> LangGraphEngine
    LangGraphEngine --> MCP((Historical Context))
    LangGraphEngine --> IntentClassifier
    IntentClassifier -->|branch| SplunkAgent
    SplunkAgent --> LLM_RCA
    LLM_RCA --> JiraAgent
    LangGraphEngine --> SplunkAPMAgent --> PlaywrightScreenshot
    LangGraphEngine --> AppDynamicsAgent
    JiraAgent --> Chainlit
    PlaywrightScreenshot --> Chainlit
 ---


## 💡 Key Features

📁 agentic-observability-platform/
├── agents.py                  # All LLM + platform agents
├── langgraph_engine.py       # LangGraph orchestration logic
├── chat_interface.py         # Chainlit app frontend
├── mcp_context.py            # Model context protocol for history
├── utils/
│   ├── llm.py                # LLM call abstraction
│   ├── logger.py             # Rotating file logger
│   └── playwright_utils.py  # Capture APM dashboard screenshot
├── logs/                     # Rotating error logs
└── requirements.txt

🚀 Getting Started
1. Clone the Repo

git clone https://github.com/your-org/agentic-observability-platform.git
cd agentic-observability-platform

2. Install Requirements

pip install -r requirements.txt

3. Run Chainlit

chainlit run chat_interface.py

🧪 Example Prompts

"Check the root cause of login failures in the last 4 hours"
"Create RCA and raise JIRA for recent payment errors"
"Show me dashboard of health status for all APM services"
"Trace all activity for session abc123 using Splunk EPM"
"Check metrics for AppDynamics node xyz-node"

🧠 Historical Context (MCP)

All user prompts are fed into an MCP (Model Context Protocol) that retains past messages, enabling:
Better RCA follow-ups
Clarifications based on previous interactions
Intent-aware workflows

🔐 Configuration
Update .env or inline config (temporarily):

Splunk:

Host: localhost, Port: 8089

Username: admin, Password: pass

JIRA:

Auth: email@example.com and API token

Project key: OBS

Playwright APM Dashboard URL:

Set DASHBOARD_URL in playwright_utils.py

🔁 Error Logging & Retry
All agent errors are logged to logs/observability.log

Automatic retries with exponential backoff for:

JIRA ticket creation

Splunk query execution

Playwright dashboard screenshot

🧩 Extensibility Roadmap
You can easily extend this platform to:

✅ Add Kubernetes service health checks

✅ Integrate NewRelic, Dynatrace, or Datadog

📈 Export insights to dashboards like Grafana

🤖 Add action agents for auto-remediation

📜 License
MIT License

✨ Credits
Built using:
LangGraph
Chainlit
Splunk SDK
Playwright
OpenAI/Gemini LLMs
AppDynamics
