from functools import wraps


def log(filename=None):
    """
    Декоратор для логирования вызова функции."""

    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as error_info:
                if filename is None:
                    print(
                        f"Function {func.__name__} started\n"
                        f"Function {func.__name__} finished by error:\n{type(error_info)}: {error_info}\n"
                        f"Parameters - args: {args}, kwargs: {kwargs}\n"
                    )
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"Function {func.__name__} started\n"
                            f"Function {func.__name__} finished by error:\n{type(error_info)}: {error_info}\n"
                            f"Parameters - args: {args}, kwargs: {kwargs}\n\n"
                        )
            else:
                if filename is None:
                    print(
                        f"Function {func.__name__} started\n"
                        f"Function {func.__name__} finished\n"
                        f"Result: {result}\n"
                    )
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"Function {func.__name__} started\n"
                            f"Function {func.__name__} finished\n"
                            f"Result: {result}\n\n"
                        )
                return result

        return inner

    return wrapper
