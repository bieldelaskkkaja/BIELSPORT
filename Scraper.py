import requests
from bs4 import BeautifulSoup
import pandas as pd

LEAGUES = {
    "Brasileirão Série A": "https://fbref.com/en/comps/24/stats/Brazil-Serie-A-Stats",
    "Brasileirão Série B": "https://fbref.com/en/comps/98/stats/Brazil-Serie-B-Stats",
    "Champions League": "https://fbref.com/en/comps/8/stats/Champions-League-Stats"
}

def limpar_tabela(url, table_id):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find('table', {'id': table_id})
    df = pd.read_html(str(table))[0]
    df = df[df[df.columns[0]] != df.columns[0]]
    df = df.reset_index(drop=True)
    return df

def coletar_dados(competicao):
    url = LEAGUES.get(competicao)
    if not url:
        raise ValueError("Liga não encontrada.")
    jogadores = limpar_tabela(url, 'stats_standard')
    jogadores = jogadores[['Player', 'Squad', 'Sh', 'SoT', 'Gls', 'Ast', 'CrdY', 'CrdR']]
    for col in ['Sh', 'SoT', 'Gls', 'Ast', 'CrdY', 'CrdR']:
        jogadores[col] = pd.to_numeric(jogadores[col], errors='coerce')
    times = limpar_tabela(url, 'stats_squads_standard_for')
    times = times[['Squad', 'MP', 'Gls', 'Sh', 'SoT', 'CrdY', 'CrdR']]
    for col in ['MP', 'Gls', 'Sh', 'SoT', 'CrdY', 'CrdR']:
        times[col] = pd.to_numeric(times[col], errors='coerce')
    return jogadores, times
