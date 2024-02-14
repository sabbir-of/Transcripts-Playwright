from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.grant_permissions(["camera", "microphone"])
    page = context.new_page()

    page.goto("https://teams.microsoft.com")
    # Add steps to log in
    page.fill('input[type="email"]', "inputemail")
    page.click('input[type="submit"]')
    page.wait_for_load_state("networkidle")
    page.fill("//input[@type='password']", "inputpassword")
    page.click('#idSIButton9')

    page.wait_for_load_state("networkidle")
    page.click('[type="submit"]')
    page.wait_for_load_state("networkidle")

    # Navigate to the specific call
    page.goto("https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fmeetup-join%2F19%3Ameeting_Yzk5NTNkMjUtNmNjMi00MzVhLWI4YjktOWRjM2ExNDZmMTFh%40thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223a0fdda6-105d-4fce-bb8a-1ed83b71e72b%2522%252c%2522Oid%2522%253a%25220a8fa023-4e79-4707-8e59-ee681a7196f0%2522%257d%26anon%3Dtrue&type=meetup-join&deeplinkId=e1b8ba68-bc64-4199-809b-825aba7adb53&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true")

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
    page.get_by_role("button", name="Confirm").click()

    with open("/index.js", "r") as file:
        script_content = file.read()
    # Inject JavaScript code to monitor and update transcripts in localStorage
    resut = page.evaluate(script_content)
    print(resut)
    # Wait for a certain time or condition before finishing
    page.wait_for_timeout(60000)  # Waits for 60 seconds, adjust as needed

    # Retrieve data from localStorage
    transcript = page.evaluate("localStorage.getItem('teamsTranscript')")
    print(transcript)

    # Close browser
    browser.close()

with sync_playwright() as playwright:
    run(playwright)