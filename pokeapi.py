import requests

def get_poke_info(poke_name): 
    """
    Gathers information about specified pokemon

    :param poke_name: Name of Pokemon you wish to know more about
    :returns: Dictionary of Pokemon information if successful; none if unsuccessful
    """
    print("Getting Pokemon information...", end='')

    poke_name = poke_name.lower().strip()

    if poke_name is None:
        print('Error: Missing name parameter')
        return
        
    if poke_name == '':
        print('Error: Missing name parameter')
        return

    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(poke_name))

    if response.status_code == 200:
        print('Success!')
        return response.json()
    else:
        print('Error',response.status_code)
        return

   
def get_pokemon_list(limit=2000, offset=0):  
    """
    Creates a list of all pokemon
    
    :param limit: limits amount returned in list
    :param offset: selects first returned item
    :returns: List of Pokemon names
    """

    print("Getting a list of Pokemon...", end='')

    URL = 'https://pokeapi.co/api/v2/pokemon/'

    params = {
        'offset': offset,
        'limit': limit
    }

    response = requests.get(URL, params=params)

    if response.status_code == 200:
        print('Success!')
        poke_dict = response.json()
        return [p['name'] for p in poke_dict['results']]
    
    else:
        print('Failed, Response code: ', response.status_code)
        return


def get_pokemon_image_url(poke_name):
    """
    Provides URL for Pokemon's image

    :param poke_name: Name of Pokemon you wish to get image of
    :returns: URL image of Pokemon if successful; none if unsuccessful
    """
    poke_dict = get_poke_info(poke_name)

    if poke_dict:
        poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']
        return poke_url


    




