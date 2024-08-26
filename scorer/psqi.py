from typing import List
import pandas

# Declaring input table headers
PSQI_HEADERS = [
    "Carimbo de data/hora",
    "Endereço de e-mail",
    "PSQI1 - Durante o último mês, quando você geralmente foi para a cama à noite? (responda só numeros com a hora cheia. Ex: 21; 22; 23; 01)",
    "PSQI2 -   Durante o último mês, quanto tempo (em minutos) você geralmente levou para dormir à noite? (responda somente um número. Ex: 20)",
    "PSQI3 -   Durante o último mês, quando você geralmente levantou de manhã? (responda só números com a hora cheia. Ex: 05; 06; 07; 09)",
    "PSQI4 -   Durante o último mês, quantas horas de sono você teve por noite?\nPode ser diferente do número de horas que você ficou na cama. (responda só números com a hora cheia. Ex: 3; 6; 7; 10)",
    "Durante o último mês, com que freqüência você teve dificuldade de dormir porque você... [PSQI5.1 - Não conseguiu adormecer em até 30 minutos]",
    "Durante o último mês, com que freqüência você teve dificuldade de dormir porque você... [PSQI5.2 - Acordou no meio da noite ou de manhã cedo]",
    "Durante o último mês, com que freqüência você teve dificuldade de dormir porque você... [PSQI5.3 - Precisou levantar para ir ao banheiro]",
    "Durante o último mês, com que freqüência você teve dificuldade de dormir porque você... [PSQI5.4 - Não conseguiu respirar confortavelmente]",
    "Durante o último mês, com que freqüência você teve dificuldade de dormir porque você... [PSQI5.5 - Tossiu ou roncou forte]",
    "Durante o último mês, com que freqüência você teve dificuldade de dormir porque você... [PSQI5.6 - Sentiu muito frio]",
    "Durante o último mês, com que freqüência você teve dificuldade de dormir porque você... [PSQI5.7 - Sentiu muito calor]",
    "Durante o último mês, com que freqüência você teve dificuldade de dormir porque você... [PSQI5.8 - Teve sonhos ruins]",
    "Durante o último mês, com que freqüência você teve dificuldade de dormir porque você... [PSQI5.9 - Teve dor]",
    "Durante o último mês, com que freqüência você teve dificuldade de dormir porque você... [PSQI5.10 - Outra(s) razão(ões): Descreva a baixo.]",
    "Outra(s) razão(ões):",
    "PSQI6 - Durante o último mês, como você classificaria a qualidade do seu sono de uma maneira geral?",
    "PSQI7 -   Durante o último mês, com que freqüência você tomou medicamento (prescrito ou ‘‘por conta própria’’) para lhe ajudar a dormir?",
    "PSQI8 -   No último mês, com que freqüência você teve dificuldade de ficar acordado enquanto dirigia, comia ou participava de uma atividade social (festa, reunião de amigos, trabalho, estudo)?",
    "PSQI9 -   Durante o último mês, quão problemático foi para você manter o entusiasmo (ânimo) para fazer as coisas (suas atividades habituais)?",
]

# Declaring output table headers
PSQI_RESULT_HEADERS = [
    "Carimbo de data/hora",
    "Endereço de e-mail",
    "Componente 1 - Qualidade subjetiva do sono",
    "Componente 2 - Latência do sono",
    "Componente 3 - Duração do sono",
    "Componente 4 - Eficiência do sono",
    "Componente 5 - Distúrbios do sono",
    "Componente 6 - Uso de medicação para dormir",
    "Componente 7 - Sonolência e disfunção diurnas",
    "Componente 8 - Qualidade do sono - valor global",
]

def score(forms: List[List[str]]) -> pandas.core.frame.DataFrame:

    results = []

    for form in forms:
        results.append(PSQI(form))
    
    df = pandas.DataFrame(data=results, columns=PSQI_HEADERS)

    return df


