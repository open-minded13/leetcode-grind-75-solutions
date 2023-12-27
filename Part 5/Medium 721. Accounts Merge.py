from typing import List


class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x != self.parent.setdefault(x, x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py


class Solution:
    def accountsMerge(self, accounts):
        dsu = DSU()
        email_to_name = {}
        email_to_id = {}
        id = 0

        # Step 1: Map each email to its owner and give each email a unique ID
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = id
                    id += 1
                dsu.union(email_to_id[account[1]], email_to_id[email])

        # Step 2: Use Union-Find to group emails
        result = {}
        for email in email_to_name:
            parent_id = dsu.find(email_to_id[email])
            result.setdefault(parent_id, []).append(email)

        # Step 3: Collect and sort emails for each account
        return [
            [email_to_name[emails[0]]] + sorted(emails) for emails in result.values()
        ]


class First_Inefficient_Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        i = 0
        while i < len(accounts):
            j = 0
            is_merged = False
            while j < len(accounts):
                if j == i:
                    j += 1
                    continue
                name = accounts[i][0]
                account_set = set(accounts[i][1:])
                if accounts[j][0] == name:
                    check_set = set(accounts[j][1:])
                    if account_set.intersection(check_set):
                        accounts[i] = [name] + list(account_set.union(check_set))
                        del accounts[j]
                        j -= 1
                        is_merged = True
                j += 1

            accounts[i][1:] = list(set(accounts[i][1:]))

            # accounts[i][1:].sort()
            accounts[i][1:] = sorted(accounts[i][1:])
            if not is_merged:
                i += 1

        return accounts


# Test cases
def main():
    solution = Solution()

    # Test Case 1: Basic Case
    accounts1 = [["Alice", "alice@mail.com"], ["Bob", "bob@mail.com"]]
    print("Test Case 1:", solution.accountsMerge(accounts1))

    # Test Case 2: Single User Multiple Accounts
    accounts2 = [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ]
    print("Test Case 2:", solution.accountsMerge(accounts2))

    # Test Case 3: Multiple Users with Same Name
    accounts3 = [["John", "johnsmith@mail.com"], ["John", "johnnybravo@mail.com"]]
    print("Test Case 3:", solution.accountsMerge(accounts3))

    # Test Case 4: Complex Case with Multiple Merges
    accounts4 = [
        ["John", "john00@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["Mary", "marynewyork@mail.com", "mary@mail.com"],
    ]
    print("Test Case 4:", solution.accountsMerge(accounts4))

    # Test Case 5: No Accounts
    accounts5 = []
    print("Test Case 5:", solution.accountsMerge(accounts5))

    # Test Case 6: Single Account with Multiple Emails
    accounts6 = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com", "john00@mail.com"]
    ]
    print("Test Case 6:", solution.accountsMerge(accounts6))


if __name__ == "__main__":
    main()
