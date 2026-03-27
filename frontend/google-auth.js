class GoogleAuth {
    constructor() {
        this.clientId = "206629117246-4aqmemu30i8ednehpgrctseb65c7gt7l.apps.googleusercontent.com";
        this.apiBase = "http://127.0.0.1:8000/api/";
        this.tokenClient = null;
        this.isRequestInProgress = false;
    }

    login() {
        if (typeof google === "undefined") {
            alert("Google script not loaded");
            return;
        }

        if (this.isRequestInProgress) {
            return;
        }

        if (!google.accounts || !google.accounts.oauth2) {
            alert("Google OAuth client not available");
            return;
        }

        if (!this.tokenClient) {
            this.tokenClient = google.accounts.oauth2.initTokenClient({
                client_id: this.clientId,
                scope: "openid email profile",
                callback: this.handleTokenResponse.bind(this)
            });
        }

        this.isRequestInProgress = true;
        this.tokenClient.requestAccessToken({ prompt: "consent" });
    }

    async handleTokenResponse(tokenResponse) {
        try {
            if (!tokenResponse || !tokenResponse.access_token) {
                throw new Error("No access token returned from Google");
            }

            console.log("Google Token:", tokenResponse.access_token);

            const profileRes = await fetch("https://www.googleapis.com/oauth2/v3/userinfo", {
                headers: {
                    "Authorization": "Bearer " + tokenResponse.access_token
                }
            });

            if (!profileRes.ok) {
                throw new Error("Unable to fetch Google user profile");
            }

            const payload = await profileRes.json();
            console.log("User Info:", payload);

            const res = await fetch(this.apiBase + "google-login/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email: payload.email,
                    name: payload.name
                })
            });

            if (!res.ok) {
                const errorText = await res.text();
                console.error("Backend login error:", errorText);
                throw new Error("Backend login failed with status: " + res.status);
            }

            let data;
            try {
                data = await res.json();
            } catch (e) {
                console.error("Failed to parse backend response as JSON:", e);
                throw new Error("Invalid response from server");
            }

            if (!data.success) {
                alert("Backend login failed: " + (data.message || "Unknown error"));
                return;
            }

            const userData = {
                id: data.user_id || payload.sub || ("user_" + Date.now()),
                name: data.name || payload.name || "User",
                email: payload.email || "",
                role: data.role || "citizen",
                authorityLevel: data.authority_level || null,
                district: "central"
            };

            localStorage.setItem("user", JSON.stringify(userData));
            localStorage.setItem("currentUser", JSON.stringify(userData));
            localStorage.setItem("token", tokenResponse.access_token);

            alert("Login successful: " + payload.name);

            // Redirect to dashboard instead of home
            if (typeof showPage === "function") {
                showPage("citizenDashboard");
            } else {
                window.location.href = "/index.html#citizenDashboard";
            }

        } catch (error) {
            console.error(error);
            alert("Google login failed");
        } finally {
            this.isRequestInProgress = false;
        }
    }
}

window.googleAuth = new GoogleAuth();
