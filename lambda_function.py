import  requests
import  json
import  os
import  photocrawler
import  cryto_api
import  lxml
HEADER = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer ' + 'your line secret token'
}

def lambda_handler(event, context):

    body = json.loads(event['body'])

    for event in body['events']:

        payload = {
            'replyToken': event['replyToken'],
            'messages': []
        }
        if event['message']['type'] == 'text':
            if len(event['message']['text'])==1 and event['message']['text'][0].lower()=='j':
                
                jphotolink = photocrawler.return_url()

                payload['messages'].append({
                'type': 'image',
                'originalContentUrl': jphotolink,
                'previewImageUrl': jphotolink
                })
            else:
                input_message = event['message']['text']
                result = cryto_api.coin_price(event['message']['text'])
                if result != False:
                    price_message = "The price of {} is BTC {}/ USD {}/ HKD {}".format(input_message,result['text'],result['BTC'],result['USD'],result['HKD'])

                else:
                    price_message = "sorry, you are not entering a correct crytocurrency name"

                payload['messages'].append({
                'type': 'text',
                'text': price_message
                })
        elif event['message']['type'] == 'sticker':
            payload['messages'].append({
                'type': 'sticker',
                'stickerId': event['message']['stickerId'],
                'packageId': event['message']['packageId']
            })

        if len(payload['messages']) > 0:
            response = requests.post('https://api.line.me/v2/bot/message/reply',
                headers=HEADER,
                data=json.dumps(payload))