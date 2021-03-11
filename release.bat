@echo off

if exist venv rd /s/q venv
if exist dist rd /s/q dist
if exist build rd /s/q build
if exist release rd /s/q release

echo Please wait...

python -m venv venv
venv\Scripts\python -m pip install --upgrade pip
venv\Scripts\python -m pip install pyinstaller

venv\Scripts\pyinstaller --clean --onefile Crawl.py
copy default.ini dist
copy readme.md dist

rename dist release
if exist build rd /s/q build
if exist dist rd /s/q dist
if exist Crawl.spec del Crawl.spec
