function recursiveCountDown(num, count=1)

    //base case
    if (num < 1) return 0
    console.log(num)
    return recursiveCountDown(num - count)