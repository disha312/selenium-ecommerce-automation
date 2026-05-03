import logging
import os

def get_logger():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    reports_path = os.path.join(project_root, "reports")

    if not os.path.exists(reports_path):
        os.makedirs(reports_path)

    log_file = os.path.join(reports_path, "logs.log")

    logger = logging.getLogger("automation")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger