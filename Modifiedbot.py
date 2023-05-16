import aiohttp
from json import dumps
from dictionary import *


async def mezgebe_kalat(text,chat_id,API_URL,BOT_TOKEN):

    response = await fetch(text)
    def construct_msg(res: list):
        msg = ""
        for r in res:
            word_type = r['WordType']
            word_lang = r['Language']
            text = f"""<b>🇪🇹 ቋንቋ {word_lang}</b>\n<b>አይነት {word_type}</b>\n-----------\n"""
            for t in r['defs']:
                text +="<code>" +t+ "</code>" + '\n'
            text += '-----------------\n'
            msg += text
        return msg
            

    
    msg = construct_msg(response) if construct_msg(response) else "ምንም ትርጉም አልተገኘም !!"
    headers = {'Content-Type': 'application/json'}
    data = dict(chat_id=chat_id, 
                                   text=msg,
                                   parse_mode="HTML",
                                   disable_web_page_preview=True)
    api_endpoint = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    async with aiohttp.ClientSession() as session:
      async with session.post(api_endpoint,data=dumps(data),headers=headers) as response:
        return await parse_json(response.json())
