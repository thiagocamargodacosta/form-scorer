from typing import List
import pandas

# Declaring input table headers
PANAS_HEADERS = [
    "Carimbo de data/hora",
    "Nome Completo",
    "Data de Nascimento",
    " [Interessado]",
    " [Perturbado]",
    " [Excitado]",
    " [Atormentado]",
    " [Agradavelmente surpreendido]",
    " [Culpado]",
    " [Assustado]",
    " [Caloroso]",
    " [Repulsa]",
    " [Entusiasmado]",
    " [ Orgulhoso]",
    " [ Irritado]",
    " [Encantado]",
    " [Remorsos]",
    " [Inspirado]",
    " [Nervoso]",
    " [Determinado]",
    " [Trémulo]",
    " [Ativo]",
    " [Amedrontado]",
]

# Declaring result table headers
PANAS_RESULT_HEADERS = [
    "Carimbo de data/hora",
    "Nome Completo",
    "Pontuação de afeto positivo",
    "Pontuação de afeto negativo",
]

class Response:
    ONE   = 1 # Very slighty or not at all
    TWO   = 2 # A little
    THREE = 3 # Moderately
    FOUR  = 4 # Quite a bit
    FIVE  = 5 # Extremely

def PANAS(form: List[str]) -> List[str]:

    date = form[0]
    name = form[1]

    # Splitting response items into positive and negative
    # form[3] == item one
    positive_items = [
        form[3], form[5], form[7], form[11], form[12],
        form[14], form[16], form[18], form[19], form[21]
    ]

    negative_items = [
        form[4], form[6], form[8], form[9], form[10],
        form[13], form[15], form[17], form[20], form[22]
    ]

    score = [
        date,
        name,
        str(positive_affect_score(positive_items)),
        str(negative_affect_score(negative_items)),
    ]

    return score

def positive_affect_score(responses: List[int]) -> int:
    score = 0

    for r in responses:
        score += to_scale(r)
    
    return score

def negative_affect_score(responses: List[int]) -> int:
    score = 0

    for r in responses:
        score += to_scale(r)
    
    return score

def score(forms: List[List[str]]) -> pandas.core.frame.DataFrame:

    results = []

    for form in forms:
        results.append(PANAS(form))
    
    df = pandas.DataFrame(data=results,
                          columns=PANAS_RESULT_HEADERS
                        )

    return df

def to_scale(response: str) -> int:
    score = 0

    match response:
        case Response.ONE:
            score = 1
        case Response.TWO:
            score = 2
        case Response.THREE:
            score = 3
        case Response.FOUR:
            score = 4
        case Response.FIVE:
            score = 5
    
    return score