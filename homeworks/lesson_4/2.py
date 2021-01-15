base_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(base_list)
result_list = [base_list[i] for i in range(1, len(base_list)) if base_list[i] > base_list[i - 1]]
print(result_list)
