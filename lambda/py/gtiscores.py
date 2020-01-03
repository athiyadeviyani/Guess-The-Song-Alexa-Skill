import boto3
client = boto3.client('dynamodb')

## Returns the CustomerID for the current Session
def get_customerid(handler_input):
    return handler_input.request_envelope.session.user.user_id

## Stores the score
def store(customerid, score):
    client.put_item(TableName='gtiscores', Item={
            'customerid': { 'S': customerid },
            'score': { 'N': str(score) }
        })

## Gets the score
def get(customerid):
    result = client.query(TableName='gtiscores', Select='ALL_ATTRIBUTES', KeyConditions={
        'customerid' : {
            'AttributeValueList': [
                { 'S' : customerid }
            ],
            'ComparisonOperator': 'EQ'
        }
    })

    if len(result['Items']) == 0:
        return None

    score = result['Items']
    return score[0]['score']['N']

## Updates the high score if it's greater than the old score
def update(customerid, newscore):
    currentscore = int(get(customerid))
    if currentscore > newscore:
        return
    store(customerid, newscore)
