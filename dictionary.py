import aiohttp
from json import dumps
from .config import Config

def parse_json(jsondata):
    """a function that extracts useful data from api response

    Args:
        jsondata (josn.dumps()): a json data dump

    Returns:
        list_of_dict: returns a list of dictionary data
    """
    contents = []
    defs = jsondata['d']['Definitions']
    for f in defs:
        if f['Language'] in Config.DEF_LANGS:
            
            for d in f['WordTypeDefinitions']:
                this = {'WordType':d['WordType'],'defs':[],'Language':f['Language']}
                for defcontent in d['DefinitionContents']:
                    this['defs'].append(defcontent['Content'])
                contents.append(this)
    return contents


    
async def fetch(word):
    #base api endpint
    api_endpoint = Config.API_BASE_URL

    data = {"word": word, "fromLanguage": "Amharic", "toLanguage": "Amharic"}
    headers = {'Content-Type': 'application/json'}

    async with aiohttp.ClientSession() as session:
        async with session.post(api_endpoint,data=dumps(data),headers=headers) as response:
            return parse_json(await response.json())
