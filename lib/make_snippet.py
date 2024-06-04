def make_snippet(str):
    if len(str) <= 5 or str == '':
        return str
    elif len(str) > 5:
        return str[:5]+ "..."
