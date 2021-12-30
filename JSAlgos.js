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

// ===========================================Stair Climber===========================================
// You are climbing a staircase. It takes n steps to reach the top.

// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

// Fibonacci solution...

var climbStairs = function(n) {
    if (n===1){
        return n;
    }
    let first = 1;
    let second = 2; 
    for (let i = 3; i <= n; i++){
        let third = first + second;
        first = second;
        second = third;
    }
    return second;
    
};

// ===============================================Reverse Words in a String================================================
// Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

const splitStr = (s) => {
    let result = [];
    temp = "";
    for (let i = 0; i < s.length; i++){
        if (s[i] == " "){
            result.push(temp)
            temp=""
        } else {
            temp += s[i]
        }
    }
    if (temp !== ""){
        result.push(temp)
    }
    return result
}
// console.log(splitStr("hello, how are you?"))




