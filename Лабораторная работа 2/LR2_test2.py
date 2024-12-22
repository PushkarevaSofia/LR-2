# TODO Напишите функцию find_common_participants

def find_common_participants(participants_first_group, participants_second_group, razdel = ','):

    participants_first_group = set(participants_first_group.split(razdel))
    participants_second_group = set(participants_second_group.split(razdel))
    # разделили зяпятыми, переход в множества

    common_participants = participants_first_group.intersection(participants_second_group)
    # пересечение

    common_participants = sorted(list(common_participants)) # список по алфавиту
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, razdel = '|')
print("Общие участники:", participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
