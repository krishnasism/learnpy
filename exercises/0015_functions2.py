import re


def is_alphanumeric(string: str):
    return re.match(r"^[a-zA-Z0-9]*$", string) is not None


to_test = "abc##!@!^!!"


# When you are done with an exercise, remove the following line!
# I'M NOT DONE

assert not is_alphanumeric, "String must not alphanumeric since it contains special characters"
print("ok")

# To get a hint, change the following no to a yes
# hint: no
