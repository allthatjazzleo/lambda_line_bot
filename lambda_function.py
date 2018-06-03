mport  requests
import  json
import  os
import  photocrawler
import  cryto_api

HEADER = {
    'Content-type': 'application/json',
    'Authorization': 'Bearer ' + 'yourowntoken'
    #change yourowntoken from your line developer platform
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
                input_message_list = [x for x in input_message.split(' ') if x!='']
                
                price_message = generate_message(input_message_list)
            
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

def generate_message(lst):
    message=''

    for i in range(len(lst)):
    
        result = cryto_api.coin_price(lst[i])
        if result != False:
            try:
                message += "The price of {} is BTC {}/ USD {}/ HKD {} ".format(lst[i],result['BTC'],result['USD'],result['HKD'])
            except:
                message += "{} is still in pre ICO stage ".format(lst[i])
                    
        else:
            message += "Sorry your entry is invalid! "
    return message        
   
        
