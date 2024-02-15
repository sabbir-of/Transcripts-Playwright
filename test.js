if (localStorage.getItem("transcripts") !== null) {
        localStorage.removeItem("transcripts");
    }

    const transcriptArray = JSON.parse(localStorage.getItem("transcripts")) || [];

    function checkTranscripts() {
        const iframe = document.querySelector('iframe');
        const transcripts = iframe.contentWindow.document.querySelectorAll('.ui-chat__item');
        transcripts.forEach(transcript => {
            const ID = transcript.querySelector('.fui-Flex > .ui-chat__message').id;
            const Name = transcript.querySelector('.ui-chat__message__author').innerText;
            const Text = transcript.querySelector('.fui-StyledText').innerText;
            const Time = new Date().toISOString().replace('T', ' ').slice(0, -1);

            const index = transcriptArray.findIndex(t => t.ID === ID);

            if (index > -1) {
                if (transcriptArray[index].Text !== Text) {
                    // Update the transcript if text changed
                    transcriptArray[index] = { Name, Text, Time, ID };
                }
            } else {
                console.log({ Name, Text, Time, ID });
                // Add new transcript
                transcriptArray.push({ Name, Text, Time, ID });
            }
        });

        localStorage.setItem('transcripts', JSON.stringify(transcriptArray));
    }

    const observer = new MutationObserver(checkTranscripts);
    observer.observe(document.body, { childList: true, subtree: true });

    setInterval(checkTranscripts, 10000);

    // Download JSON
    function downloadJSON() {
        let transcripts = JSON.parse(localStorage.getItem('transcripts'));
        // Remove IDs
        transcripts = transcripts.map(({ID, ...rest}) => rest);

        // Stringify with pretty printing
        const prettyTranscripts = JSON.stringify(transcripts, null, 2);

        // Use the page's title as part of the file name, replacing "__Microsoft_Teams" with nothing
        // and removing any non-alphanumeric characters except spaces
        let title = document.title.replace("__Microsoft_Teams", '').replace(/[^a-z0-9 ]/gi, '');
        const fileName = "transcript - " + title.trim() + ".json";

        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(prettyTranscripts);
        const downloadAnchorNode = document.createElement('a');
        downloadAnchorNode.setAttribute("href", dataStr);
        downloadAnchorNode.setAttribute("download", fileName);
        document.body.appendChild(downloadAnchorNode); // required for firefox
        downloadAnchorNode.click();
        downloadAnchorNode.remove();
    }

    // Let's download the JSON
    // downloadJSON();