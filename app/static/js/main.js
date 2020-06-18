// ask if you want to delete the user or not:
const btnDelete = document.querySelectorAll('.btn-delete');

if (btnDelete) {
    const btnArray = Array.from(btnDelete);
    btnArray.forEach((btn) => {
        btn.addEventListener('click', (e) => {
            if(!confirm('Are you sure you want to delete it?')) {
                e.preventDefault();
            }
        });
    });
}

// Close flash message-info:
const $btnCloseMessage = document.getElementById('btn-close-message'); //show-hide');

$btnCloseMessage.addEventListener('click', (e) => {
    const $hideMessage = document.getElementById('show-hide');
    $hideMessage.parentNode.removeChild($hideMessage);
});