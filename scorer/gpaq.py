from typing import List
import pandas

# Declaring input table headers
GPAQ_HEADERS = [
    "Carimbo de data/hora",
    "Nome Completo",
    "Data de Nascimento",
    "P1 - O seu trabalho envolve atividade de intensidade vigorosa que leva a grandes aumentos na respiração ou batimentos cardíacos como [transportar ou levantar cargas pesadas, escavação ou construção] durante pelo menos 10 minutos de forma contínua?",
    "P2 - Em uma semana típica, em quantos dias você faz atividades de intensidade vigorosa como parte do seu trabalho? Responda o número de dias:",
    "P3 - Quanto tempo você gasta fazendo atividades de intensidade vigorosa no trabalho em um dia típico? Responda somente números em minutos, por exemplo: 1 hora e 30 minutos = 90",
    "P4  - O seu trabalho envolve atividade de intensidade moderada que leva a pequenos aumentos na respiração ou batimentos cardíacos, como caminhada rápida [ou transportar cargas leves] durante pelo menos 10 minutos de forma contínua?",
    "P5 - Em uma semana típica, em quantos dias você faz atividades de intensidade moderada como parte do seu trabalho? Responda o número de dias:",
    "P6 - Quanto tempo você gasta fazendo atividades de intensidade vigorosa no trabalho em um dia típico? Responda somente números em minutos, por exemplo: 1 hora e 30 minutos = 90",
    "P7 - Você caminha ou usa bicicleta (não elétrica) durante pelo menos 10 minutos continuamente para se deslocar entre lugares?",
    "P8 - Em uma semana típica, em quantos dias você caminha ou usa bicicleta por pelo menos 10 minutos continuamente para se deslocar entre lugares? ",
    "P9 - Quanto tempo você gasta caminhando ou andando de bicicleta para viajar em um dia típico?Responda somente números em minutos, por exemplo: 1 hora e 30 minutos = 90",
    "P10 - Você faz algum esporte, exercício ou atividade recreativa (lazer) de intensidade vigorosa que causa grande aumento na respiração ou batimentos cardíacos, como lutas, corrida, aulas coletivas durante pelo menos 10 minutos de forma contínua?",
    "P11 - Em uma semana típica, em quantos dias você pratica esportes, exercícios ou atividades recreativas (lazer) de intensidade vigorosa? ",
    "P12 - Quanto tempo você gasta praticando esportes, exercícios ou atividades recreativas de intensidade vigorosa em um dia típico? Responda somente números em minutos, por exemplo: 1 hora e 30 minutos = 90",
    "P13 - Você pratica algum esporte, exercício ou atividades recreativas (lazer) de intensidade moderada que provoca um pequeno aumento na respiração ou batimentos cardíacos, como caminhada rápida, voleibol, musculação, por pelo menos 10 minutos de forma contínua?",
    "P14 - Em uma semana típica, em quantos dias você pratica esportes, exercícios ou atividades recreativas (lazer) de intensidade moderada? ",
    "P15 - Quanto tempo você gasta praticando esportes, exercícios ou atividades recreativas (lazer) de intensidade moderada em um dia típico? Responda somente números em minutos, por exemplo: 1 hora e 30 minutos = 90",
    "P16 - Quanto tempo você costuma passar sentado ou deitado em um dia típico? Responda somente com números a quantidade de horas.",
    # "",
    # "Calculadora de Atividade Vigorosa",
    # "Calculadora de Atividade Moderada",
    # "Transporte",
    # "Calculadora total de METS",
    # "Atende a recomendação da OMS",
]

# Declaring result table headers
GPAQ_RESULT_HEADERS = [
    "Carimbo de data/hora",
    "Nome Completo",
    "Trabalho vigoroso (P1-P3)",
    "Trabalho moderado (P4-P6)",
    "Deslocamento (P7-P9)",
    "Recreação vigorosa (P10-P12)",
    "Recreação moderada (P13-P15)",
    "Sentado (P16)",
    "Calculadora de atividade vigorosa",
    "Calculadora de atividade moderada",
    "Deslocamento",
    "Calculadora total de METS",
    "Atende à recomendação da OMS",
]

def score(forms: List[List[str]]) -> pandas.core.frame.DataFrame:
    pass
    # results = []

    # for form in forms:
    #     results.append(GPAQ(form))
    
    # df = pandas.DataFrame(data=results,
    #                       columns=GPAQ_RESULT_HEADERS
    #                     )

    # return df