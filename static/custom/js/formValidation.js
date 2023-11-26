function validateForm() {
    // Check if a file is selected
    const fileInput = document.getElementById('fileInput');
    if (fileInput.files.length === 0) {
        alert('Please select a file.');
        return false;
    }

    // Check if at least one checkbox is selected
    const checkboxes = document.querySelectorAll('input[name="playerRoles"]');
    let atLeastOneChecked = false;
    checkboxes.forEach((checkbox) => {
        if (checkbox.checked) {
            atLeastOneChecked = true;
        }
    });

    if (!atLeastOneChecked) {
        alert('Please select at least one role.');
        return false;
    }

    return true; // Form will be submitted
}