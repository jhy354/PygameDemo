class Debug:
    """
    Debug log print
    """

    def __init__(self, debug_mode=False):
        self.debug_mode = debug_mode

    def __lshift__(self, other):
        if self.debug_mode:
            print(other, end="")

        return self

    def div(self):
        if self.debug_mode:
            print("-" * 30)
