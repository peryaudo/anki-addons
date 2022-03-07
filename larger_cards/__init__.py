from anki.hooks import addHook
from aqt import mw
import subprocess

def onPrepareQA(text, card, kind):
    return '<span style="font-size: 200%;">' + text + '</span>'

addHook("prepareQA", onPrepareQA)
