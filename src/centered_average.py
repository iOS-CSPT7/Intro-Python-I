

def centered_average(a_list): 
    #make a copy
    copy_list = list(a_list)   #a_list.copy()  #a_list[:]
    #sort the list
    copy_list.sort()
    #slice the list to exclude the first and last elements
    list_to_sum = copy_list[1:-1]
    #sum the list
    return sum(list_to_sum)/ len(list_to_sum)

    
print(centered_average([1, 2, 3, 4, 100]))

print(centered_average([1, 2, 3]))