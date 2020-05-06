import sys
import select

from typing import Iterable


def read_stdin_lines(read_timeout: int = 0) -> Iterable[str]:
    """
    Read stdin line by line and return the tuple:

    (IS_STDIN_PIPE, IS_STDOUT_PIPE, LINE)

    :param read_timeout: read timeout of stdin. 0 = infinite
    :type read_timeout: int
    """

    is_stdout_pipe = not sys.stdout.isatty()

    # -------------------------------------------------------------------------
    # Read info by stdin or parameter
    # -------------------------------------------------------------------------
    if sys.stdin in select.select([sys.stdin], [], [], read_timeout)[0]:

        for line in sys.stdin.readlines():
            yield True, is_stdout_pipe, line

    else:
        yield False, is_stdout_pipe, None


__all__ = ("read_stdin_lines",)
