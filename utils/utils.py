LAST_LINE = ""


class Debug:
    """
    Debug log print
    """

    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode

    def __lshift__(self, other):
        global LAST_LINE
        if self.debug_mode and str(other) != LAST_LINE:
            print(other, end="")
            LAST_LINE = str(other)

        return self
