from time import strftime

UNI_ESC: str = '\u001b'
CLR_ERR: str = '%s[91m' % UNI_ESC
CLR_SUCCESS: str = '%s[92m' % UNI_ESC
CLR_WARNING: str = '%s[93m' % UNI_ESC
CLR_MSG: str = '%s[94m' % UNI_ESC
CLR_END: str = '%s[0m' % UNI_ESC


class Logger:
    @staticmethod
    def _format(msg: str) -> str:
        return f'[{strftime("%Y-%m-%d %H:%M:%S")}] {msg}'

    @classmethod
    def _log(cls, msg: str, color: str = '') -> None:
        formatted_msg = f'{color}{cls._format(msg)}{CLR_END}'
        print(formatted_msg, flush=True)

    @classmethod
    def debug(cls, msg: str) -> None:
        cls._log(msg)

    @classmethod
    def msg(cls, msg: str) -> None:
        cls._log(msg, CLR_MSG)

    @classmethod
    def success(cls, msg: str) -> None:
        cls._log(msg, CLR_SUCCESS)

    @classmethod
    def warn(cls, msg: str) -> None:
        cls._log(msg, CLR_WARNING)

    @classmethod
    def error(cls, msg: str) -> None:
        cls._log(msg, CLR_ERR)
