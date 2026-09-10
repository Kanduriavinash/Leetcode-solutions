class Solution(object):
    def averageOfSubtree(self, root):
        
        def dfs(node):
            if not node:
                return 0, 0, 0

            left_sum, left_count, left_ans = dfs(node.left)
            right_sum, right_count, right_ans = dfs(node.right)

            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            average = total_sum // total_count

            ans = left_ans + right_ans

            if node.val == average:
                ans += 1

            return total_sum, total_count, ans

        return dfs(root)[2]