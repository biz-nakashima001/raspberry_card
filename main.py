# -*- coding: UTF-8 -*-
from datetime import datetime
from datetime import date
from pytz import timezone
import time
import json
import nfc
import jtalk
import music
# import slackapi
import kintoneapi

def on_startup(targets):
        print("ready...")
        return targets

def on_connect(tag):
    if tag.ndef:
        music.hello()
        record = tag.ndef.records[0]
        cardId = record.data[3:10]

        #レコードの取得
        memberData = kintoneapi.getMember(cardId)
        if len(memberData['records']) != 0:
            #本日
            today = datetime.today()
            #会員No
            memberNo = json.dumps(memberData['records'][0]['member_no']['value'],indent=4, ensure_ascii=False).strip('"')
            print("memberNo : " + memberNo)
            isExistUpdate = False
            #次回更新日付
            strNextUpdate = json.dumps(memberData['records'][0]['next_update_date']['value'],indent=4, ensure_ascii=False).strip('"')
            if strNextUpdate and strNextUpdate != "null":
                isExistUpdate = True
                nextUpdateDate = datetime.strptime(strNextUpdate.strip('"'), '%Y-%m-%d')
            
            #slack用
            # nowDate = datetime.now(timezone('Asia/Tokyo'))
            # output = "Card ID " + cardId + " : " + str(nowDate)

            #期限切れ
            if isExistUpdate and today > nextUpdateDate: 
                #slackapi.kigen(cardId, nowDate, output)
                music.kigen()
                jtalk.kigen()
            else:
                #レコードの取得
                usage = kintoneapi.getUsage(memberNo)
                print("usage")
                print(usage)
                
                #本日エントリー済み
                if len(usage['records']) != 0:
                    recordId = json.dumps(usage['records'][0]['record_Id']['value'],indent=4, ensure_ascii=False).strip('"')
                    t_now = datetime.now(timezone('Asia/Tokyo')).replace(microsecond=0) 
                    result = kintoneapi.putUsage(recordId, t_now.isoformat())
                    #slackapi.out(cardId, nowDate, output)
                    # music.hello()
                    music.goodby()
                    jtalk.goodby()

                #本日初回
                else:
                    kana = json.dumps(memberData['records'][0]['kana']['value'],indent=4, ensure_ascii=False).strip('"')
                    result = kintoneapi.postUsage(memberNo, kana)
                    # print("memberNo")
                    # print(memberNo)
                    # result = kintoneapi.postUsage(memberNo)
                    # slackapi.entry(cardId, nowDate, output)
                    # music.hello()
                    #jtalk.hello()
        else:
            #登録してないカードのとき
            music.kigen()
            jtalk.mitouroku()

        return True    

def on_release(tag):
        print("on_release()")
        if tag.ndef:
            print(tag.ndef.message.pretty())
        return True

clf = nfc.ContactlessFrontend('usb')
while True: 
    if clf:
        print("Clf: {}".format(clf))
        clf.connect(rdwr={
                'on-startup': on_startup,
                'on-connect': on_connect,
                'on-release': on_release
        })
clf.close()
