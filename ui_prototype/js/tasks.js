document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll("button");
    let completed = {
        dsa: false,
        dev: false
    };

    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            if (btn.innerText.includes("DSA")) {
                completed.dsa = true;
                btn.disabled = true;
                btn.innerText = "DSA Completed";
            }

            if (btn.innerText.includes("REST")) {
                completed.dev = true;
                btn.disabled = true;
                btn.innerText = "Dev Completed";
            }

            if (completed.dsa && completed.dev) {
                let streak = AppState.get("streak") || 0;
                streak += 1;
                AppState.set("streak", streak);
                alert("🎉 Both tasks completed! Streak increased.");
            }
        });
    });
});
