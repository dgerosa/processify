# processify

Python decorator to spawn a new process every time a function is called.

This is a for fork from [gist.github.com/schlamar/2311116](https://gist.github.com/schlamar/2311116), where I just added files  `__init__.py` and `setup.py` to make it a module.

### Usage

    def test_processify():

        @processify
        def tricky():
            return os.getpid()

        print(os.getpid(), tricky(), tricky())
    
    
