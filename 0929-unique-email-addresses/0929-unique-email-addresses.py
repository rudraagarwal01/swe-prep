class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            # lets you split local name before @
            # and domain name after @
            local, domain = email.split('@')
            # everything after + is ignored
            local = local.split('+')[0]
            # removes the .
            local = local.replace('.', '')
            # add al the emails to set
            unique_emails.add((local, domain))
        
        return len(unique_emails)