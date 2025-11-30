import shlex

from src.exceptions import FlagNotFound


class Command:
    def __init__(self, command: str):
        self.input_str: str = command

        self.tokens: list[str] = []
        self._get_tokens()

        self.command: str = ''
        self.params: list[str] = []
        self.flags: list[str] = []

        self._get_command()
        self._get_params()
        self._get_flags()


    def _get_tokens(self) -> None:
        self.tokens = shlex.split(self.input_str)


    def _check_flag(self, flag: str) -> bool:
        if flag not in ['-b']:
            raise FlagNotFound(flag)

        return True


    def _get_flags(self) -> None:
        self.flags = [token for token in self.tokens if token.startswith('-') and not token.lstrip('-').isdigit() and self._check_flag(token)]


    def _get_params(self) -> None:
        tokens = self.tokens[1:]

        self.params = [token for token in tokens if not (token.startswith('-') and not token.lstrip('-').isdigit())]


    def _get_command(self) -> None:
        self.command = self.tokens[0]