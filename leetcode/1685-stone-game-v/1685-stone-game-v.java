class Solution {
    int[][] dp = new int[502][502];

    int f(int left, int right, int total_sum, int[] stoneValue) {

        // Only one stone is left.
        // We cannot split it anymore.
        if (left == right) {
            return 0;
        }

        // Already calculated this interval.
        if (dp[left][right] != -1) {
            return dp[left][right];
        }

        int cur_sum = 0;
        int ans = 0;

        // Try every possible split:
        //
        // [left ... i] | [i+1 ... right]
        //
        for (int i = left; i < right; i++) {

            // Sum of the left part.
            cur_sum += stoneValue[i];

            // Sum of the right part.
            int rem_sum = total_sum - cur_sum;

            // Left side is smaller.
            // Bob throws away the right side.
            // Alice keeps the left side.
            if (cur_sum > rem_sum) {

                ans = Math.max(
                    ans,
                    rem_sum + f(i + 1, right, rem_sum, stoneValue)
                );

            }
            // Right side is smaller.
            // Bob throws away the left side.
            // Alice keeps the right side.
            else if (cur_sum < rem_sum) {

                ans = Math.max(
                    ans,
                    cur_sum + f(left, i, cur_sum, stoneValue)
                );

            }
            // Both sides have equal sums.
            // Alice can choose either side.
            else {

                // Keep the right side.
                ans = Math.max(
                    ans,
                    rem_sum + f(i + 1, right, rem_sum, stoneValue)
                );

                // Keep the left side.
                ans = Math.max(
                    ans,
                    cur_sum + f(left, i, cur_sum, stoneValue)
                );
            }
        }

        return dp[left][right] = ans;
    }

    public int stoneGameV(int[] stoneValue) {

        int total_sum = 0;

        for (int value : stoneValue) {
            total_sum += value;
        }

        int left = 0;
        int right = stoneValue.length - 1;

        // Initialize every DP state to -1.
        for (int i = 0; i < 502; i++) {
            java.util.Arrays.fill(dp[i], -1);
        }

        return f(left, right, total_sum, stoneValue);
    }
}