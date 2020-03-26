from sdk.api.message import Message

api_key = "NCSGLMHSQ2FTVZUA"
api_secret = "LCSOKSWPDNLZF971PMZ4XAQPZPYD60EW"

params = dict()
params['type'] = 'sms'
params['to'] = '01082128997'
params['from'] = '01050022354'
params['text'] = '야 홍빈아 내가 내일 커피사줄께'

cool = Message(api_key, api_secret)
try:
    response = cool.send(params)
except:
    print('에러')

