import yfinance as yf
import datetime
import matplotlib.pyplot as plt
import discord
from discord.ext import commands
from dateutil.relativedelta import relativedelta
import random
import os
from dotenv import load_dotenv
from lists import compy, colors, periods

bot = commands.Bot(command_prefix="$")
client = discord.Client()


@client.event
async def on_ready():
    print(f"We logged in as {client.user}")


def company_period(company, period):
    i = 0
    for com in company:
        col = random.choice(['red', 'black', 'blue', 'green', 'purple'])
        historical_data = yf.download(com, progress=False, period=period)
        plt.plot(historical_data['Close'], color=col, label=com)
        plt.xlabel('Datetime')
        plt.ylabel('closing price')
        plt.legend()
        i = i + 1
    plt.gcf().autofmt_xdate()
    plt.savefig('image.png')
    chart = discord.File('image.png', filename='image.png')
    plt.close()
    return chart


def p(company, start, end):
    yy_start, mm_start, dd_start = str(start).split('-')
    yy_end, mm_end, dd_end = str(end).split('-')
    i = 0
    nt = []
    for com in company:
        col = random.choice(colors)

        start1 = datetime.datetime(int(yy_start), int(mm_start), int(dd_start))
        end1 = datetime.datetime(int(yy_end), int(mm_end), int(dd_end))
        historical_data = yf.download(com, start=start1, end=end1, progress=False)
        plt.plot(historical_data['Close'], color=col, label=com)
        plt.xlabel('Datetime')
        plt.ylabel('closing price')
        plt.legend()
        i = i + 1
        colors.remove(col)

    plt.gcf().autofmt_xdate()
    plt.savefig('image.png')
    chart = discord.File('image.png', filename='image.png')
    plt.close()
    return chart


@client.event
async def on_message(message):
    ppp = False
    msg = message.content
    com = []
    list_msg = msg.split(' ')
    end = datetime.date.today()
    start = datetime.date.today() - relativedelta(year=datetime.date.today().year - 1)
    per = '3d'
    is_company = False
    if client.user == message.author:
        return
    elif msg.startswith("stock"):
        await message.channel.send("""Type in  either of these formats for more info:
    - period   company_codes
    - start_date  end_date  company codes
    - year  company codes""")

    else:

        for word in list_msg:
            if word == '\0':
                break
            elif word in compy:
                com.append(word)
                is_company = True
            elif word[len(word) - 2:] in periods:
                per = word
                ppp = True
                if word[len(word) - 2:] == "yr":
                    ppp = False
                    end = datetime.date.today()
                    start = datetime.date.today() - relativedelta(year=datetime.date.today().year - int(word[:-2]))
            elif word[-1:] in periods:
                per = word
                ppp = True
            elif len(word) >= 6:
                start = list_msg[0]

                end = list_msg[1]

        if not is_company:
            await message.channel.send("ENTER A VALID COMPANY CODE")

    if ppp:
        await message.channel.send(file=company_period(com, per))
    elif not ppp and is_company:
        await message.channel.send(file=p(com, start, end))


load_dotenv()
TOKEN = os.getenv("token_key")

client.run(TOKEN)
"""from datetime import datetime
 
my_string = str(input('Enter date(yyyy-mm-dd): '))
my_date = datetime.strptime(my_string, "%Y-%m-%d")
 
print(my_date) date validation after completing the project"""

"""plt.plot(apple_df.head(65)['Open'], label='Open_price')
plt.plot(apple_df.head(65)['High'], label='High_price')
plt.plot(apple_df.head(65)['Low'], label='Low_price')
plt.plot(apple_df.head(65)['Close'], label='Close_price')
plt.title('Microsoft stock prices')
plt.xlabel('Datetime')
plt.ylabel('value')
plt.legend()"""

"""plt.savefig('image.png')
chart1 = discord.File("image.png", filename="image.png")
charts.append(chart1)

plt.close()
plt.cla()
plt.clf()
plt.plot(apple_df.head(65)['Close'])
plt.title('Microsoft stock prices')
plt.ylabel('closing price')
plt.xlabel('Datetime')
plt.savefig('image1.png')

chart2 = discord.File("image1.png", filename="image1.png")
charts.append(chart2)
plt.close()"""
"""@client.event
async def on_message(message):
    if client.user == message.author:
        return
    if not message.content.startswith('MSFT'):
        for chart in charts:
            await message.channel.send(file=chart)
    if not message.content.startswith('msft'):
        for chart in charts:
            await message.channel.send(file=chart)

"""
'''Type in this either of these formats for more info:
    1.period company_code or company_codes(period<1year)
    2.2/3/2020 3/3/2022 company_code or company codes
    3.year company_code or company codes'''
'''if msg=="1"
if list_msg has[“1d”, “5d”, “1mo”, “3mo”, “6mo”, “1y”, “2y”, “5y”, “10y”, “ytd”, “max”]
list_msg has compy
'''
# get historical market data
# hist = msft.history(period="max")
