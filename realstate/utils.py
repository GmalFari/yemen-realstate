
def path_file_name(instance, filename):
    return '/'.join(filter(None, (str(instance.company.id), filename)))
def img_file_name(instance, filename):
    return '/'.join(filter(None,(str(instance.realstate.company.id), str(instance.realstate.id), filename)))
