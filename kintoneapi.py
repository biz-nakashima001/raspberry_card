# -*- coding: UTF-8 -*-
import api
import json
import datetime

開発環境用設定
URL = "https://devzxtnwd.cybozu.com/k/v1/" #テスト
API_TOKEN = "bmFrYXNpbjUyQGxpdmUuanA6eHIxaDh2MGw=" #テスト
MEMBER_DB_APP_ID = 3
USAGE_APP_ID = 4

# # 本番環境用設定
# URL = "" #本番
# API_TOKEN = "" #本番
# MEMBER_DB_APP_ID = 1
# USAGE_APP_ID = 38

# 会員メンバー取得
def getMember(cardId):
    query = 'card_no = \"' + cardId + '\"'
    print(query)
    params = {"app": MEMBER_DB_APP_ID, "query":query}
    files = {"X-Cybozu-Authorization": API_TOKEN}
    resp = api.getJson(URL + 'records.json', params, files)
    data = resp.json()
    return data

# 利用記録取得
def getUsage(memberNo):
    query = 'member_no = \"' + memberNo + '\" and usage_date = TODAY()'
    print(query)
    params = {"app": USAGE_APP_ID, "query":query}
    files = {"X-Cybozu-Authorization": API_TOKEN}
    resp = api.getJson(URL + 'records.json', params, files)
    data = resp.json()
    return data

# 利用記録登録
def postUsage(memberNo, kana):
    params = {"app": USAGE_APP_ID,"record": {"member_no": {"value": memberNo}, "kana": {"value": kana}}}
    files = {"X-Cybozu-Authorization": API_TOKEN,"Content-Type": "application/json"}
    resp = api.postJson(URL + 'record.json', params, files)
    data = resp.json()
    return data

# 利用記録更新
def putUsage(recordId, t_now):
    print(recordId)
    print(t_now)
    params = {"app": USAGE_APP_ID,"id": recordId ,"record": {"leaving_date": {"value": t_now}}}
    files = {"X-Cybozu-Authorization": API_TOKEN,"Content-Type": "application/json"}
    resp = api.putJson(URL + 'record.json', params, files)
    data = resp.json()
    return data

#テスト用メソッド
if __name__ == "__main__":
    result = getMember('m000002')
    str_next_update_date =  json.dumps(result['records'][0]['next_update_date']['value'], indent=4, ensure_ascii=False)

    nowDate = datetime.date.today()

    strNextUpdateDate = datetime.datetime.strptime(str_next_update_date.strip('"'), '%Y-%m-%d')
    nextDate = datetime.date(strNextUpdateDate.year, strNextUpdateDate.month, strNextUpdateDate.day)

    if nowDate > nextDate:
        print("超えてます")
    else:
        print("超えてません")
    print(nowDate)
    print(nextDate)
