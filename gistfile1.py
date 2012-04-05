import os
import sys
from multiprocessing import Process


def processify(func):
    '''Decorator to run a function as a process.

    Be sure that every argument is *pickable* and
    the function is importable (no anonymous functions
    supported).

    Some considerations:

    - It doesn't support return values.
    - The created process is joined, so the
      code does not run in parallel.

    '''
    # register original function with different name 
    # in sys.modules so it is pickable
    func.__name__ = func.__name__ + 'processify_func'
    setattr(sys.modules[__name__], func.__name__, func)

    def wrapper(*args, **kwargs):
        p = Process(target=func, args=args, kwargs=kwargs)
        p.start()
        p.join()
    return wrapper


@processify
def test_function():
    print os.getpid()


def test():
    print os.getpid()
    test_function()

if __name__ == '__main__':
    test()
