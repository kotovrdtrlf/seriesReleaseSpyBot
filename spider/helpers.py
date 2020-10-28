# helpers.py

def is_informational_tr(tr):
    # Returns true if a table row contains all 5 information sections
    return len(tr.findAll('td')) == 5