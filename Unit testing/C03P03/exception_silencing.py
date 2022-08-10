class ExceptionSilencer:
    def __init__(self, exception_cls):
        self.exception_cls = exception_cls

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.exception_cls is exc_type
