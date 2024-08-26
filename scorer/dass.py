from typing import List
import pandas

# Declaring input table headers
DASS_21_HEADERS = [
    "Carimbo de data/hora",
    "Endereço de e-mail",
    "1 - Achei difícil me acalmar",
    "2 - Senti minha boca seca",
    "3 -  Não consegui vivenciar nenhum sentimento positivo",
    "4 -  Tive dificuldade em respirar em alguns momentos (ex. respiração ofegante, falta de ar, sem ter feito nenhum esforço físico)",
    "5 -  Achei difícil ter iniciativa para fazer as coisas",
    "6 -  Tive a tendência de reagir de forma exagerada às situações",
    "7-  Senti tremores (ex. nas mãos)",
    "8-  Senti que estava sempre nervoso",
    "9-  Preocupei-me com situações em que eu pudesse entrar em pânico e parecesse ridículo (a)",
    "10-  Senti que não tinha nada a desejar",
    "11-  Senti-me agitado",
    "12-  Achei difícil relaxar",
    "13 -  Senti-me depressivo (a) e sem ânimo",
    "14-  Fui intolerante com as coisas que me impediam de continuar o que eu estava fazendo",
    "15-  Senti que ia entrar em pânico",
    "16-  Não consegui me entusiasmar com nada",
    "17-  Senti que não tinha valor como pessoa",
    "18-  Senti que estava um pouco emotivo/sensível demais",
    "19-  Sabia que meu coração estava alterado mesmo não tendo feito nenhum esforço físico (ex. aumento da frequência cardíaca, disritmia cardíaca)",
    "20-  Senti medo sem motivo",
    "21-  Senti que a vida não tinha sentido",
]

# Declaring result table headers
DASS_21_RESULT_HEADERS = [
    "Carimbo de data/hora",
    "Endereço de e-mail",
    "Classificação do sintoma - Depressão",
    "Classificação do sintoma - Ansiedade",
    "Classificação do sintoma - Estresse",
]


class Response:
    ZERO = "0 - Não se aplicou de maneira alguma"
    ONE = "1 - Aplicou-se em algum grau, ou por pouco de tempo"
    TWO = "2 - Aplicou-se em um grau considerável, ou por uma boa parte do tempo"
    THREE = "3 - Aplicou-se muito, ou na maioria do tempo"


def DASS(form: List[str]) -> List[str]:
    date = form[0]
    email = form[1]
    depression = [form[4], form[6], form[11], form[14], form[17], form[18], form[22]]
    anxiety = [form[3], form[5], form[8], form[10], form[16], form[20], form[21]]
    stress = [form[2], form[7], form[9], form[12], form[13], form[15], form[19]]

    score = [
        date,
        email,
        str(Depression(depression)),
        str(Anxiety(anxiety)),
        str(Stress(stress)),
    ]

    return score


def score(forms: List[List[str]]) -> pandas.core.frame.DataFrame:

    results = []

    for form in forms:
        results.append(DASS(form))

    df = pandas.DataFrame(data=results, columns=DASS_21_RESULT_HEADERS)

    return df


def ToScale(response: str) -> int:
    score = 0

    match response:
        case Response.ZERO:
            score = 0
        case Response.ONE:
            score = 1
        case Response.TWO:
            score = 2
        case Response.THREE:
            score = 3

    return score


def Stress(responses: List[str]) -> int:
    score = 0
    for r in responses:
        score += ToScale(r)
    return score * 2


def Depression(responses: List[str]) -> int:
    score = 0
    for r in responses:
        score += ToScale(r)
    return score * 2


def Anxiety(responses: List[str]) -> int:
    score = 0
    for r in responses:
        score += ToScale(r)
    return score * 2
