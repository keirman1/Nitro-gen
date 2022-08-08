import random, string, requests, threading
from discord_webhook import DiscordWebhook
f = open("Valid.txt", "w", encoding='utf-8')

#url = input("Please state your webhook\n> ")

#DiscordWebhook(url=url, content=f"```Started checking urls\nI will send any valid codes here```").execute()

web = 'https://discord.com/api/webhooks/1001416977912447046/BAfXFC9hgtmGJVXmQOioR2asR3babRWBa5HQzwVl7Nmqfis56COrPVni8uc-PwnP00gK'


def genCode():
    global web
    while True:
        code = ('').join(random.choices(string.ascii_letters + string.digits,k=24))
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:  # If the code was valid
                    # Add that code to the list of found codes
                    
            print(f"Valid Nitro Code > discord.gift/{code}")
            f.write(f"discord.gift/{code}\n")
            DiscordWebhook(url=web, content=f"https://discord.gift/{code} @everyone").execute()
        else:
            print("Invaild")
        
        

threads = []


for i in range(5):
    t = threading.Thread(target=genCode, args=())
    threads.append(t)
for i in range(5):
    threads[i].start()

for i in range(5):
    threads[i].join()
