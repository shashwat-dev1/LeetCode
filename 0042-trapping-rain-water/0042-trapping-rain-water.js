/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    const n = height.length;
    
    // Edge case: need at least 3 bars to trap water
    if (n <= 2) {
        return 0;
    }
    
    let maxLeft = height[0];      // Tallest bar from left
    let maxRight = height[n - 1]; // Tallest bar from right
    let trappedWater = 0;         // Total water trapped
    let left = 1;                 // Left pointer (skip first bar)
    let right = n - 2;            // Right pointer (skip last bar)
    
    while (left <= right) {
        if (maxLeft < maxRight) {
            // Left side is the limiting factor
            if (height[left] >= maxLeft) {
                maxLeft = height[left];
            } else {
                trappedWater += maxLeft - height[left];
            }
            left++;
        } else {
            // Right side is the limiting factor
            if (height[right] > maxRight) {
                maxRight = height[right];
            } else {
                trappedWater += maxRight - height[right];
            }
            right--;
        }
    }
    
    return trappedWater;
};