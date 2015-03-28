from __future__ import print_function


def safe_input(prompt):
    """Return 'None' rather than EOF or KeyboardInterrupt exceptions"""
    try:
        raw_input(prompt)
    except (EOFError, KeyboardInterrupt):
        return 'None'

