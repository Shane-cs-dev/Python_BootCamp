from pandas import BooleanDtype


def age_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(age_check(18))