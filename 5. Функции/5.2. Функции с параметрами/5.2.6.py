def print_perm_time_call(msc_time):
    if "08" <= msc_time[:2] < "10":
        print(f"Созвон будет в {int(msc_time[1])+2}{msc_time[2:]}.")
    elif "18" <= msc_time[:2] < "20":
        print(f"Созвон будет в {int(msc_time[:2])+2}{msc_time[2:]}.")
    else:
        print(f"Созвон будет в {msc_time[0]}{int(msc_time[1])+2}{msc_time[2:]}.")
