# qa_has_power

1. Install latest stable Firefox version (https://www.mozilla.org/pl/firefox/new/)
2. Download latest gecko driver version for your OS (https://github.com/mozilla/geckodriver/releases)
3. Unpack gecko driver

```
tar -xvzf geckodriver*
```
4. Move gecko driver file to `/usr/local/bin/` directory

```
cp geckodriver /usr/local/bin/
```
5. Install selenium (best practise in python virtualenv)

```
pip install -U selenium
```
6. Run test from qa_has_power repository

```
cd qa_has_power
python test.py
```
7. You should see `stxnext.com` on new firefox instance
