from config.app import ConnectionFromPool


def transactional():
    def wrapper(func):
        def wrapper_func(*args, **kwargs):
            with ConnectionFromPool() as cursor:
                return func(*args, **kwargs, db_cursor=cursor)

        return wrapper_func

    return wrapper
