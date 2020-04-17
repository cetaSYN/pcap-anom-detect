# from scipy.stats import entropy
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html


def is_english_text(e_val):
    """Returns True if the given value is potentially English text based upon entropy"""
    return 0.5 > e_val > 0.35
