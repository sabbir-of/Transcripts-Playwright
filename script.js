function transcript() {
  // Function to monitor transcript updates
  function monitorTranscripts() {
    // Logic to extract transcript data
    // This could be from a DOM element, an API response, etc.
    let newTranscriptData = extractTranscriptData();

    // Get existing transcripts from localStorage
    let existingTranscripts = localStorage.getItem("transcripts");
    existingTranscripts = existingTranscripts
      ? JSON.parse(existingTranscripts)
      : [];

    // Update transcripts in localStorage
    existingTranscripts.push(newTranscriptData);
    localStorage.setItem("transcripts", JSON.stringify(existingTranscripts));
  }

  // Function to extract transcript data
  // Replace this with the actual logic for your specific case
  function extractTranscriptData() {
    // Example: Extracting text from a DOM element
    let transcriptElement = document.querySelector("//h3[@dir='auto']");
    return transcriptElement ? transcriptElement.innerText : "";
  }

  // Set an interval to periodically check for updates
  // Adjust the interval time as needed
  setInterval(monitorTranscripts, 10000); // 10 seconds
}
