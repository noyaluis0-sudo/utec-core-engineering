#!/usr/bin/env python3


def uppercase(str):
    res = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            res += chr(ord(c) - 32)
        else:
            res += c
<<<<<<< HEAD
    print("{}".format(res)
=======
    print("{}".format(res))
>>>>>>> 3e026f0f8d6f656b9050e9db96737e302e616e1f
