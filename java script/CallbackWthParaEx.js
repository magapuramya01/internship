function add(a, b) {
    return a + b;
}

function calculate(callback) {
    console.log(callback(10, 20));
}

calculate(add);