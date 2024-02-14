from playwright.sync_api import sync_playwright
import time
import json

def join_meeting_and_extract_transcripts(meeting_url, js_code, output_file_path):
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        context.grant_permissions(["camera", "microphone"])
        page = context.new_page()

        # Navigate to the meeting URL
        page.goto(meeting_url)
        page.wait_for_load_state("networkidle")
        # Wait for the meeting to be fully joined
        # page.wait_for_selector("selector-indicating-meeting-started", timeout=60000)
        # page.wait_for_timeout(60000)
        page.get_by_label("Join meeting from this browser").click()
        page.get_by_placeholder("Type your name").click()
        page.get_by_placeholder("Type your name").fill("demo data")
        page.get_by_role("button", name="Open device settings", exact=True).click()
        page.get_by_label("Noise suppression", exact=True).click()
        page.get_by_label("Noise suppression", exact=True).click()
        page.get_by_label("Audio devices").click()
        page.get_by_role("combobox", name="Audio devices").click()
        page.get_by_label("Choose your video and audio").click()
        page.get_by_role("button", name="Close right pane").click()
        page.get_by_label("Mic on").click()
        page.get_by_label("More").click()
        page.get_by_label("Language and speech").click()
        page.get_by_label("Turn on live captions").click()

        # Execute initial JavaScript to setup local storage monitoring
        page.evaluate(js_code)

        # Loop to periodically extract transcripts and update the local file
        try:
            while True:
                # Extract transcript data from local storage or directly from the DOM
                transcripts_data = page.evaluate("() => localStorage.getItem('transcripts')")
                if transcripts_data:
                    # Convert JSON string to Python dictionary
                    transcripts = json.loads(transcripts_data)
                    # Write or append the data to a local file
                    with open(output_file_path, 'w') as f:
                        json.dump(transcripts, f, indent=2)

                time.sleep(10)  # Adjust the delay as needed
        except KeyboardInterrupt:
            print("Stopping transcripts extraction...")
        finally:
            browser.close()

# JavaScript code to monitor and store transcripts
js_code = "/index.js"



if __name__ == "__main__":
    meeting_url = "https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3Ameeting_Yzk5NTNkMjUtNmNjMi00MzVhLWI4YjktOWRjM2ExNDZmMTFh%40thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223a0fdda6-105d-4fce-bb8a-1ed83b71e72b%2522%252c%2522Oid%2522%253a%25220a8fa023-4e79-4707-8e59-ee681a7196f0%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=e1b8ba68-bc64-4199-809b-825aba7adb53&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true"  # Replace with your meeting URL
    output_file_path = "transcripts.txt"  # Path to the output file
    join_meeting_and_extract_transcripts(meeting_url, js_code, output_file_path)