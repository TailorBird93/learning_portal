// Show Spinner on Form Submit
document.querySelectorAll("form").forEach((form) => {
    form.addEventListener("submit", () => {
        const spinner = document.getElementById("spinner");
        if (spinner) {
            spinner.classList.remove("d-none");
        }
    });
});

// Toast Notifications
function showToast(message) {
    const toastEl = document.getElementById("toast");
    if (toastEl) {
        const toastBody = toastEl.querySelector(".toast-body");
        toastBody.textContent = message;

        const toast = new bootstrap.Toast(toastEl);
        toast.show();
    }
}

