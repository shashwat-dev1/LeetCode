class Solution {
    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int maxH = findMaxConsecutive(hBars);
        int maxV = findMaxConsecutive(vBars);
        int side = Math.min(maxH, maxV) + 1;
        return side * side;
    }
    private int findMaxConsecutive(int[] bars) {
        if (bars.length == 0) return 0;
        Arrays.sort(bars);
        int maxConsecutive = 1;
        int currentConsecutive = 1;
        for (int i = 1; i < bars.length; i++) {
            if (bars[i] == bars[i - 1] + 1) {
                currentConsecutive++;
                maxConsecutive = Math.max(maxConsecutive, currentConsecutive);
            } else {
                currentConsecutive = 1;
            }
        }
        return maxConsecutive;
    }
}