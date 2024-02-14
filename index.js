function monitorTranscripts() {
  // Function to extract transcript data
  function extractTranscriptData() {
    // Replace with the actual selector for transcript text in Microsoft Teams.
    // This is just a placeholder selector.
    const transcriptSelector = "div.fui-Flex.___inloz00";
    const transcriptElement = document.querySelector(transcriptSelector);

    return transcriptElement ? transcriptElement.innerText : "";
  }

  // Function to update transcripts in localStorage
  function updateTranscripts(newData) {
    let existingTranscripts = localStorage.getItem("teamsTranscripts");
    existingTranscripts = existingTranscripts
      ? JSON.parse(existingTranscripts)
      : [];

    // Add new transcript data
    existingTranscripts.push(newData);

    // Update localStorage
    localStorage.setItem(
      "teamsTranscripts",
      JSON.stringify(existingTranscripts)
    );
  }

  // Monitor and update transcripts every 10 seconds
  setInterval(() => {
    const newTranscriptData = extractTranscriptData();
    if (newTranscriptData) {
      updateTranscripts(newTranscriptData);
    }
  }, 10000); // Adjust the interval as needed
}

// Start monitoring transcripts
monitorTranscripts();
