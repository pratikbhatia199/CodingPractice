class Solution:
    # @param A, a list of integers
    # @return an integer

    def maxProduct(self, A):
        current_negative_product = 1
        current_positive_product = 1
        max_val = float("-inf")
        max_positive_product = 0
        max_product = float("-inf")
        count = 0
        for index in range(0, len(A)):
            if A[index] == 0:
                count = 0
                if A[index] > max_val:
                    max_val = A[index]
            if A[index]!=0:
                count = count + 1
                if A[index] > max_val:
                   max_val = A[index]
                if count > 1:
                    break
        if count == 1:
            return max_val
        if count == 0:
            return max_val

        for index in range(0, len(A)):

            if A[index] > 0:
                current_positive_product = current_positive_product*A[index]
                current_negative_product = min(current_negative_product*A[index], 1)


            if A[index] < 0:
                prev_current_positive = current_positive_product
                current_positive_product = max(1, current_negative_product*A[index])
                current_negative_product = min(A[index],  prev_current_positive*A[index])


            if max_product <= current_positive_product:
                max_index = index
                max_product = current_positive_product

            if A[index] == 0:
                current_negative_product = 1
                current_positive_product = 1

        return max_product