class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if (numRows == 1 or numRows >= len(s)): 
            return s

        # create empty strings
        # so if numRows is 3 then it will create ["",  "", ""]
        # it iterates through loop and adds each letter
        # For instance if s = "ABCDE"
        # Itll add ["A", "B", "C"]
        # Then when it reaches numRows - 1 it goes back up
        # So then itll be ["AE", "BD", "C"]
        rows = numRows * [""]
        curr_row = 0
       

        for ch in s:
            # appends the current char to the string
            rows[curr_row] += ch

            # directions 
            if curr_row == 0:
                # go down
                direction = 1
            elif curr_row == numRows -1:
                direction = -1
                
            #moves to the correct row
            curr_row += direction 

        return "".join(rows)

    
        
