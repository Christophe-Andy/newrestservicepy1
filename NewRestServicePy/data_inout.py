#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import json
from fonctions import *


def file_to_dataframe(path_x, sheet_x):
    df = pd.read_excel(path_x, sheet_name=sheet_x, header=0)
    return df


def stresstest0(varmacros, df):
    result_dict = {
        "Banque": df.loc[0, "Sigle_Banque"],
        "AnneeReference": int(df.loc[0, "Annees"]),
        "ScenarioId": 2,
        " Resultat": [
            {
                "AnneeRef": int(df.loc[0, "Annees"]),
                "FPB_durs_cet1": int(df.loc[0, "FPB_durs_cet1"]),
                "FPB_additionnels_cet1": int(df.loc[0, "FPB_additionnels_cet1"]),
                "FPB_t1": int(df.loc[0, "FPB_t1"]),
                "FPT_2": int(df.loc[0, "FPT_2"]),
                "FPE": int(df.loc[0, "FPE"]),
                "T_actif": int(df.loc[0, "T_actif"]),
                "Ratio_cet1": int((df.loc[0, "FPE"] / df.loc[0, "T_actif"]) * 100),
                "Interpretation": interpretation(
                    int((df.loc[0, "FPE"] / df.loc[0, "T_actif"]) * 100), 4.5
                ),
            },
            {
                "Annee1": 2021,
                "FPB_durs_cet1": int(df.loc[0, "FPB_durs_cet1"] * varmacros[1]),
                "FPB_additionnels_cet1": int(
                    df.loc[0, "FPB_additionnels_cet1"] * varmacros[1]
                ),
                "FPB_t1": int(df.loc[0, "FPB_t1"] * varmacros[1]),
                "FPT_2": int(df.loc[0, "FPT_2"] * varmacros[1]),
                "FPE": int(df.loc[0, "FPE"] * varmacros[1]),
                "T_actif": int(df.loc[0, "T_actif"] * varmacros[1]),
                "Ratio_cet1": int(
                    ((df.loc[0, "FPE"] / df.loc[0, "T_actif"]) * 100) * varmacros[1]
                ),
                "Interpretation": interpretation(
                    int(
                        ((df.loc[0, "FPE"] / df.loc[0, "T_actif"]) * 100) * varmacros[1]
                    ),
                    4.5,
                ),
            },
            {
                "Annee2": 2022,
                "FPB_durs_cet1": int(df.loc[1, "FPB_durs_cet1"] * varmacros[2]),
                "FPB_additionnels_cet1": int(
                    df.loc[1, "FPB_additionnels_cet1"] * varmacros[2]
                ),
                "FPB_t1": int(df.loc[0, "FPB_t1"] * varmacros[2]),
                "FPT_2": int(df.loc[0, "FPT_2"] * varmacros[2]),
                "FPE": int(df.loc[0, "FPE"] * varmacros[2]),
                "T_actif": int(df.loc[0, "T_actif"] * varmacros[2]),
                "Ratio_cet1": int(
                    ((df.loc[0, "FPE"] / df.loc[0, "T_actif"]) * 100) * varmacros[2]
                ),
                "Interpretation": interpretation(
                    int(
                        ((df.loc[0, "FPE"] / df.loc[0, "T_actif"]) * 100) * varmacros[2]
                    ),
                    4.5,
                ),
            },
            {
                "Annee3": 2023,
                "FPB_durs_cet1": int(df.loc[2, "FPB_durs_cet1"] * varmacros[3]),
                "FPB_additionnels_cet1": int(
                    df.loc[2, "FPB_additionnels_cet1"] * varmacros[3]
                ),
                "FPB_t1": int(df.loc[0, "FPB_t1"] * varmacros[3]),
                "FPT_2": int(df.loc[0, "FPT_2"] * varmacros[3]),
                "FPE": int(df.loc[0, "FPE"] * varmacros[3]),
                "T_actif": int(df.loc[0, "T_actif"] * varmacros[3]),
                "Ratio_cet1": int(
                    ((df.loc[0, "FPE"] / df.loc[0, "T_actif"]) * 100) * varmacros[3]
                ),
                "Interpretation": interpretation(
                    int(
                        ((df.loc[0, "FPE"] / df.loc[0, "T_actif"]) * 100) * varmacros[3]
                    ),
                    4.5,
                ),
            },
        ],
    }
    return result_dict


def recup_json_to_dict(path):
    with open(path) as entree_json:
        entree_dict = json.load(entree_json)

    return entree_dict
