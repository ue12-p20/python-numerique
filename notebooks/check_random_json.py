import random
import json

import logging


# one possible way
def random_json():
    """
    returns a JSON-encoded of a list 
    of 2 to 5 values between 2 and 5
    """
    plain = [ 2 + 3 * random.random() for i in range(random.randint(2, 5))]
    return json.dumps(plain)


def _check_random_json(random_json):
    try:
        for run in range(10):
            result = random_json()
            if not isinstance(result, str):
                logging.error(f"result {result} is not a str")
                break
            decoded = json.loads(result)
            if not isinstance(decoded, list):
                logging.error(f"decoded {decoded} is not a list")
                break
            if not (2 <= len(decoded) <= 5):
                logging.error(f"wrong result length {len(decoded)}")
                break
            if not all( 2 <= x <= 5 for x in decoded):
                logging.error(f"at least one item outside ouf [2..5] in {decoded}")
                break
        else:
            return True
    except Exception as exc:
        logging.exception("An exception occurred")
        return False


# ipython filters out 'info' messages 
# and it's too cumbersome to turn that on:
# get_ipython().parent.log.setLevel(logging.INFO)

# let's do just print() when it's OK
def check_random_json(random_json):
    if _check_random_json(random_json):
        print("YES !!!")
    else:
        logging.error("nope, try again")
