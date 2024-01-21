from typing import List
from collections import Counter

# Date of Last Practice: Jan 17, 2024
#
# Time Complexity: O(N), where N is the number of tasks.
#
# Space Complexity: O(1). We need space to store the count of each task.
#                   In the worst case, this can be as large as the number of distinct tasks.
#                   However, since the task identifiers are uppercase English letters,
#                   there's a fixed maximum of 26 possible tasks.
#                   Therefore, this space requirement is O(1) — constant space.
#
# Step 1 - The Most Frequent Task Sets the Minimum Timeframe:
#          The task that occurs the most frequently sets a minimum bound for the time needed.
#          This is because it will require the most cooldown periods.
#
# Step 2 - Idle Slots: After placing the most frequent task with its necessary cooldown periods,
#          we get a series of slots that can be filled with other tasks.
#
# Step 3 - Filling the Slots: If we can fill all these slots with other tasks,
#          we don't need any idle time. If there aren't enough tasks to fill the slots,
#          the remaining slots become idle time.
#
# Step 4 - After Filling All Slots: Once all slots are filled,
#          we can start another cycle of the most frequent task "without needing idle time,"
#          as the cooldown period for the most frequent task has been met.
#
# Why No More Idle After Filling Slots:
#
# 1. Cooldown Period is Respected: Once you've filled the cooldown slots for the most frequent task,
#    you've ensured that this task won't appear again until after n slots.
#    This means its cooldown is respected.
#
# 2. Other Tasks Don't Need as Much Cooldown: Other tasks are less frequent,
#    meaning they naturally fit into the gaps without needing extra idle time.
#
# 3. Efficient Use of Time Slots: By the time you need to place the most frequent task again,
#    you've used up other tasks in the cooldown slots,
#    making room for the most frequent task without additional idle time.


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_count = max(task_counts.values())
        tasks_with_max_count = sum(
            1 for count in task_counts.values() if count == max_count
        )
        part_count = max_count - 1
        part_length = max(0, n - (tasks_with_max_count - 1))
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - tasks_with_max_count * max_count
        idles = max(0, empty_slots - available_tasks)
        return len(tasks) + idles


# Test cases
sol = Solution()

# Test Case 1
assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8

# Test Case 2
assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6

# Test Case 3
assert (
    sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
    == 16
)

print("All test cases passed!")
