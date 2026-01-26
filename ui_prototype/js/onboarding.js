document.addEventListener("DOMContentLoaded", () => {
    const usernameInput = document.querySelector("input");
    const form = document.querySelector("form");

    if (!form) return;

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const username = usernameInput.value.trim();

        const valid =
            username.length >= 3 &&
            username.length <= 20 &&
            /^[a-zA-Z0-9_]+$/.test(username);

        if (!valid) {
            alert("Invalid username");
            return;
        }

        AppState.set("username", username);
        window.location.href = "field.html";
    });
});
// Field selection logic
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const radios = document.querySelectorAll("input[type='radio']");

    if (!form || radios.length === 0) return;

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        let selectedField = null;

        radios.forEach(radio => {
            if (radio.checked) {
                selectedField = radio.nextElementSibling.querySelector("h3").innerText;
            }
        });

        if (!selectedField) {
            alert("Please select a field");
            return;
        }

        AppState.set("field", selectedField);
        AppState.set("streak", 0);

        window.location.href = "tasks.html";
    });
});
