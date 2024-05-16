import time

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
ANSI_RED = "\u001b[31m"
ANSI_GREEN = "\u001b[32m"
ANSI_YELLOW = "\u001b[33m"
ANSI_BLUE = "\u001b[34m"
ANSI_MAGENTA = "\u001b[35m"
ANSI_CYAN = "\u001b[36m"
ANSI_RESET = "\u001b[0m"


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def dbg(*args):

    msg = f"INFO|{time.time():.4f}|"
    msg += ", ".join([str(arg) for arg in args])

    print(msg)

def info(*args):

    msg = f"INFO|{time.time():.4f}|"
    msg += ", ".join([str(arg) for arg in args])

    print(ANSI_GREEN + msg + ANSI_RESET)

def warn(*args):

    msg = f"INFO|{time.time():.4f}|"
    msg += ", ".join([str(arg) for arg in args])

    print(ANSI_YELLOW + msg + ANSI_RESET)

def error(*args):

    msg = f"INFO|{time.time():.4f}|"
    msg += ", ".join([str(arg) for arg in args])

    print(ANSI_RED + msg + ANSI_RESET)


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def main():
    dbg("dbggggg")
    info("dassa", 231, 312.21, "dssa")

    for _ in range(42999):
        13*3131

    warn("WARRRRRRRRRRRRRN----------")
    error("0==================[];;;;;;;;;;;>>>>>>")


if '__main__' == __name__:
    main()
