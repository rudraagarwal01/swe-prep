class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        seen = set()

        for email in emails:
            curr_email = []
            symbol = None
            for char in email:
                if symbol != '@' and char == '.':
                    continue
                elif char == '@':
                    symbol = '@'
                elif symbol != '@' and char == '+':
                    symbol = '+'
                
                if symbol != '+':
                    curr_email.append(char)
            
            seen.add("".join(curr_email))
        
        return len(seen)


