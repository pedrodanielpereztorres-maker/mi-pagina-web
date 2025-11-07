document.addEventListener('animationstart', function(event) {
    if (event.animationName === 'onAutoFillStart') {
        // Input field has been autofilled
        event.target.style.color = 'white';
        event.target.style.webkitTextFillColor = 'white';
        event.target.style.backgroundColor = 'black'; // Add this line
        event.target.style.boxShadow = '0 0 0px 1000px black inset'; // Add this line for WebKit background fix
    }
}, true);

document.addEventListener('animationend', function(event) {
    if (event.animationName === 'onAutoFillStart') {
        // Input field has been autofilled
        event.target.style.color = 'white';
        event.target.style.webkitTextFillColor = 'white';
        event.target.style.backgroundColor = 'black'; // Add this line
        event.target.style.boxShadow = '0 0 0px 1000px black inset'; // Add this line for WebKit background fix
    }
}, true);

// Also apply styles on page load for already autofilled fields
document.querySelectorAll('input:-webkit-autofill, textarea:-webkit-autofill').forEach(function(el) {
    el.style.color = 'white';
    el.style.webkitTextFillColor = 'white';
    el.style.backgroundColor = 'black'; // Add this line
    el.style.boxShadow = '0 0 0px 1000px black inset'; // Add this line for WebKit background fix
});