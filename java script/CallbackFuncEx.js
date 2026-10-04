function greet() {
    console.log("Hello");
}

function execute(callback) {
    callback();
}

execute(greet);