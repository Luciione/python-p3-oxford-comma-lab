def oxford_comma(array):
    if len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return f"{array[0]} and {array[1]}"
    else:
        last_element = array[-1]
        other_elements = ", ".join(array[:-1])
        return f"{other_elements}, and {last_element}"
