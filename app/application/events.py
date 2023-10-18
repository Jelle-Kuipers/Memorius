import random

def get_xenos():
    #Return all xenos in an array
    data_file_path = 'app/data/xeno_races.txt'
    with open(data_file_path, 'r') as file:
        race_list = [line.strip() for line in file.readlines()]
    return race_list

def get_xeno_purging_quotes():
    #Return all quotes in an array
    data_file_path = 'app/data/xeno_purging_quotes.txt'
    with open(data_file_path, 'r') as file:
        quote_list = [line.strip() for line in file.readlines()]
    return quote_list

def setup_application_events(client):
    #load all the application events
    print('Module: Events, has been awoken.')
    
    @client.event              
    async def on_message(message):
         #if a xenos race is mentioned in a message, send a xenos-purging quote 
        xenos = get_xenos()
        punctuation_chars = '`\/\'.,!?;:()[]{}*~_"|#@$%^&'
        words = [word.strip(punctuation_chars) for word in message.content.lower().split()]
        if message.author == client.user:
            return

        if any(word in xenos for word in words):
            purging_quotes = get_xeno_purging_quotes()
            random_number = random.randint(0,99)
            await message.channel.send(purging_quotes[random_number])