import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/utelly/api/utelly'

mcp = FastMCP('utelly')

@mcp.tool()
def lookup(term: Annotated[Union[str, None], Field(description='name of the show you want availability - supports partial strings')] = None,
           country: Annotated[Union[str, None], Field(description='only selects services available in a specific country - supported territories uk, us, ar, at, be, br, ca, de, es, fr, ie, id, it, is, kr, my, mx, no, nl, pt, se & sg')] = None) -> dict: 
    '''Lookup a tv show or movie by name and retrieve its availability across supported services for a particular country || Netflix, Amazon Prime Video, Amazon Instant Video, Apple TV+, Google Play, iTunes, YouTube Premium, Disney Plus, Hulu, Atom Tickets, CBS, DC Universe, HBO, Discovery Channel, Fandango Movies, Fox, NBC, Nickelodeon.'''
    url = 'https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/lookup'
    headers = {'x-rapidapi-host': 'utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'term': term,
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def idlookup(source_id: Annotated[str, Field(description='')],
             source: Annotated[str, Field(description='')],
             country: Annotated[Union[str, None], Field(description='only selects services available in a specific country - supported territories uk, us, ar, at, be, br, ca, de, es, fr, ie, id, it, is, kr, my, mx, no, nl, pt, se & sg')] = None) -> dict: 
    '''Find where to watch a movie or tv show, with look-up using common IDs (IMDb, tmdb, wiki, etc). For example (The Shawshank Redemption): - **IMDb**, tt0111161 - **TMDb**, movie/278'''
    url = 'https://utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com/idlookup'
    headers = {'x-rapidapi-host': 'utelly-tv-shows-and-movies-availability-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'source_id': source_id,
        'source': source,
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
