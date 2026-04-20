import React from "react";
import ReactDOM from "react-dom/client";
import App from "./app/App";
import "./styles/index.css";

import { GoogleOAuthProvider } from "@react-oauth/google";
import { AuthProvider } from "./app/context/AuthContext";
ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <GoogleOAuthProvider clientId="228619658357-9jv2lcks7hqsqmn2mv3bjo7hp88f1p1u.apps.googleusercontent.com">
      <AuthProvider>
        <App />
      </AuthProvider>
    </GoogleOAuthProvider>
  </React.StrictMode>
);