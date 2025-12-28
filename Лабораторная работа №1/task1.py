numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


sum_of_numbers = sum(numbers[:4] + numbers[5:])
count_of_numbers = len(numbers)
average_of_numbers = round(sum_of_numbers / count_of_numbers, 2)
edited_numbers = (numbers[:4] + [average_of_numbers] + numbers[5:])









# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", edited_numbers)
