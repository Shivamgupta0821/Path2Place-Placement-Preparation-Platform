document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");

    if (!form) return;

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        if (!email || !password) {
            alert("Please fill all fields");
            return;
        }

        // Simulate successful login
        AppState.set("isLoggedIn", true);

        window.location.href = "username.html";
    });
});
