"""Tool schemas for the RCA agent."""

GET_LOGS_SCHEMA = {
    "name": "get_logs",
    "description": (
        "Fetch application logs for a specific service within a recent "
        "time window. Use this when you need to see error messages, "
        "stack traces, or log patterns to understand what went wrong."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "service": {
                "type": "string",
                "description": (
                    "Name of the service to fetch logs for (e.g. 'payment-api')."
                ),
            },
            "query": {
                "type": "string",
                "description": (
                    "Optional search term to filter logs (e.g. 'error', 'timeout')."
                ),
            },
            "minutes_back": {
                "type": "integer",
                "description": (
                    "How many minutes of log history to fetch, counting back from now."
                ),
            },
        },
        "required": ["service", "minutes_back"],
    },
}

GET_METRICS_SCHEMA = {
    "name": "get_metrics",
    "description": (
        "Fetch time-series metrics using a PromQL-style query. Use this "
        "when you need to see trends, spikes, or resource usage over time."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "promql_query": {
                "type": "string",
                "description": "A PromQL-style query for the metric to fetch.",
            },
            "minutes_back": {
                "type": "integer",
                "description": (
                    "How many minutes of metric history to fetch, "
                    "counting back from now."
                ),
            },
        },
        "required": ["promql_query", "minutes_back"],
    },
}
