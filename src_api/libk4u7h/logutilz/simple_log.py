import time

from libk4u7h.logutilz import ANSI_COLORS


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def dbg(*args):

    msg = f"INFO|{time.time():.4f}|"
    msg += ", ".join([str(arg) for arg in args])

    print(msg)


def info(*args):

    msg = f"INFO|{time.time():.4f}|"
    msg += ", ".join([str(arg) for arg in args])

    print(ANSI_COLORS.GREEN + msg + ANSI_COLORS.RESET)


def warn(*args):

    msg = f"INFO|{time.time():.4f}|"
    msg += ", ".join([str(arg) for arg in args])

    print(ANSI_COLORS.YELLOW + msg + ANSI_COLORS.RESET)


def error(*args):

    msg = f"INFO|{time.time():.4f}|"
    msg += ", ".join([str(arg) for arg in args])

    print(ANSI_COLORS.RED + msg + ANSI_COLORS.RESET)


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def main():
    dbg("dbggggg")
    info("dassa", 231, 312.21, "dssa")

    for _ in range(42999):
        13 * 3131

    warn("WARRRRRRRRRRRRRN----------")
    error("0==================[];;;;;;;;;;;>>>>>>")


if '__main__' == __name__:
    main()
