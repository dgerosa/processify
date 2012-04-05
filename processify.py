import os
import sys
from multiprocessing import Process, Queue


def processify(func):
    '''Decorator to run a function as a process.

    Be sure that every argument is *pickable* and
    the function is importable (no anonymous functions
    supported).

    Some considerations:

    - The created process is joined, so the
      code does not run in parallel.

    '''
    # register original function with different name
    # in sys.modules so it is pickable
    def process_func(q, *args, **kwargs):
        ret = func(*args, **kwargs)
        q.put(ret)

    process_func.__name__ = func.__name__ + 'processify_func'
    setattr(sys.modules[__name__], process_func.__name__, process_func)

    def wrapper(*args, **kwargs):
        q = Queue()
        p = Process(target=process_func, args=[q] + list(args), kwargs=kwargs)
        p.start()
        ret = q.get()
        p.join()
        return ret
    return wrapper


@processify
def test_function():
    return os.getpid()


def test():
    print os.getpid()
    print test_function()

if __name__ == '__main__':
    test()
