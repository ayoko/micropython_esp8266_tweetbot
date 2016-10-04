# Twitter bot for MicroPython v1.8.4 (ESP8166)
#
# Copyright (c) 2016, Atsushi Yokoyama, Firmlogics (http://flogics.com)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
#       copyright notice, this list of conditions and the following
#       disclaimer in the documentation and/or other materials provided
#       with the distribution.
#     * Neither the name of the <organization> nor the names of its
#       contributors may be used to endorse or promote products derived
#       from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT
# HOLDER> BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# import esp
# esp.sleep_type(esp.SLEEP_MODEM)

global sta_if

def start_network():
    global sta_if
    import network
    sta_if = network.WLAN(network.STA_IF)

def wait_network_up():
    import time
    while not sta_if.isconnected():
        time.sleep_ms(100)
        print(sta_if.ifconfig())
    print("Now connected")
    print(time.ticks_ms(), "ms")

###############################################################################

def rm_tweet_txt():
    import os
    os.remove('tweet.txt')

start_network()
wait_network_up()

try:
    f = open('tweet.txt', 'r')
    str = f.read(4096)
    f.close()

    import usocket
    import ussl
    s=usocket.socket()
    addr = usocket.getaddrinfo("api.twitter.com", 443)[0][-1]
    s.connect(addr)
    s=ussl.wrap_socket(s)
    print(s)
    s.write(str)
    print(s.read(4096))
    s.close()
    rm_tweet_txt()
    
except:
    import tweet
    import esp
    esp.deepsleep(1)
