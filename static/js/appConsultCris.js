
function consult_inventory() {
    id = document.getElementById('ident').value
    fetch('/consult_inventory', {
        "method":"post",
        "headers":{"Content-Type":"application/json"},
        "body": JSON.stringify(id)
    })
}