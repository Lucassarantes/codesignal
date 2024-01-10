from collections import OrderedDict

def solution(names):
    print(names)
    name_count = OrderedDict()

    for i in range(len(names)):
        original_name = names[i]
        if original_name in name_count:
            suffix = 1
            while f"{original_name}({suffix})" in name_count:
                suffix += 1
            names[i] = f"{original_name}({suffix})"
            name_count[f"{original_name}({suffix})"] = 1
        else:
            name_count[original_name] = 1
            
    return names