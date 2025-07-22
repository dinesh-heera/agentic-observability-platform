def route_by_intent(intent: str):
    if intent in ["error_logs", "latency_issue"]:
        return "splunk"
    elif intent == "apm_health_check":
        return "splunk_apm"
    elif intent == "traceability":
        return "splunk_epm"
    elif intent == "performance_issue":
        return "appdynamics"
    else:
        return "default"