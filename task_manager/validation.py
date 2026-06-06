from datetime import datetime

def validate_task_title(title):
    if len(title) == 0:
        raise ValueError("Title cannot be empty")
    return True


def validate_task_description(description):

    if len(description) == 0:
        raise ValueError("Description cannot be empty")
    return True


def validate_due_date(due_date):
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty")
    return True