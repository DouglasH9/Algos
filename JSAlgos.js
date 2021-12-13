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

// console.log(fastMaxSubArray([-2,1,-3,4,-1,2,1,-5,4]));

// ==================================Plus one array=========================================
// given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

// Increment the large integer by one and return the resulting array of digits.

const plusOne = (digits) => {
    if (digits.length === 1 && digits[0] === 9){
        digits[0] = 1;
        digits.push(0);
        return digits;
    }
    for (let i = digits.length - 1; i > - 1; i--){
        if(digits[i] === 9){
            digits[i] = 0;
        }
        else {
            digits[i] += 1
            return digits;
        }
    }
    digits[0] = 1;
    digits.push(0);
    return digits;
    
};