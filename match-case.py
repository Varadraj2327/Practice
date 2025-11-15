# Match-Case statement (switch): An alternative to using many "elif" statements
#                              Excute some cpde if a value matches a "case"
#                               Benefits: cleaner and syntax is more readeble

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
print(is_weekend("Sunday"))