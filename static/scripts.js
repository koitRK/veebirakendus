function myFunction() {
    console.log("clicked");
    alert("hello");
    console.log("xdxd");
}


window.onload = function() {
    var reloading = sessionStorage.getItem("reloading");
    if (reloading) {
        sessionStorage.removeItem("reloading");
        myFunction();
    }
}

function reloadP() {
    sessionStorage.setItem("reloading", "true");
    document.location.reload();
}
