#!/usr/bin/python3
import asyncio, cleverbotfree
from mcpi.minecraft import Minecraft
from time import sleep
# Settings
chatPollRate = 0.5
host = "localhost"
port = 4711
username = ""
escapeword = "quit"

def mcInput(entityID):
    gotInput = False
    while(not gotInput):
        sleep(chatPollRate)
        chatEvents = mc.events.pollChatPosts()
        for chatEvent in chatEvents:
            if(chatEvent.entityId == entityID):
                stringToSend = str(chatEvent.message)
                gotInput = True
    return stringToSend
async def async_chat():
    async with cleverbotfree.async_playwright() as p_w:
        c_b = await cleverbotfree.CleverbotAsync(p_w)
        while True:
            user_input = mcInput(playerid)
            if user_input == escapeword:
                break
            bot = await c_b.single_exchange(user_input)
            mc.postToChat('§f<§aCleverbot§f> §7' + bot)
        await c_b.close()

# Connect to local Minecraft server
mc = Minecraft.create(host, port)
playerid = mc.getPlayerEntityId(username)
print("Found player " + username + " (Entity " + str(playerid) + ")")
# Input
mc.postToChat("§eStarting conversation with §c" + username)
mc.postToChat("§eEscape with §2" + escapeword)
asyncio.run(async_chat())
mc.postToChat("§eClosed.")