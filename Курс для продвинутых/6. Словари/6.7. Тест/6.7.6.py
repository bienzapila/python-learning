def build_query_string(params):
    ans = ""
    for key in sorted(list(params.keys())):
        ans += f"{key}={params[key]}&"
    ans = ans[:-1]
    return ans


print(build_query_string({"name": "timur", "age": 28}))
