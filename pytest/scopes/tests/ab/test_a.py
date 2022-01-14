import logging


def test(fix):
    logging.debug(fix)


def test_with_closure(think):
    msg = think(" add this to _fix")
    logging.debug(msg)