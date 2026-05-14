const SUPABASE_URL = "https://qbpbohrggxsxqhgplhng.supabase.co";

const SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFicGJvaHJnZ3hzeHFoZ3BsaG5nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzg2NTQ4OTgsImV4cCI6MjA5NDIzMDg5OH0.OQWytnXW5-WNRMWYM8gDB2qIb_IXpOsA1W271HvcnxU";

const client = supabase.createClient(
  SUPABASE_URL,
  SUPABASE_KEY
);

// REGISTER

const registerForm =
document.getElementById("registerForm");

if (registerForm) {

  registerForm.addEventListener(
    "submit",
    async (e) => {

      e.preventDefault();

      const email =
      document.getElementById(
        "registerEmail"
      ).value;

      const password =
      document.getElementById(
        "registerPassword"
      ).value;

      const confirmPassword =
      document.getElementById(
        "registerConfirm"
      ).value;

      if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return;
      }

      const { data, error } =
      await client.auth.signUp({
        email,
        password,
      });

      if (error) {
        alert(error.message);
      } else {
        alert("Registration Successful");
        window.location.href =
        "login.html";
      }
    }
  );
}

// LOGIN

const loginForm =
document.getElementById("loginForm");

if (loginForm) {

  loginForm.addEventListener(
    "submit",
    async (e) => {

      e.preventDefault();

      const email =
      document.getElementById(
        "loginEmail"
      ).value;

      const password =
      document.getElementById(
        "loginPassword"
      ).value;

      const { data, error } =
      await client.auth.signInWithPassword({
        email,
        password,
      });

      if (error) {
        alert(error.message);
      } else {
        alert("Login Successful");
        window.location.href =
        "home.html";
      }
    }
  );
}