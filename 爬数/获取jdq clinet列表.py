import pymysql
import requests
import time

url = "http://dp.jd.com/jdq/api/jrdw/topicManager/getClientListAjax.ajax"

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://dp.jd.com",
    "Pragma": "no-cache",
    "Referer": "http://dp.jd.com/jdq/dataPipe/consumer",
    "Sgm-Context": "398151085746154900;398151085746154900",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36",
    "Cookie": "__jdv=240971990|direct|-|none|-|1748396027027; jd.erp.lang=zh_CN; jdd69fo72b8lfeoe=P3RJR4JB5WC5F7OXTII6FKTDMZA25FJXBUJP444TJCDKRKQTCEC7BPFSJ4GLYP46PHBMYT6WUWJ4UVK5TNF22MRRJ4; sso.jd.com=BJ.723E83325748D82AC18C1AF647CBAACE.9920250528094828; __rtUser=%E9%A9%AC%E8%87%AA%E5%BC%BA(maziqiang4); __jdu=17483960270252013725649; me_token=ee.44396b0c8f00cfadf4ae030239a0aaa6; focus-token=ee.44396b0c8f00cfadf4ae030239a0aaa6; focus-team-id=00046419; focus-client=WEB; logbook_u=maziqiang4; erp=maziqiang4; lng=zh; ssa.origin-api=2b16bf126a49e58d7aaf7d6b8a0030b326ef6cf4f4f6bb391e108c4b30351f3baef6a2ff976836d1e6be1fc524d0863da6efa4b723775c42ad6ad65ab9930d99f1f2e30e631a89c99f3a364eb6fb6f81f0acb6c31aacdbba52da7e8768546db5280f0d89822bec51dd084a0a8a44791db14e7e7394db64113c5014fe0fc2e0b0; ssa.global.ticket=8bee13d084e5b7407f41b75ad23496c59706e7b60548a77d830e56413c479700; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Imx4VUNqYVFyQnZxem9tNnlIRmRlIiwiZXhwIjoxNzQ5MDkxMzc5LCJpYXQiOjE3NDg0ODY1Nzl9.C2s5sjPyL7tPNL81CwWCmrmsgyEHOaJSwxyzKKmIvAs; iam_token=eyJhbGciOiJIUzI1NiJ9.eyJ0bSI6IntcImV4cGlyZVwiOjE3NDg1NzI5ODM2NzcsXCJjcmVhdGVkVGltZVwiOjE3NDg0ODY1ODM2NzcsXCJoYXNPdHBcIjp0cnVlLFwiaWRcIjpcIkMwMlNXMVNHSDA0MFwiLFwic25cIjpcIkMwMlNXMVNHSDA0MFwiLFwiZXJwXCI6XCJtYXppcWlhbmc0XCIsXCJzdGF0dXNcIjpcIlwiLFwiY29kZVwiOlwiXCIsXCJ2RXJwXCI6XCJtYXppcWlhbmc0XCIsXCJpcFwiOlwiXCIsXCJ1c2VyQWdlbnRcIjpcIlwiLFwib25saW5lU3RhdHVzXCI6XCJvbmxpbmVcIixcInNzb1Rva2VuRW5jcnlwdFwiOlwiXCIsXCJ0cnVzdGVkRGV2aWNlXCI6XCIxXCIsXCJicm93c2VyRnBcIjpcIlAzUkpSNEpCNVdDNUY3T1hUSUk2RktURE1aQTI1RkpYQlVKUDQ0NFRKQ0RLUktRVENFQzdCUEZTSjRHTFlQNDZQSEJNWVQ2V1VXSjRVVks1VE5GMjJNUlJKNFwiLFwicGluXCI6XCJcIn0iLCJleHAiOjE3NDg1NzI5ODN9.vBTxaNXqOkDRsP12lJOIDVdRQX_PRqaMC6sMQVno3Qo; ssa.origin-gateway=66fd8fd459a60a025a1896a88dc48163981fbb514439dd0c90f6c5f777e72fdcce083a19f240d045e31e82b1445bb4a0c2e0875d6286e598c12af91f4f31e53b87af343abb930a803be77814261024cb066d789532882010dd38ecc565126b4af846de7e20fb99d74df4d30ab65b140c5ea17da56bc66c254c28c5cb083bf787; __jda=240971990.17483960270252013725649.1748396027.1748437578.1748483100.7; __jdc=240971990; SSAID=05562e80003da076a26eddbdde8f22f67a85670c77a9ceb44b95190d787d31ffaeff667c75fb9383e546eeacd27d678daf42932afe7657417aa70ed37870356b766af248affcea4fcfbad2347b561f26539215173b3ace9227196e0ffe6e3c1c1751c2c8bc82d1c67c98e4ffa2c33030eaae3f1951583b0faf540b467ef9e8822d155cab748c0047a222d9d183197d36bcc854307423a495f23612d91f3b8f416b5eb418d72cae412b14e720ab16d5ab15a57d3d721a939b06cbc920848fddc4; __jdb=240971990.64.17483960270252013725649|7.1748483100"
}

request_params = {
    "type": "2",
    "proposer": "maziqiang4",
    "status": "0",
    "heartBeatCheck": "0",
    "masterStr": "0,1",
    "page": "1",
    "rows": "10",
    "isNewVersion": "true",
    "version": "4"
}

response = requests.post(url, headers=headers, data=request_params, verify=False)  # verify=False 忽略SSL证书验证
json_res = response.json()
# 获取page和total，用于遍历处理
page = json_res["page"]
total = json_res["total"]

connection = pymysql.connect(host='localhost',
                             port=9030,
                             user='root',
                             password='',
                             database='sys',
                             cursorclass=pymysql.cursors.DictCursor)

rows_per_page=10
# 开始遍历
while page <= total:
    request_params['page']=str(page)
    request_params['rows']=str(rows_per_page)

    fetch_response = requests.post(url, headers=headers, data=request_params, verify=False).json()
    rows = fetch_response["rows"]
    print(f'开始获取第{page}批数据，共{total}批，每批{rows_per_page}条数据。拉取数据内容:{rows}。')

    for row in rows:
        column_names = ','.join(['`' + x + '`' for x in row])
        column_values = [row[x] for x in row]
        placeholder = ('%s,' * (len(row)))[0:-1]
        created = row['created']

        stmt = f"insert into mydb.jdq_consumer_client_info (dt,{column_names}) values(date('{created}'),{placeholder})"
        execute = connection.cursor().execute(stmt, column_values)
        print(execute)
    page += 1

    time.sleep(5)
