def find_common_participants(participants1, participants2, separator=','):

    # Разделяем строки на списки участников
    list1 = participants1.split(separator)
    list2 = participants2.split(separator)
    
    # Находим общих участников
    common = set(list1) & set(list2)
    
    # Возвращаем отсортированный список
    return sorted(list(common))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

result = find_common_participants(participants_first_group, participants_second_group, '|')
print(result)
