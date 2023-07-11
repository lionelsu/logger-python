from time import strftime


class Log:
    CLR_WARNING: str = '\033[93m'
    CLR_ERR: str = '\033[92m'
    CLR_END: str = '\033[0m'
    CLR_MSG: str = '\033[94m'
    CLR_SUCCESS: str = '\033[92m'

    @staticmethod
    def _format(msg: str) -> str:
        return f'[{strftime("%Y-%m-%d %H:%M:%S")}] {msg}'

    @classmethod
    def msg(cls, msg: str) -> None:
        print(f'{cls.CLR_MSG}{cls._format(msg)}{cls.CLR_END}', flush=True)

    @classmethod
    def warning(cls, msg: str) -> None:
        print(f'{cls.CLR_WARNING}{cls._format(msg)}{cls.CLR_END}', flush=True)

    @classmethod
    def err(cls, msg: str) -> None:
        print(f'{cls.CLR_ERR}{cls._format(msg)}{cls.CLR_END}', flush=True)

    @classmethod
    def success(cls, msg: str) -> None:
        print(f'{cls.CLR_SUCCESS}{cls._format(msg)}{cls.CLR_END}', flush=True)

    @classmethod
    def debug(cls, msg: str) -> None:
        print(cls._format(msg), flush=True)
