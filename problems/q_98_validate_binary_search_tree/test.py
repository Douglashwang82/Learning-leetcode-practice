    def downheap(index):
        left_index = 2*index + 1
        right_index = 2* index + 2
        if left_index <= len(self.number_pool) - 1:
            small_index = left_index
            if right_index <= len(self.number_pool) - 1:
                if self.number_pool[left_index] > self.number_pool[right_index]:
                    small_index = right_index
            if self.number_pool[index] < self.number_pool[small_index]:
                small_index = index
                self.number_pool[small_index], self.number_pool[index] = self.number_pool[index], self.number_pool[small_index]