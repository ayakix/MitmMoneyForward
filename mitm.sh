#!/bin/sh

set -e

proxy_on() {
  networksetup -setwebproxy Wi-Fi localhost 8080
  networksetup -setwebproxystate Wi-Fi on
  networksetup -setsecurewebproxy Wi-Fi localhost 8080
  networksetup -setsecurewebproxystate Wi-Fi on
}

proxy_off() {
  retval=$?
  networksetup -setwebproxystate Wi-Fi off
  networksetup -setsecurewebproxystate Wi-Fi off
  exit $retval
}

trap proxy_off INT QUIT TERM EXIT
proxy_on
mitmproxy -s ./mitm.py --ignore-hosts '(crashlytics.com|googlesyndication.com|gstatic.com|doubleclick.net|mixpanel.com|dropbox.com)' "$@"
