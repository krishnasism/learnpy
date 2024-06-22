import re


def is_alphanumeric(string: str):
    return re.match(r"^[a-zA-Z0-9]*$", string) is not None


to_test = "abc##!@!^!!"

assert not is_alphanumeric, "String must not alphanumeric since it contains special characters"

# When you are done with an exercise, remove the following line!
# I'M NOT DONE
