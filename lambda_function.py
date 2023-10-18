from main import order_bybit

def lambda_handler(event, context):
    if 'symbol' in event and event['symbol']:
        order_return = order_bybit(event)
        return order_return
    else:
        if not event:
            print('eventに適切な要素が含まれていない。具体的には、何も含まれていない。')
            return 'eventに適切な要素が含まれていない。具体的には、何も含まれていない。'
        else:
            print(f'eventに適切な要素が含まれていない。具体的には以下のような内容になっている: {event}')
            return f'eventに適切な要素が含まれていない。具体的には以下のような内容になっている: {event}'
