def singleton(the_class):
    instances = {}
    def get_class(*arg, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*arg, **kwargs)
        return instances[the_class]
    
    return get_class

@singleton
class AppSettings:
    def __init__(self):
        print("OI")
    


if __name__ == '__main__':
    as1 = AppSettings()
    as2 = AppSettings()

    print(as1)
    print(as2)