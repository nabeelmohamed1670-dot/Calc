[app]
title = Calc
package.name = calc
package.domain = org.nabeel
source.dir =.
source.include_exts = py,kv,png,jpg,jpeg
version = 0.1
requirements = python3,kivy==2.3.1,cython,sdl2,setuptools,meson,ninja,pyjnius
orientation = portrait
fullscreen = 1
android.archs = arm64-v8a
android.api = 31
android.minapi = 21
android.ndk = 25b
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
p4a.source_dir =

[buildozer]
log_level = 2
warn_on_root = 1
