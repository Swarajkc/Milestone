from datetime import datetime


def log_message(content, is_error) -> str:
        log_status = f"{datetime.now()}Success: {'Error' if is_error else 'Success'}"
        return log_status + '\n' + content
        