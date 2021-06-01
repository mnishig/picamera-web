import time

def gen_tempname():
    """
    return YYYYMMDD-HHmmss (HH:0-23)
    """
    t = time.time()
    lt = time.localtime(t)
    st = time.strftime('%Y%m%d-%H%M%S',lt)
    return st

# end of file
