def is_sub_folder(folder_dict, subfolder, folder):
    ans = []
    for key in folder_dict.keys():
        for s in folder[key]:
            
