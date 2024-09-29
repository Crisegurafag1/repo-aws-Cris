
function consult_inventory() {
    id = document.getElementById('ident').value
    fetch('/consult_inventory', {
        "method":"post",
        "headers":{"Content-Type":"application/json"},
        "body": JSON.stringify(id)
    })
    .then(resp => resp.json())
    .then(data => 
        
        alert(data.marca))
}