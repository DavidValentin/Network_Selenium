import re
import json

# Existe un substring llamado postData

string_post_data = '''
content-length: 6108
sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
sec-ch-ua-mobile: ?0
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
viewport-width: 1536
content-type: application/x-www-form-urlencoded
x-fb-lsd: lW0Lm9UWMpNTcIRu_O-EA_
x-fb-friendly-name: CometMarketplaceSearchContentPaginationQuery
sec-ch-prefers-color-scheme: light
sec-ch-ua-platform: "Windows"
accept: */*
origin: https://www.facebook.com
sec-fetch-site: same-origin
sec-fetch-mode: cors
sec-fetch-dest: empty
referer: https://www.facebook.com/marketplace/category/exercise-fitness
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
cookie: sb=BjNtY4n86bsabo_bMCCUs2DK; wd=1536x700; dpr=1.25; datr=BjNtYzOM-Kw84sSSu-t7EZVn; c_user=100086515548463; xs=41%3ADhc6BafjaI5NmQ%3A2%3A1668100877%3A-1%3A-1; fr=0mBu5LlhmIZ9aqxCl.AWUxJJ7tOJQq8XZZqrwwODNP37o.BjbTMG.k6.AAA.0.0.BjbTMN.AWV13pQHFlc; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1668100911288%2C%22v%22%3A1%7D
'''
# Existe un substring llamado path":"/api/graphql/
# string_path = '''
# {'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[{"blockedReasons":[],"cookie":{"domain":".facebook.com","expires":1702082768.757496,"httpOnly":true,"name":"sb","path":"/","priority":"Medium","sameParty":false,"sameSite":"None","secure":true,"session":false,"size":26,"sourcePort":443,"sourceScheme":"Secure","value":"x2BkYz6yiYwElxuR_Qo5V9zH"}},{"blockedReasons":[],"cookie":{"domain":".facebook.com","expires":1702082760.072253,"httpOnly":true,"name":"datr","path":"/","priority":"Medium","sameParty":false,"sameSite":"None","secure":true,"session":false,"size":28,"sourcePort":443,"sourceScheme":"Secure","value":"x2BkY6w6RCxC6YH_ysWe03fi"}},{"blockedReasons":[],"cookie":{"domain":".facebook.com","expires":1668127579,"httpOnly":false,"name":"wd","path":"/","priority":"Medium","sameParty":false,"sameSite":"Lax","secure":true,"session":false,"size":10,"sourcePort":443,"sourceScheme":"Secure","value":"1536x700"}},{"blockedReasons":[],"cookie":{"domain":".facebook.com","expires":1668127579,"httpOnly":false,"name":"dpr","path":"/","priority":"Medium","sameParty":false,"sameSite":"None","secure":true,"session":false,"size":7,"sourcePort":443,"sourceScheme":"Secure","value":"1.25"}},{"blockedReasons":[],"cookie":{"domain":".facebook.com","expires":1699058765.757589,"httpOnly":false,"name":"c_user","path":"/","priority":"Medium","sameParty":false,"sameSite":"None","secure":true,"session":false,"size":21,"sourcePort":443,"sourceScheme":"Secure","value":"100086515548463"}},{"blockedReasons":[],"cookie":{"domain":".facebook.com","expires":1699058765.757631,"httpOnly":true,"name":"xs","path":"/","priority":"Medium","sameParty":false,"sameSite":"None","secure":true,"session":false,"size":48,"sourcePort":443,"sourceScheme":"Secure","value":"30%3AZozTiljYdCOHEw%3A2%3A1667522765%3A-1%3A-1"}},{"blockedReasons":[],"cookie":{"domain":".facebook.com","expires":1675298762.757672,"httpOnly":true,"name":"fr","path":"/","priority":"Medium","sameParty":false,"sameSite":"None","secure":true,"session":false,"size":84,"sourcePort":443,"sourceScheme":"Secure","value":"0Z7kMVkF562RbXG7p.AWVToFJxyTvnvSxJQojBG2bvexs.BjZGDH.fz.AAA.0.0.BjZGDN.AWWeZ9lHbqo"}},{"blockedReasons":[],"cookie":{"domain":".facebook.com","expires":-1,"httpOnly":false,"name":"presence","path":"/","priority":"Medium","sameParty":false,"secure":true,"session":true,"size":75,"sourcePort":443,"sourceScheme":"Secure","value":"C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1667522785087%2C%22v%22%3A1%7D"}}],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":289925.579235},"headers":{":authority":"www.facebook.com",":method":"POST",":path":"/ajax/webstorage/process_keys/?state=0",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br","accept-language":"en-US,en;q=0.9","content-length":"1014","content-type":"application/x-www-form-urlencoded","cookie":"sb=x2BkYz6yiYwElxuR_Qo5V9zH; datr=x2BkY6w6RCxC6YH_ysWe03fi; wd=1536x700; dpr=1.25; c_user=100086515548463; xs=30%3AZozTiljYdCOHEw%3A2%3A1667522765%3A-1%3A-1; fr=0Z7kMVkF562RbXG7p.AWVToFJxyTvnvSxJQojBG2bvexs.BjZGDH.fz.AAA.0.0.BjZGDN.AWWeZ9lHbqo; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1667522785087%2C%22v%22%3A1%7D","origin":"https://www.facebook.com","referer":"https://www.facebook.com/marketplace/category/exercise-fitness","sec-ch-prefers-color-scheme":"light","sec-ch-ua":"\\"Google Chrome\\";v=\\"107\\", \\"Chromium\\";v=\\"107\\", \\"Not=A?Brand\\";v=\\"24\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Windows\\"","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"same-origin","user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","viewport-width":"1536","x-fb-lsd":"yNPDp5vl6k3IU3N3OK59_H"},"requestId":"16764.464"}},"webview":"3C676F545F8821E5E3F6095008144DF8"}', 'timestamp': 1667522790180}
# '''

cookie = re.findall('cookie: ([^\n]*)', string_post_data)
xfblsd = re.findall('x-fb-lsd: ([^\n]*)', string_post_data)
referer = re.findall('referer: ([^\n]*)', string_post_data)

data = {'cookie': cookie, 'xfblsd': xfblsd, 'referer': referer}

with open('data.json', 'w') as fp:
    json.dump(data, fp)

with open('data.json', 'r') as fp:
    data = json.load(fp)


cookie2 = 'cookie2'
xfblsd2 = 'xfblsd2'
referer2 = 'referer2'

data = {'cookie': cookie2, 'xfblsd': xfblsd2, 'referer': referer2}

with open('data.json', 'w') as fp:
    json.dump(data, fp)

with open('data.json', 'r') as fp:
    data = json.load(fp)


print(data)
print(type(data))

print(type(xfblsd))
