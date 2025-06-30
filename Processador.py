def gerar_sugestoes_time(row):
    sugestoes = []
    if row["Gls"] / row["MP"] > 1.5:
        sugestoes.append("Over 1.5 gols")
    if row["CrdY"] / row["MP"] > 2:
        sugestoes.append("Over 2 cartões")
    if row["SoT"] / row["MP"] > 4:
        sugestoes.append("Time finaliza muito (Over chutes)")
    return sugestoes

def gerar_sugestoes_jogador(row):
    sugestoes = []
    if row["SoT"] > 2.5:
        sugestoes.append("Over 2.5 chutes ao gol")
    if row["Gls"] > 0.5:
        sugestoes.append("Chance de marcar")
    return sugestoes
