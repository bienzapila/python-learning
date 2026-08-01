def is_subfolder(folder_dict, subfolder, folder):
    for key in folder_dict.keys():
        if subfolder in folder_dict[key]:
            if key == folder:
                return True
            else:
                subfolder = key
                for key in folder_dict.keys():
                    if subfolder in folder_dict[key]:
                        if key == folder:
                            return True
                        else:
                            subfolder = key
                            for key in folder_dict.keys():
                                if subfolder in folder_dict[key]:
                                    if key == folder:
                                        return True
    else:
        return False
