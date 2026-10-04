function outer() {

    function inner() {
        console.log("Inner function");
    }

    inner();
}

outer();