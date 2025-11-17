from google.adk.agents.callback_context import CallbackContext
from google.genai.types import Content, Part


def check_for_malicious_content(user_input: str) -> bool:
    """
    Placeholder function for detection of harmful content or injection attempts.
    In a production system, this would call an external service
    (like Model Armor or a classifier) or policy engine.
    """
    # Example detection of prompt injection attempts
    injection_keywords = [
        "ignore previous instructions",
        "act as root",
        "reveal private key",
    ]

    # Example detection of slang/harmful content (toxicity/policy violation)
    toxic_keywords = ["unacceptable_slang_1", "profanity_2"]

    if any(
        keyword in user_input.lower() for keyword in injection_keywords + toxic_keywords
    ):
        return True  # Malicious/Harmful input detected
    return False


# --- Implement the Callback Function ---


def enforce_input_guardrail_callback(callback_context: CallbackContext):
    """
    Executes before the LLM call. Inspects the user's prompt (Input Filtering)
    and blocks or modifies the request if policy is violated.
    """

    try:
        user_query = callback_context.user_content.parts[0].text
    except AttributeError:
        return None

    if check_for_malicious_content(user_query):
        # If malicious content is detected:

        # Enforce the hard-stop policy by overriding the prompt to the model
        # This prevents the malicious query from reaching the core reasoning engine.
        response_content = Content(
            parts=[
                Part(
                    text="I cannot process that request due to a policy violation. Please rephrase your query."
                )
            ]
        )
        return response_content
        # If safe, return None to proceed with agent execution
    return None

    # Note: In a production framework, you might raise an exception to halt
    # the entire agent execution or utilize a dedicated feature flag (circuit breaker).

    # If the check passes, the callback does nothing, and the agent proceeds normally.
