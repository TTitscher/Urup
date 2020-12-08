def task_readme():
    return {
        "file_dep": ["urup/to_md.py"],
        "actions": ["urup urup/to_md.py -o README.md"],
    }


def task_modifiers():
    return {
        "file_dep": ["urup/to_md.py", "urup/modifiers.py"],
        "actions": ["urup urup/modifiers.py -o urup/modifiers.md"],
    }
