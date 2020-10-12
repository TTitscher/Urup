
def task_readme():
    return {
        "file_dep": ["urup/to_md.py"],
        "actions": ["urup urup/to_md.py -o README.md"]
    }
    
