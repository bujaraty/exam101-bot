import discord
import math
import random
import json

with open('config.json') as json_file:
    TOKEN = json.load(json_file)['DISCORD_TOKEN']
client = discord.Client()

random.seed(1111)
exam_info = [[123456, "6430000021", ['Q05', 'Q01', 'Q02'], ['10', '12', '50'], 3],
             [234567, "6430000121", ['Q03', 'Q05'], ['20'], 1]]
all_questions = ['TA คนไหนตอบเร็วสุด', 'ไม่ชอบวิชาไหนที่สุดในปีนี้', 'เรียนเครียดมั้ย', 'การบ้านไหนที่ชอบที่สุด', 'คนไหนตอบคุณเยอะสุด']
all_questions.sort()
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    msg = message.content
    uid2 = message.author.name + "#" + message.author.discriminator
    uid = message.author.id
    channel = author.channel
    if msg.startswith('.sign_in'):
        sign_in(uid2, msg.split()[1], exam_info)
        await client.send_message(get_welcome_and_rules_msg())
        #await channel.send(get_welcome_and_rules_msg())
        await channel.send(get_question(uid2, exam_info, all_questions))
    elif msg.startswith('.answer'):
        submit_answer(uid2, msg.split()[1], exam_info)
        await channel.send(get_question(uid2, exam_info, all_questions))

def sign_in(uid, sid, exam_info):
    # เขียนโปรแกรมในส่วนนี้
    signin = False
    for i in exam_info:
        if (i[0] == uid) or (i[1] == sid):
            signin = True
    if not (signin):
        exam_info.append([uid,sid,[],[],0])

def get_welcome_and_rules_msg():
    # เขียนโปรแกรมในส่วนนี้
    return  'สวัสดีครับนิสิต ขอให้นิสิตทำข้อสอบได้ทุกคนนะครับ\n ใครลอกได้ F กฏไปอ่านเอง ใน myCourseVille'

def get_student_info(uid, exam_info):
    # เขียนโปรแกรมในส่วนนี้
    for i in exam_info:
        if i[0] == uid:
            return i    

def get_question(uid, exam_info, all_questions):
    # เขียนโปรแกรมในส่วนนี้
    stlist = get_student_info(uid,exam_info)
    if (sorted(stlist[2]) == all_questions):
        return "end"
    elif len(stlist[3]) == stlist[4]:
        not_answered_list = []
        for e in all_questions:
            if e not in stlist[2]:
                not_answered_list.append(e)
        a = random.choice(not_answered_list)
        stlist[2].append(a)
        return uid+ ' '+ a
    else:
        return stlist[2][stlist[4]]
def submit_answer(uid, answer, exam_info):
    # เขียนโปรแกรมในส่วนนี้
    a = get_student_info(uid,exam_info)
    a[3].append(answer)
    a[4]+= 1


client.run(TOKEN)
