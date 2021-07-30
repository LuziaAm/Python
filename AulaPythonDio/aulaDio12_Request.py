import requests

def retorna_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    print(response.status_code)
    print(response.text)
    print(type(response.json()))
    dados_cep =response.json()
    print(dados_cep['logradouro'])
    return dados_cep

def retonar_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon
def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://globallab.org/en/#.YQNg7XVKhNg')
    print(response)
    #retorna_cep('01001000')
    #dados_pokemon = retonar_pokemon('pikachu')
    #print(dados_pokemon['sprites']['front_shiny'])