[app]
title = KaliCMD Toolkit
package.name = kalicmdtoolkit
package.domain = org.hackerai
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,pyperclip,plyer
orientation = portrait
fullscreen = 0
android.archs = arm64-v8a,armeabi-v7a
android.api = 33
android.minapi = 21
android.permissions = INTERNET
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1