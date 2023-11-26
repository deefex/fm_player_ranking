// script.js

document.addEventListener("DOMContentLoaded", function () {
    // Array to store selected roles
    let selectedRoles = [];

    // Function to update the selected roles pills and count
    function updateSelectedRoles() {
        const pillsContainer = document.getElementById("selectedRolesPills");
        const countElement = document.getElementById("selectedRolesCount");

        // Clear existing pills
        pillsContainer.innerHTML = "";

        // Display "No roles selected" if no roles are selected
        if (selectedRoles.length === 0) {
            pillsContainer.innerHTML = '<span class="badge bg-secondary">No roles selected</span>';
        } else {
            // Display selected roles pills
            selectedRoles.forEach(role => {
                const pill = document.createElement("span");
                pill.className = "badge bg-primary me-1";
                pill.textContent = role;
                pillsContainer.appendChild(pill);
            });
        }

        // Update the selected roles count
        countElement.textContent = selectedRoles.length;

        // Disable remaining checkboxes if 8 roles are selected
        const checkboxes = document.querySelectorAll('input[name="playerRoles"]');
        checkboxes.forEach((checkbox) => {
            checkbox.disabled = selectedRoles.length >= 8 && !checkbox.checked;
        });
    }

    // Initialize 'No roles selected' pill
    updateSelectedRoles();

    // Event listener for checkbox changes
    document.querySelectorAll('input[name="playerRoles"]').forEach((checkbox) => {
        checkbox.addEventListener("change", function () {
            if (this.checked) {
                // Add the role label to the selectedRoles array
                selectedRoles.push(this.nextElementSibling.textContent.trim());
            } else {
                // Remove the role label from the selectedRoles array
                selectedRoles = selectedRoles.filter(role => role !== this.nextElementSibling.textContent.trim());
            }

            // Update the selected roles pills and count
            updateSelectedRoles();
        });
    });
});