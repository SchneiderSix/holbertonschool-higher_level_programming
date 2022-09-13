#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    dn = 0
    nl = []
    for i in range(0, list_length):
        try:
            dn = my_list_1 / my_list_2
        except (TypeError):
            dn = 0
            print("wrong type")
        except (ZeroDivisionError):
            dn = 0
            print("division by 0"):
        except (IndexError)
            dn = 0
            print("out of range"):
        finally:
            nl.append(dn)
    return nl
