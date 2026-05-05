def add_query_string(url, query):
    ans = url
    if len(query):
        ans += "?"
        for key in query.keys():
            ans += f"{key}={query[key]}&"
        ans = ans[:-1]
    return ans
