import vk
import time
import datetime
print('VKBot')
session = vk.Session('adb530c427ebcc74e0a33bac60a5bec85137bdfd11e89b478dcfef282349dfc48c1d7ce5550bd15ab765c')
api = vk.API(session)
messages = api.messages.get()
commands = ['Что это за программа?', 'что это за программа?', 'Как погода?', 'как погода?', 'привет', 'Привет', 'Как дела?', 'как дела?', 'Спокойной ночи', 'спокойной ночи']
messages = [(m['uid'], m['mid'] , m['body'])
            for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]
for m in messages:
    user_id = m[0]
    message_id = m[1]
    comand = m[2]
    date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S')
    if comand == 'Что это за программа?':
        api.messages.send(user_id=user_id,
                          message=date_time_string + '\n>VKBoot v0.1\n>Разработал: Калюжный Николай')
    if comand == 'что это за программа?':
        api.messages.send(user_id=user_id,
                          message=date_time_string + '\n>VKBoot v0.1\n>Разработал: Калюжный Николай')
    if comand == 'Как погода?':
        api.messages.send(user_id=user_id,
                          message=date_time_string + '\n>Погода отличная!')
    if comand == 'как погода?':
        api.messages.send(user_id=user_id,
                          message=date_time_string + '\n>Погода отличная!')
    if comand == 'привет':
        api.messages.send(user_id=user_id,
                          message=date_time_string + '\n>Здравствуй.Дети хотят конфет.')
    if comand == 'Привет':
        api.messages.send(user_id=user_id,
                          message=date_time_string + '\n>Здравствуй. Дети хотят конфет.')
    if comand == 'Как дела?':
        api.messages.send(user_id=user_id,
                          message=date_time_string + '\n>У меня всё хорошо. Ты как?')
    if comand == 'как дела?':
        api.messages.send(user_id=user_id,
                          message=date_time_string + '\n>У меня всё хорошо. Ты как?')
    if comand == 'спокойной ночи':
        api.messages.send(user_id=user_id,
                          message=date_time_string + '\n>спокойной ночи.')
    if comand == 'Спокойной ночи':
        api.messages.send(user_id=user_id,
                          message=date_time_string + '\n>спокойной ночи.')
ids = ','.join([str(m[1]) for m in messages])
if ids:
    api.messages.markAsRead(message_ids=ids)
time.sleep(3)

