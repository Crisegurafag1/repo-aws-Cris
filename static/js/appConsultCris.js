function consult_inventory() {
    let id = document.getElementById('ident').value;
    fetch('/consult_inventory', {
        method: "post",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({id: id})
    })
    .then(resp => resp.json())
    .then(data => {
        if (data.error) {
            console.error('Error:', data.error);
            document.getElementById("result").value = "No data found";
            document.getElementById("photo").style.display = "none";
        } else {
            document.getElementById("result").value = data.marca + "\n" + data.modelo + "\n" + data.color;
            document.getElementById("photo").src = data.photo_url;
            document.getElementById("photo").style.display = "block";
        }
    })
    .catch(error => console.error('Error:', error));
}
