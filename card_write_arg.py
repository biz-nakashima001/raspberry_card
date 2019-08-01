import nfc
import sys

def on_startup(targets):
    if len(args) <= 1:
        print("please enter more args!!!")
        return False
    else:
        print("on_startup()")
        return targets

def on_connect(tag):
        print("Tag: {}".format(tag))
        print("Tag type: {}".format(tag.type))
        #print '\n'.join(tag.dump())
        if tag.ndef:
            id = args[1]
            record = nfc.ndef.TextRecord(id)
            tag.ndef.message = nfc.ndef.Message(record)
            print tag.ndef.message.pretty()
        return True

def on_release(tag):
        print("on_release()")
        if tag.ndef:
                print(tag.ndef.message.pretty())

args = sys.argv
clf = nfc.ContactlessFrontend('usb')
if clf:
        print("Clf: {}".format(clf))
        clf.connect(rdwr={
                'on-startup': on_startup,
                'on-connect': on_connect,
                'on-release': on_release
        })

clf.close()
