#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from datetime import date


def recup_date():
    today = date.today()
    # dd/mm/YY
    date_of_today = today.strftime("%d/%m/%Y")
    return date_of_today


def get_dico_elem_json(dico, elem):
    result = {elem: dico.get(elem)}
    return result


def formule_sol(x, y, r):
    temp = x * y
    return temp * r


def formule_liq(x, y, r):
    temp = y / x
    return temp * r


def interpretation(val, seuil):
    if val > seuil:
        return "Bon"
    if val == seuil:
        return "Neutre"
    if val < seuil:
        return "Mauvais"


def inventaire_ind(a, b, e):
    indicateurs_dict = {
        "Solvabilite": {
            "1": {
                "id": 1,
                "date de calcul": recup_date(),
                "libelle": "Fonds Propres Effectifs",
                "unitIndicateur": "Aucune",
                "codeIndicateur": "FPE",
                "valeur": formule_sol(a, b, e),
            },
            "2": {
                "id": 2,
                "date de calcul": recup_date(),
                "libelle": "Total Risques Ponderes",
                "unitIndicateur": "Aucune",
                "codeIndicateur": "TRP",
                "valeur": formule_liq(e, a, b),
            },
        },
        "Liquidite": {
            "1": {
                "id": 3,
                "date de calcul": recup_date(),
                "libelle": "Net liquidity Position",
                "unitIndicateur": "Aucune",
                "codeIndicateur": "PNL",
                "valeur": formule_liq(b, a, e),
            },
            "2": {
                "id": 4,
                "date de calcul": recup_date(),
                "libelle": "Liquidity Coverage Ratio",
                "unitIndicateur": "Aucune",
                "codeIndicateur": "LCR",
                "valeur": formule_liq(b, e, a),
            },
            "3": {
                "id": 5,
                "date de calcul": recup_date(),
                "libelle": "Net Stable Funding Ratio",
                "unitIndicateur": "Aucune",
                "codeIndicateur": "NSFR",
                "valeur": formule_liq(a, e, b),
            },
        },
    }
    return indicateurs_dict
