# Memorius - About
Ludicarum Bellorum Memorius is a warhammer 40,000 themed discord bot written in Python3 using the [discord.py](https://discordpy.readthedocs.io/en/stable/index.html) library.

It exists only to serve and aid in the planning of our next date of wargaming or DnD. <br>
The bot is heavily stylized after warhammer 40,000 and it's name is a rough High-Gothic translation of "reminder of wargames" (as by ChatGPT)

## Features

Currently Memorius only contains 2 simple application commands, and a singular [task inside a cog](https://discordpy.readthedocs.io/en/stable/ext/tasks/index.html)

#### ```/hello```
Returns a greeting.

#### ```/ping```
Returns a bit of flavoured text with the current ping in MS.

#### Notify
Checks every hour if it is "notify time".
Once its notify time, the bot sends out a message pinging a role, asking them for their availability for the coming weekend.
Is automatically started once the bot goes live.

You can specify the date and time in the ***.ENV*** file!

## Running

Memorius can ran locally aslong as you have python3.10 and the requirements as listen in requirements.txt <br>

Memorius is also Dockerized! just pull the repository, configure a **.ENV** and run ```docker compose up -d``` !