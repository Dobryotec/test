

with open("10m.txt", "r") as file:
     new_list = []
     for number in file.readlines():
          new_list.append(int(number.replace("\n","")))

max_number = max(new_list)
min_number = min(new_list)

length_new_list = len(new_list)

average = sum(new_list) / length_new_list

copy_new_list = [*new_list]

copy_new_list.sort()


def get_median(copy_new_list, length_new_list):
     if length_new_list == 0:
          return None
     if length_new_list % 2 != 0:
          return copy_new_list[length_new_list // 2]
     else:
          right_number = length_new_list // 2
          left_number = right_number - 1
          return (copy_new_list[left_number] + copy_new_list[right_number]) / 2

median = get_median(copy_new_list, length_new_list)

def find_longest_increasing_sequence(new_list, length_new_list):
    count = 1
    max_count = 1
    for i in range(1, length_new_list):
        if new_list[i] > new_list[i -1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
    return max_count

longest_increasing_sequence = find_longest_increasing_sequence(new_list, length_new_list)

def find_longest_decreasing_sequence(new_list, length_new_list):
    count = 1
    max_count = 1
    for i in range(1, length_new_list):
        if new_list[i] < new_list[i -1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
    return max_count

longest_decreasing_sequence = find_longest_decreasing_sequence(new_list, length_new_list)
          
print(f"Max number => {max_number}")
print(f"Min number => {min_number}")               
print(f"Median => {median}")
print(f"Average => {average}")
print(f"Longest increasing sequence => {longest_increasing_sequence}") 
print(f"Longest decreasing sequence => {longest_decreasing_sequence}")

