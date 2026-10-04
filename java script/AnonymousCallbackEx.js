function calculate(callback) {
    console.log(callback(10, 20));
}

calculate(function(a, b) {
    return a + b;
});