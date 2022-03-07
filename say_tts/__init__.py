from anki.hooks import addHook
from aqt import mw
import subprocess
import re

remove_style = re.compile('<style>.*</style>', re.MULTILINE | re.DOTALL)

def onShowQuestion():
    card = mw.reviewer.card
    q = remove_style.sub('', card.q())
    subprocess.Popen(["say", "-r", "200", "-v", "Samantha", q])

addHook("showQuestion", onShowQuestion)
