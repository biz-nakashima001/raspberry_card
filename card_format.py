import nfc

def on_connect(tag):
        print("format:", tag.format())

clf = nfc.ContactlessFrontend('usb')
if clf:
        print("Clf: {}".format(clf))
        clf.connect(rdwr={
                'on-connect': on_connect
        })

clf.close()
