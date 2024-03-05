import asyncio
from datetime import date
import polygon


# Chave de API da Polygon.io 
API_KEY = '7I6rgRavB8o1SGT0IvVKWFQbf332zDt2'
tetse = polygon.StocksClient(API_KEY, True)



async def meu_metodo_assincrono():
    print("Iniciando meu método assíncrono")
    # Faça alguma operação assíncrona, como esperar por um certo tempo
    await tetse.get_current_price("AMD")
    print("Meu método assíncrono foi concluído")

# Executar o método assíncrono
asyncio.run(meu_metodo_assincrono())


async def main():

  client = polygon.StocksClient(API_KEY, True)



   