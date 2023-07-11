from time import strftime


class Logger:
    CLR_WARNING: str = '\u001b[93m'
    CLR_ERR: str = '\u001b[91m'
    CLR_END: str = '\u001b[0m'
    CLR_MSG: str = '\u001b[94m'
    CLR_SUCCESS: str = '\u001b[92m'

    @staticmethod
    def _format(msg: str) -> str:
        return f'[{strftime("%Y-%m-%d %H:%M:%S")}] {msg}'

    @classmethod
    def _log(cls, msg: str, color: str) -> None:
        formatted_msg = f'{color}{cls._format(msg)}{cls.CLR_END}'
        print(formatted_msg, flush=True)

    @classmethod
    def msg(cls, msg: str) -> None:
        cls._log(msg, cls.CLR_MSG)

    @classmethod
    def success(cls, msg: str) -> None:
        cls._log(msg, cls.CLR_SUCCESS)

    @classmethod
    def warn(cls, msg: str) -> None:
        cls._log(msg, cls.CLR_WARNING)

    @classmethod
    def error(cls, msg: str) -> None:
        cls._log(msg, cls.CLR_ERR)


log = Logger()
