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

<br>
<h1>notifier script on android setup</h1>
Using <a href="https://wiki.termux.com/"><strong>Termux<strong></a>+<a href="https://ss64.com/bash/screen.html">screen</a> is the best way to run python scripts in android.
<ul>
<li>Never download Termux from playstore(TL;DR Termux developers update fdroid page before playstore). I cant stress this enough: you will have to download Termux from its offical F-Droid page, link: https://f-droid.org/packages/com.termux/ <em>ps:you dont have to download fdroid, you can download latest termux builds direct from F-Droid offical page.</em></li>
<li>Run the following commands in Termux:</li>
<ul>
<li> <a href="https://wiki.termux.com/wiki/Package_Management">pkg install package-name</a> </li>
<li> <a href="https://wiki.termux.com/wiki/Python">pkg install python</a> </li>
<li> <a href="https://www.freshports.org/sysutils/screen/">pkg install screen</a> </li>
<li> <a href="https://wiki.termux.com/wiki/Termux-setup-storage">termux-setup-storage<a> </li>
</ul>
<li>Once you run the termux-setup-storage command, you will get a pop up asking for permission/s related to storate, make sure to allow it.</li>
<li>Now you should have access to android storage from Termux. culb the notifier.py,credentials.json,token.json and requirements.json into a folder and send that folder to android storage(usually not into any folders on android, just on the top most level)</li>
<li>now that you have the files in a folder on andorid, on Termux use commands like ls and cd to navigate to the folder (<a href="https://hacksland.net/termux-command-list">reference link</a>) </li>
<li>once you are in the project folder, do the following commands:</li>
<ul>
<li> <a href="https://pip.pypa.io/en/stable/cli/pip_install/">pip install -r requirements.txt</a> </li>
<li> <a href="https://ss64.com/bash/screen.html">screen</a> </li>
<li> python notifier.py </li>
<li> <a href="https://ss64.com/bash/screen.html">Control-a d</a> <em>(This will detach the screen, to execute this command properly do 'ctr-a' immediately followed by 'd' )</em> </li>
<li> <a href="https://wiki.termux.com/wiki/Termux-wake-lock">termux-wake-lock</a> </li>
</ul>
<li>Once you run the termux-wake-lock command, you will get a pop up asking for permission/s related to battery optimization, make sure to allow it.</li>
<li>Normally we would exit out of Termux by using 'exit' command, make sure to not use it:) you will need termux running the session in background for the notifications to work, just close the app with out using the exit command and you should be able to see it running on your notifications dropdown on android.</li>
<li>Once you have completed the setup, you should be able to see something like this below:</li>
<image src="https://user-images.githubusercontent.com/25448502/187714075-3b9eff3a-23aa-4b63-a7d7-944f2a35b734.png">
<li>Now android phone is acting like a smallest pocket friendly linux vps:) if anyone has any problems with the setup, create a issue on this github page</li>
</ul>

<br>
<h1>Known issues and todo's:</h1>
<ul>
<li>When the router goes offline, your ip of the smart lights can get changed and this setup will not work anymore, you will have to find the new ip and change the value of ip in the notifier.py....... I believe This can be fixed easily by using cloud based controls for the smart light rather then local lan controls or if need to have lan control then We can add a method to get the ip of the smartblubs by scanning the local devices(when ever network resets) rather then getting it static like now</li>
</ul>
