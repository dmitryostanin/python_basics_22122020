start_result = float(input('Enter start result (km): '))
goal_result = float(input('Enter goal result (km): '))
goal_day = 1
result = start_result
while result < goal_result:
    print(f'Day: {goal_day} Result: {result:.3f} km')
    result *= 1.1
    goal_day += 1
else:
    print(f'At day {goal_day} sportsman reached the goal - not less than {goal_result:.3f} km')
