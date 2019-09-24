import math
import pandas as pd
from enums import Teams


def update_elo(elo, k, result, opp_elo):
    return round(elo + k * (result - calc_odds(elo, opp_elo)))


def calc_odds(odds_a, odds_b):
    return 1 / (1 + math.pow(10, (odds_b - odds_a) / 400))


def reset_elo(file):
    elo_data = pd.DataFrame(columns=["team", "elo"])
    elo_data.loc[1] = [Teams.Arizona_Cardinals, 1500]
    elo_data.loc[2] = [Teams.Atlanta_Falcons, 1500]
    elo_data.loc[3] = [Teams.Baltimore_Ravens, 1500]
    elo_data.loc[4] = [Teams.Buffalo_Bills, 1500]
    elo_data.loc[5] = [Teams.Carolina_Panthers, 1500]
    elo_data.loc[6] = [Teams.Chicago_Bears, 1500]
    elo_data.loc[7] = [Teams.Cincinnati_Bengals, 1500]
    elo_data.loc[8] = [Teams.Cleveland_Browns, 1500]
    elo_data.loc[9] = [Teams.Dallas_Cowboys, 1500]
    elo_data.loc[10] = [Teams.Denver_Broncos, 1500]
    elo_data.loc[11] = [Teams.Detroit_Lions, 1500]
    elo_data.loc[12] = [Teams.Green_Bay_Packers, 1500]
    elo_data.loc[13] = [Teams.Houston_Texans, 1500]
    elo_data.loc[14] = [Teams.Indianapolis_Colts, 1500]
    elo_data.loc[15] = [Teams.Jacksonville_Jaguars, 1500]
    elo_data.loc[16] = [Teams.Kansas_City_Chiefs, 1500]
    elo_data.loc[17] = [Teams.Los_Angeles_Chargers, 1500]
    elo_data.loc[18] = [Teams.Los_Angeles_Rams, 1500]
    elo_data.loc[19] = [Teams.Miami_Dolphins, 1500]
    elo_data.loc[20] = [Teams.Minnesota_Vikings, 1500]
    elo_data.loc[21] = [Teams.New_England_Patriots, 1500]
    elo_data.loc[22] = [Teams.New_Orleans_Saints, 1500]
    elo_data.loc[23] = [Teams.New_York_Giants, 1500]
    elo_data.loc[24] = [Teams.New_York_Jets, 1500]
    elo_data.loc[25] = [Teams.Oakland_Raiders, 1500]
    elo_data.loc[26] = [Teams.Philedelphia_Eagles, 1500]
    elo_data.loc[27] = [Teams.Pittsburgh_Steelers, 1500]
    elo_data.loc[28] = [Teams.San_Fransisco_49ers, 1500]
    elo_data.loc[29] = [Teams.Seattle_Seahawks, 1500]
    elo_data.loc[30] = [Teams.Tampa_Bay_Buccaneers, 1500]
    elo_data.loc[31] = [Teams.Tennessee_Titans, 1500]
    elo_data.loc[32] = [Teams.Washington_Redskins, 1500]
    print(elo_data)
    pd.to_pickle(elo_data, file)


def reset(file):
    b = {Teams.Arizona_Cardinals: 1500,
     Teams.Atlanta_Falcons: 1500,
     Teams.Baltimore_Ravens: 1500,
     Teams.Buffalo_Bills: 1500,
    Teams.Carolina_Panthers: 1500,
    Teams.Chicago_Bears: 1500,
    Teams.Cincinnati_Bengals: 1500,
    Teams.Cleveland_Browns: 1500,
    Teams.Dallas_Cowboys: 1500,
    Teams.Denver_Broncos: 1500,
    Teams.Detroit_Lions: 1500,
    Teams.Green_Bay_Packers: 1500,
    Teams.Houston_Texans: 1500,
    Teams.Indianapolis_Colts: 1500,
    Teams.Jacksonville_Jaguars: 1500,
    Teams.Kansas_City_Chiefs: 1500,
    Teams.Los_Angeles_Chargers: 1500,
    Teams.Los_Angeles_Rams: 1500,
    Teams.Miami_Dolphins: 1500,
    Teams.Minnesota_Vikings: 1500,
    Teams.New_England_Patriots: 1500,
    Teams.New_Orleans_Saints: 1500,
    Teams.New_York_Giants: 1500,
    Teams.New_York_Jets: 1500,
    Teams.Oakland_Raiders: 1500,
    Teams.Philedelphia_Eagles: 1500,
    Teams.Pittsburgh_Steelers: 1500,
    Teams.San_Fransisco_49ers: 1500,
    Teams.Seattle_Seahawks: 1500,
    Teams.Tampa_Bay_Buccaneers: 1500,
    Teams.Tennessee_Titans: 1500,
    Teams.Washington_Redskins: 1500}
    pd.to_pickle(b, file)


reset("elo.pkl")
