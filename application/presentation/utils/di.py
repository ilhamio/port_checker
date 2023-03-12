import asyncio
import inspect

from application.pkg.handlers.event import EVENT_HANDLERS


def inject(function):
    """
    Self-written dependency injector which provide "cmd" and "usecase" args to CLI command
    :param function:
    :return:
    """
    def wrapper(*args, **kwargs):
        try:
            model_type = function.__annotations__['cmd']
            model = model_type(**kwargs)
        except KeyError:
            print('Error: Presentation function must have "cmd" and "usecase" arguments with annotation')
            return
        except TypeError as e:
            print(e)
            print('Error: Wrong arguments!!!')
            return

        try:
            usecase = EVENT_HANDLERS[model_type]()
        except KeyError:
            print('Error: No usecase associated with the command')
            return
        if inspect.iscoroutinefunction(function):
            result = asyncio.get_event_loop().run_until_complete(function(cmd=model, usecase=usecase))
        else:
            result = function(cmd=model, usecase=usecase)
        return result

    return wrapper
