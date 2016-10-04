# micropython_esp8266_tweetbot
Tweet bot for MicroPython v1.8.4 (ESP8266)

This program is a Tweet bot (Twitter status updater) for MicroPython ESP8266.
Confirmed working with MicroPython 1.8.4.

One problem is, this program consumes a lot of heap memory, so it will not run
if you add more functionality.

To run, we need a modified hmac.py which is compatible with SHA1.  We can
obtain the code below even though it is not marged to the main stream, yet.

https://github.com/micropython/micropython-lib/pull/82/files

Any question, please send email to yokoyama@flogics.com though I may not have time to answer clearly.

Thanks you.

Yokoyama, Atsushi
Firmlogics
http://flogics.com
