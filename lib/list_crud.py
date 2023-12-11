def create_an_empty_list():
    return []


def create_a_list():
    return [1, 2, 3, 4]


def add_element_to_end_of_list(list, element):
    list.append(element)
    return list


def add_element_to_start_of_list(list, element):
    list.insert(0, element)
    return list


def remove_element_from_end_of_list(list):
    last = len(list) - 1
    list.pop(last)
    return list


def remove_element_from_start_of_list(list):
    del list[0]
    return list


def retrieve_first_element_from_list(list):
    first_item = list[0]
    return first_item


def retrieve_element_from_index(list, index):
    item = list[index]
    return item


def retrieve_last_element_from_list(list):
    item = len(list) - 1
    return list[item]
