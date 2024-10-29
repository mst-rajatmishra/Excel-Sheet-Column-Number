class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        length = len(columnTitle)
        
        for i, char in enumerate(columnTitle):
            # Calculate the position of the current character
            value = ord(char) - ord('A') + 1
            # Update total based on its position in the string
            total = total * 26 + value
        
        return total
