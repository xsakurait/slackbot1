from slackbot.bot import respond_to
from slackbot.bot import listen_to

# 「respond_to」はメンションする(slackのほうで#でターゲットを指定すること,DMでやる)と応答する

#@~=デコレーター
@respond_to('こんにちは')
def greeting_1(message):
    # Slackに応答を返す
    message.reply('こんにちは!')

# 「listen_to」はメンションがなくても応答する


@listen_to('プログラミングlist')
def greeting_2(message):
    message.reply('c,java,react,Vue,html,css,javascript,python')


@listen_to('React' or 'react')
def greeting_2(message):
    message.reply('C,java,React,Vue.js,HTML,CSS,JavaScript,Python')


@listen_to('C' or 'c')
def greeting_2(message):
    message.reply('C,java,React,Vue.js,HTML,CSS,JavaScript,Python')

@listen_to('java' or 'Java')
def greeting_2(message):
    message.reply('C,java,React,Vue.js,HTML,CSS,JavaScript,Python')

@listen_to('React' or 'react' or 'React.js' or 'react.js')
def greeting_2(message):
    message.reply('C,java,React,Vue.js,HTML,CSS,JavaScript,Python')

@listen_to('Vue' or 'Vue.js' or 'vue.js' or 'vue')
def greeting_2(message):
    message.reply('C,java,React,Vue.js,HTML,CSS,JavaScript,Python')


@listen_to('js' or 'javascript' or 'JavaScript')
def greeting_2(message):
    message.reply('C,java,React,Vue.js,HTML,CSS,JavaScript,Python')

@listen_to('Python' or 'python')
def greeting_2(message):
    message.reply('C,java,React,Vue.js,HTML,CSS,JavaScript,Python')