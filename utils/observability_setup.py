import logging
import os


def setup_observability():
    # Clean up any previous logs
    for log_file in ["logger.log", "web.log", "tunnel.log"]:
        if os.path.exists(log_file):
            os.remove(log_file)
            print(f"🧹 Cleaned up {log_file}")

    """
    Configures detailed logging for the agent framework to enable trajectory debugging.
    In production, this would integrate with Cloud Trace and Cloud Logging.
    """
    logging.basicConfig(
        filename="logger.log",
        level=logging.DEBUG,
        format="%(filename)s:%(lineno)s %(levelname)s:%(message)s",
    )

    print("Observability configured: Detailed logging is ON.")
