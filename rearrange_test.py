#!/usr/bin/env python3

import re

def rearrange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$",name)
    if result is None:
        return result
    return "{} {}".format(result[2], result[1])
    #fname= "{} {}".format(result[2], result[1])
    #print(fname)

rearrange_name("Lovelace, Ada") # Ada Lovelace
rearrange_name("Ritchie, Dennis") # Dennis Ritchie
rearrange_name("Hopper, Grace M.") # Grace M. Hopper
name = rearrange_name("Kennedy, John F.") # John F. Kennedy
