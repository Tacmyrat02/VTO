// Webcam işlemleri
const video = document.getElementById('webcam');
const canvas = document.getElementById('canvas');
const captureBtn = document.getElementById('capture-btn');

// Webcam açmak
if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
        })
        .catch(error => {
            console.error("Webcam error: ", error);
        });
}

// Try-on prosesi
function processTryOn(imageData, productId) {
    fetch('/tryon/webcam/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            image: imageData,
            product_id: productId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // Netijäni görkez
            updateResultImage(data.result_image);
        }
    });
}