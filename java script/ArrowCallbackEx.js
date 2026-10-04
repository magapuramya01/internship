function calculate(callback) {
    console.log(callback(10, 20));
}

calculate((a, b) => a + b);