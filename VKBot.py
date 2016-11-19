import vk
import time
import datetime



print('VKBot')
session = vk.AuthSession('5698477','+79613101622','k27081997kaluzni',scope='messages')
api = vk.API(session)
lastcomand=''
date_time_string = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
while True:
    time.sleep(3)
    messages = api.messages.get()
    commands = ['Что это за программа?', 'Как погода?', 'Привет', 'спокойной ночи']
    messages = [(m['uid'], m['mid'], m['body'])
                for m in messages[1:] if m['body'] in commands and m['read_state'] == 0]
    for m in messages:
        user_id = m[0]
        message_id = m[1]
        comand = m[2]

        if lastcomand==comand :
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>Пшел na!')
            lastcomand='sdfsdfiuweyr34nvry34yrwe0hmvn7fw0yrvn3ryv930fwem'

        if comand == 'Что это за программа?':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>VKBoot v0.1\n>Разработал: Калюжный Николай')
            lastcomand=comand

        if comand == 'Как погода?':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>Погода отличная!')
            lastcomand = comand
        if comand == 'Привет':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>Здравствуй.Дети хотят конфет.')
            lastcomand = comand

        if comand == 'спокойной ночи':
            api.messages.send(user_id=user_id,
                              message=date_time_string + '\n>спокойной ночи.')
            lastcomand = comand

ids = ','.join([str(m[1]) for m in messages])
if ids:
    api.messages.markAsRead(message_ids=ids)
time.sleep(4)
