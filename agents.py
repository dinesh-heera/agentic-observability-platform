from utils.llm import call_llm
import splunklib.client as client
import splunklib.results as results
import asyncio
import requests

async def classify_intent(state):
    intent = await call_llm(f"Classify this intent: {state.prompt}")
    state.context["intent"] = intent.strip().lower()
    return state

async def generate_splunk_query(state):
    query = await call_llm(f"Generate a Splunk SPL to diagnose: {state.prompt}")
    state.context["spl_query"] = query
    return state

async def run_splunk_query(state):
    service = client.connect(host="localhost", port=8089, username="admin", password="pass")
    job = service.jobs.create(state.context["spl_query"])
    while not job.is_done():
        await asyncio.sleep(2)
    for result in results.ResultsReader(job.results()):
        state.context["splunk_result"] = result
    return state

async def do_rca(state):
    raw_data = str(state.context["splunk_result"])
    rca = await call_llm(f"Do RCA based on this: {raw_data}")
    state.context["rca"] = rca
    return state

async def create_jira_ticket(state):
    rca = state.context["rca"]
    jira_resp = requests.post(
        "https://your-domain.atlassian.net/rest/api/3/issue",
        auth=("email@example.com", "jira_token"),
        json={
            "fields": {
                "project": {"key": "OBS"},
                "summary": "Auto RCA - Observability",
                "description": rca,
                "issuetype": {"name": "Bug"}
            }
        }
    )
    ticket_url = f"https://your-domain.atlassian.net/browse/{jira_resp.json()['key']}"
    state.context["final_response"] = f"🧠 RCA: {rca}\n🎟️ Jira Ticket: {ticket_url}"
    return state