# gmail-smart-light-integration
basic notification python script, which changes the light color upon receiving new emails, made for remote work environment, can be customized further depending upon needs.

link to tinytuya github: https://github.com/jasonacox/tinytuya

google gmail api official page: https://developers.google.com/gmail/api


<h1>Notes:</h1>
<ul>
<li>Before you run the notifier script, you will have to get your credentials from https://console.cloud.google.com , in there Enable the Gmail API and you can get the credentials from there</li>
<li>then all of the required python packages are mentioned in the requirements.txt -install them in a virtual env</li>
<li>make sure to read the readme on tinytuya github to initialize your smart lights account on tuya platform</li>
<li>tuya has both lan controls and cloud controls, right now the notifier script works via the lan mode for easy integration with raspberry pi</li>
<li>If you dont have rashberry pi, after the first time of running the script you will receive the token.json, now along with both credentials.json and token.json you can run the script anywhere on a vps or even a android python clients</li>
</ul>
