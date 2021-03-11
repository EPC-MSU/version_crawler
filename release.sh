python3 -c "import tkinter"

if [ $? -eq 0 ]; then
    echo "Tkinter is installed."
else
    echo "Tkinter is not installed. Run sudo apt-get install python3-tk"
    exit -1
fi


if [-d venv ]; then rm -rf venv; fi;
if [-d dist ]; then rm -rf dist; fi;
if [-d build ]; then rm -rf build; fi;
if [-d release ]; then rm -rf release; fi;

echo Please wait
python3 -m venv venv

venv/bin/python -m pip install --upgrade pip
venv/bin/python -m pip install pyinstaller

venv/bin/pyinstaller --clean --onefile Crawl.py
cp default.ini dist/
cp readme.md dist/

mv -R dist release
if [ -d build ]; than rm -rf build; fi;
if [ -d dist ]; than rm -rf dist; fi;
