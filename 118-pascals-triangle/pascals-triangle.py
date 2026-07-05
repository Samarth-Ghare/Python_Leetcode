class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[] for _ in range(numRows)]

        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    pascal[i].append(1)
                else:
                    pascal[i].append(pascal[i-1][j-1] + pascal[i-1][j])
        return pascal