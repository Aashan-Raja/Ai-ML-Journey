def pld_checkr(str):
    rev_str = str[::-1]
    if str == rev_str:
        print("The string is Plandrome!")
    else:
        print("Not a plandrome!")
pld_checkr("bob")
pld_checkr("car")