function register_inventory() {
    let formData = new FormData(document.getElementById('registerForm'));
    
    fetch('/register_inventory', {
        method: "post",
        body: formData
    })
    .then(resp => resp.json())
    .then(data => {
        showNotification(data.message);
    })
    .catch(error => {
        console.error('Error:', error);
        showNotification('Error adding motorcycle');
    });
}

function showNotification(message) {
    let notification = document.getElementById('notification');
    notification.innerText = message;
    notification.style.display = 'block';
    setTimeout(() => {
        notification.style.display = 'none';
    }, 5000);
}
