import time

from libk4u7.logutilz import ANSI_COLORS

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
_ALWAYS_FLUSH = True
_TS_FLOAT_DIGITS = 0


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def dbg(*args):

    curr_ts = int(time.time() * (10**_TS_FLOAT_DIGITS)) / float(10**_TS_FLOAT_DIGITS)
    if 0 == _TS_FLOAT_DIGITS:
        curr_ts = int(curr_ts)
    curr_ts_str = f"{curr_ts}"

    msg = f"DBG|{curr_ts_str}|"
    msg += ", ".join([str(arg) for arg in args])
    print(msg, flush=_ALWAYS_FLUSH)


def info(*args):

    curr_ts = int(time.time() * (10**_TS_FLOAT_DIGITS)) / float(10**_TS_FLOAT_DIGITS)
    if 0 == _TS_FLOAT_DIGITS:
        curr_ts = int(curr_ts)
    curr_ts_str = f"{curr_ts}"

    msg = f"INFO|{curr_ts_str}|"
    msg += ", ".join([str(arg) for arg in args])
    print(ANSI_COLORS.GREEN + msg + ANSI_COLORS.RESET, flush=_ALWAYS_FLUSH)


def warn(*args):

    curr_ts = int(time.time() * (10**_TS_FLOAT_DIGITS)) / float(10**_TS_FLOAT_DIGITS)
    if 0 == _TS_FLOAT_DIGITS:
        curr_ts = int(curr_ts)
    curr_ts_str = f"{curr_ts}"

    msg = f"WARN|{curr_ts_str}|"
    msg += ", ".join([str(arg) for arg in args])
    print(ANSI_COLORS.YELLOW + msg + ANSI_COLORS.RESET, flush=_ALWAYS_FLUSH)


def error(*args):

    curr_ts = int(time.time() * (10**_TS_FLOAT_DIGITS)) / float(10**_TS_FLOAT_DIGITS)
    if 0 == _TS_FLOAT_DIGITS:
        curr_ts = int(curr_ts)
    curr_ts_str = f"{curr_ts}"

    msg = f"ERROR|{curr_ts_str}|"
    msg += ", ".join([str(arg) for arg in args])
    print(ANSI_COLORS.RED + msg + ANSI_COLORS.RESET, flush=_ALWAYS_FLUSH)


# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
def main():
    dbg("dbggggg")
    info("dassa", 231, 312.21, "dssa")


if '__main__' == __name__:
    main()
