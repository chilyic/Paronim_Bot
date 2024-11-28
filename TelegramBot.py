# pip install aiogram=="2.25.1"
from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup 
import random

#bot = Bot(token='5631699730:AAH0LLLo-C9d-WaOa_HgVjQHYhUvtVME9Wg')
bot = Bot(token='7778561726:AAE2IpeSc2clhpqDfCk-x-e9LosjsoPcJBI')
dp = Dispatcher(bot)

file = open('Paronims.txt', encoding='utf-8', mode='r')
content = file.readlines()

questions = []
buttons1 = []
buttons2 = []
buttons3 = []
temp = ''
for words in content[0]:    
    if words == '\n':
        questions = temp.split(', ')
        temp = ''        
    else:
        temp += words    
        

for words in content[1]:    
    if words == '\n':
        buttons1 = temp.split(', ')
        temp = ''        
    else:
        temp += words  
        

for words in content[2]:    
    if words == '\n':
        buttons2 = temp.split(', ')
        temp = ''        
    else:
        temp += words

for words in content[3]:    
    if words == '\n':
        buttons3 = temp.split(', ')
        temp = ''        
    else:
        temp += words

print(questions)
print(buttons1)
print(buttons2)
print(buttons3)

index = 0
question = questions[0]
button1 = buttons1[0]
button2 = buttons2[0]
button3 = buttons3[0]

keyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buts = [button1, button2, button3]
random.shuffle(buts)
print(buts)
keyboard_reply.add(buts[0], buts[1], buts[2])

@dp.message_handler(commands=['start'])
async def check(message: types.Message):
    index = 0
    question = questions[0]
    button1 = buttons1[0]
    button2 = buttons2[0]
    await message.reply(question, reply_markup=keyboard_reply)

@dp.message_handler() 
async def check_rp(message: types.Message): 
    global index
    global question
    global button1
    global button2
    global button3

    print(message.text)
    
    if message.text == button1:         
        await message.reply("Правильно!") 
        if index < len(questions) - 1:
            index += 1
            question = questions[index]
            button1 = buttons1[index]
            button2 = buttons2[index]
            button3 = buttons3[index]

            keyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            buts = [button1, button2, button3]
            random.shuffle(buts)
            keyboard_reply.add(buts[0], buts[1], buts[2])

            await message.reply(question, reply_markup=keyboard_reply) 
        else:
            await message.reply("Yo, goodbay! Y R great!")
            
    elif message.text == button2 or message.text == button3:
        await message.reply("Неправильно") 
        index = 0
        question = questions[index]
        button1 = buttons1[index]
        button2 = buttons2[index]
        button3 = buttons3[index]

        keyboard_reply = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        buts = [button1, button2, button3]
        random.shuffle(buts)
        keyboard_reply.add(buts[0], buts[1], buts[2])

        await message.reply(question, reply_markup=keyboard_reply) 

    else: 
        # Responding with a message that includes the text of the user's message 
        await message.reply(f"Your message is: {message.text}") 

executor.start_polling(dp)