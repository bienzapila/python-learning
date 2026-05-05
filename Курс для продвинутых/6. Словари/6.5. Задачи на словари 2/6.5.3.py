def is_access_allowed(ip_adress, mode, ip_access_lists):
    if mode == 1:
        if ip_adress not in ip_access_lists["black list"]:
            return "ДА"
        else:
            return "НЕТ"
    elif mode == 2:
        if ip_adress in ip_access_lists["white list"]:
            return "ДА"
        else:
            return "НЕТ"
