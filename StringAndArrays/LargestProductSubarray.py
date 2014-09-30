__author__ = 'pratik'

class Solution:
    # @param A, a list of integers
    # @return an integer

    def maxProduct(self, A):
        current_negative_product = 1
        current_positive_product = 1

        max_positive_product = 0
        max_product = float("-inf")
        for index in range(0, len(A)):
            if A[index] > 0:
                current_positive_product = current_positive_product*A[index]
                current_negative_product = min(current_negative_product*A[index], 1)


            if A[index] < 0:
                prev_current_positive = current_positive_product
                current_positive_product = max(current_positive_product, current_negative_product*A[index])
                current_negative_product = min(A[index],  1)


            if max_product <= current_positive_product:
                max_index = index
                max_product = current_positive_product

            if A[index] == 0:
                current_negative_product = 1
                current_positive_product = 1

        return max_product

def main():
    obj_solution = Solution()
    print obj_solution.maxProduct([-4, -3])

main()