def PSQI(form: List[str]) -> List[str]:
    date = form[0]
    email = form[1]
    C1 = form[17]
    C2 = [form[3], form[6]]
    C3 = form[5]
    C4 = [str(form[5]), str(form[2]), str(form[4])]  # sleep efficiency (parsing time madness)
    C5 = [
        form[7],
        form[8],
        form[9],
        form[10],
        form[11],
        form[12],
        form[13],
        form[14],
        form[15],
    ]
    C6 = form[17]
    C7 = [form[19], form[20]]

    score = [
        date,
        email,
        str(Component1(C1)),
        str(Component2(C2)),
        str(Component3(C3)),
        str(Component4(C4)),
        str(Component5(C5)),
        str(Component6(C6)),
        str(Component7(C7)),
    ]

    Component8 = Component1(C1) + Component2(C2) + Component3(C3) + Component4(C4) + Component5(C5) + Component6(C6) + Component7(C7)

    score.append(str(Component8))

    return score


def score(forms: List[List[str]]) -> pandas.core.frame.DataFrame:

    results = []

    for form in forms:
        results.append(PSQI(form))

    df = pandas.DataFrame(data=results, columns=PSQI_RESULT_HEADERS)

    return df


def Component1(response: str) -> int:
    score = 0

    match response:
        case "Muito boa":
            score = 0
        case "Boa":
            score = 1
        case "Ruim":
            score = 2
        case "Muito ruim":
            score = 3

    return score


def Component2(responses: List[str]) -> int:
    total = 0

    PSQI2 = int(responses[0])
    PSQI5a = responses[1]

    if PSQI2 <= 15:
        total += 0
    elif PSQI2 <= 30:
        total += 1
    elif PSQI2 <= 60:
        total += 2
    else:
        total += 3

    match PSQI5a:
        case "Nunca":
            total += 0
        case "Menos 1 vez/ semana":
            total += 1
        case "1 ou 2 vezes/ semana":
            total += 2
        case "3 ou mais vezes/ semana":
            total += 3

    if total == 0:
        score = 0
    elif total <= 2:
        score = 1
    elif total <= 4:
        score = 2
    else:
        score = 3

    return score


def Component3(response: str) -> int:

    PSQI4 = int(response)

    if PSQI4 > 7:
        score = 0
    elif PSQI4 >= 6:
        score = 1
    elif PSQI4 >= 5:
        score = 2
    else:
        score = 3

    return score


def Component4(responses: List[str]) -> int:
    import ctypes
    def to_c_str_array(strs: List[str]):
        ptr = (ctypes.c_char_p * (len(strs) + 1))()
        ptr[:-1] = [s.encode() for s in strs]
        ptr[-1] = None # Null terminator
        return ptr

    from pathlib import Path
    p = Path('.')
    dir = p / 'scorer' / 'scorer.so'

    lib = ctypes.CDLL(dir.resolve())
    sleep_efficiency = lib.SleepEfficiency
    sleep_efficiency.argtypes = [ctypes.POINTER(ctypes.c_char_p)]

    score = sleep_efficiency(to_c_str_array(responses))

    return score


def Component5(responses: List[str]) -> int:

    total = 0

    for r in responses:

        match r:
            case "Nenhuma no último mês":
                total += 0
            case "Menos de 1 vez/ semana":
                total += 1
            case "1 ou 2 vezes/ semana":
                total += 2
            case "3 ou mais vezes/ semana":
                total += 3

    if total == 0:
        score = 0
    elif total < 10:
        score = 1
    elif score <= 18:
        score = 2
    else:
        score = 3

    return score


def Component6(response: str) -> int:

    PSQI7 = response
    score = 0

    match PSQI7:
        case "Nenhuma no último mês":
            score = 0
        case "Menos de 1 vez/ semana":
            score = 1
        case "1 ou 2 vezes/ semana":
            score = 2
        case "3 ou mais vezes/ semana":
            score = 3

    return score


def Component7(responses: List[str]) -> int:

    total = 0

    PSQI8 = responses[0]

    match PSQI8:
        case "Nenhuma no último mês":
            total += 0
        case "Menos de 1 vez/ semana":
            total += 1
        case "1 ou 2 vezes/ semana":
            total += 2
        case "3 ou mais vezes/ semana":
            total += 3

    PSQI9 = responses[1]

    match PSQI9:
        case "Nenhuma dificuldade":
            total += 0
        case "Um problema leve":
            total += 1
        case "Um problema razoável":
            total += 2
        case "Um grande problema":
            total += 3

    if total == 0:
        score = 0
    elif total <= 2:
        score = 1
    elif score <= 4:
        score = 2
    else:
        score = 3

    return score
