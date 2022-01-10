    def downheap(index):
        left_index = 2*index + 1
        right_index = 2* index + 2
        if left_index <= len(number_pool) - 1:
            small_index = left_index
            if right_index <= len(number_pool) - 1:
                if number_pool[left_index] > number_pool[right_index]:
                    small_index = right_index
            if number_pool[index] < number_pool[small_index]:
                small_index = index
                number_pool[small_index], number_pool[index] = number_pool[index], number_pool[small_index]