import discord
import csv
import asyncio
import random 


client = discord.Client(intents=discord.Intents.all())

def read_question_from_csv(delimiter):
    with open('questions.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=delimiter)
		
        rows = [row for row in reader]  
        return random.choice(rows)  

def check_answer(answer, correct_answer):
    return answer.strip().lower() == correct_answer.strip().lower()

@client.event
async def on_message(message):
    if message.content.startswith('!ccna'):
        question = read_question_from_csv(';')
        correct_answer = question['Correct_Answer']
        answers = f"A) {question['Answer_Choice_A']}\nB) {question['Answer_Choice_B']}\nC) {question['Answer_Choice_C']}\nD) {question['Answer_Choice_D']}"
        explain = question['Explain']
        embed = discord.Embed(title="Trivia", description=question['Question'], color=0x00ff00)
        embed.add_field(name="Answer choices:", value=answers)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction("🇦")
        await msg.add_reaction("🇧")
        await msg.add_reaction("🇨")
        await msg.add_reaction("🇩")

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) in ["🇦","🇧","🇨","🇩"]
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await message.channel.send('On se réveille!!!')
        else:
            if str(reaction.emoji) == "🇦":
                user_answer = question['Answer_Choice_A']
            elif str(reaction.emoji) == "🇧":
                user_answer = question['Answer_Choice_B']
            elif str(reaction.emoji) == "🇨":
                user_answer = question['Answer_Choice_C']
            elif str(reaction.emoji) == "🇩":
                user_answer = question['Answer_Choice_D']
            if check_answer(user_answer, correct_answer):
                await message.channel.send('Correct!')
            else:
                await message.channel.send('Incorrect, the correct answer is :' + correct_answer +  explain)
                
             

    







    




client.run('MTA2MzExNzA1ODQ0OTA4ODYxNA.GCES9F.u26MpNOfcmxS-ZU2WzQNjx3j1o6_jF82sSpQnM')

