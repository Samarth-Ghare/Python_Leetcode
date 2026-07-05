class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for  i in range(rowIndex):
            newRow = [0] * (len(row)+1)
            for j in range(len(row)):
                newRow[j] += row[j]
                newRow[j+1]+= row[j]

            row = newRow
        return row