class NetworkError(Exception):
    pass
class HttpError(NetworkError):
    pass

def get_network_error_classes(classes_list):
    new_list = []
    for cl in classes_list:
        if issubclass(cl, NetworkError):
            new_list.append(cl)
    return new_list