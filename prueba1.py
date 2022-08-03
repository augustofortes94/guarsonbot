def find_two_sum(numbers, target_sum):
    if len(numbers) < 2 or numbers is None:
        return None

    i = 0
    for y in numbers:
        h = len(numbers)-1
        while h > i:
            print('(' + str(i) + ',' + str(h) + ')')
            if numbers[h] + numbers[i] == target_sum:
                return [i,h]
                # str(i) + ' and ' + str(h) + ' (or ' + str(h) + ' and ' + str(i) + ') as ' + str(numbers[i]) + ' + ' + str(numbers[i]) + ' = ' + str(target_sum)
            h= h -1
        i = i +1
    return None


print(find_two_sum([3, 1, 5, 7, 5, 9], 10))