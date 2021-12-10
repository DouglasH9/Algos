// ==================================================Max Sub Array================================
// Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


// Slow solution
const maxSubArray = (arr) => {
    maxSub = -Infinity;
    for (let i = 0; i < arr.length; i++){
        let currentSub = 0;
        for (let j = i; j < arr.length; j++){
            currentSub += arr[j];
            maxSub = Math.max(maxSub, currentSub)
        }
    }
    return maxSub;
}

// console.log(maxSubArray([3,2,-1,-4,5,7,-10]));

// Fast solution
const fastMaxSubArray = (arr) => {
    currentSub = 0;
    amaxSub = arr[0];
    arr.forEach(num => {
        currentSub = Math.max(num, currentSub + num);
        maxSub = Math.max(maxSub, currentSub);
    });
    return maxSub;
}

console.log(fastMaxSubArray([-2,1,-3,4,-1,2,1,-5,4]));