def string_unquote(string):
    s = string

    if s.startswith('"'):
        assert s.endswith('"')
    else:
        assert s.startswith("'")
        assert s.endswith("'")

    s = s[:-1]
    s = s[1:]

    return s