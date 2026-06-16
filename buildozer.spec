[app]
title = Calc
package.name = calc
package.domain = org.nabeel
source.dir =.
source.include_exts = py,kv,png
version = 0.1
requirements = python3,kivy==2.3.1,cython,sdl2,setuptools
orientation = portrait
fullscreen = 1
icon.filename = logo.png
android.archs = arm64-v8a
android.ndk = 25b
p4a.branch = master

[buildozer]
log_level = 2
