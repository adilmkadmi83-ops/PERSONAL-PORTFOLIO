const GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwkV2vj6Ng-hdchHZvLbEIjuaD0JQ0m91HujP961Hew4pl-8BsLq2KkXBZBSftsuyku5A/exec";

// Helper to check if Google Sheets integration is configured
function isGoogleSheetsConfigured() {
    return typeof GOOGLE_SCRIPT_URL !== 'undefined' &&
           GOOGLE_SCRIPT_URL && 
           GOOGLE_SCRIPT_URL !== "YOUR_GOOGLE_SCRIPT_URL" &&
           GOOGLE_SCRIPT_URL.trim() !== "";
}
