def group(items):
    result = []
    index = 0

    while index < len(items):
        current_group = [items[index]]

        lookup_index = index + 1

        while lookup_index < len(items) and items[index] == items[lookup_index]:
            current_group.append(items[lookup_index])
            index += 1
            lookup_index = index + 1

        result.append(current_group)
        index += 1

    return result


print(group([2, 2, 2, -1, 2]))
