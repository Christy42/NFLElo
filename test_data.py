import pandas as pd

from elo_functions import update_elo, reset, calc_odds
from enums import Teams


def run_data(data_file, elos_file, k):
    data = pd.read_pickle(data_file)
    elos = pd.read_pickle(elos_file)

    k_error = 0
    count = 0
    for i in range(len(data)):
    # for i in range(93):
        home_result = 1 if data.iloc[i]["home score"] > data.iloc[i]["away score"] else 0
        home_result = 0.5 if data.iloc[i]["home score"] == data.iloc[i]["away score"] else home_result
        away_result = 1 - home_result
        hold_elo = elos[data.iloc[i]["home team"]]
        expected = calc_odds(elos[data.iloc[i]["home team"]], elos[data.iloc[i]["away team"]])
        # print([i, data.iloc[i]["home team"], elos[data.iloc[i]["home team"]], data.iloc[i]["away team"], elos[data.iloc[i]["away team"]], expected])
        k_error += (expected - home_result) ** 2
        elos[data.iloc[i]["home team"]] = update_elo(elos[data.iloc[i]["home team"]], k, home_result,
                                                     elos[data.iloc[i]["away team"]])

        elos[data.iloc[i]["away team"]] = update_elo(elos[data.iloc[i]["away team"]], k, away_result, hold_elo)
        count += 1

    print({k: k_error / count * 100})
    for element in elos:
        # print(element, elos[element])
        pass
    pd.to_pickle(elos, elos_file)


# reset("elo.pkl")
# run_data("results.pkl", "elo.pkl", 25)


def create_data(to_store):
    data = pd.DataFrame(columns=['away team', 'home team', 'away score', 'home score'])
    data.loc[1] = [Teams.Atlanta_Falcons, Teams.Philedelphia_Eagles, 12, 18]
    data.loc[2] = [Teams.Buffalo_Bills, Teams.Baltimore_Ravens, 3, 47]
    data.loc[3] = [Teams.Jacksonville_Jaguars, Teams.New_York_Giants, 20, 15]
    data.loc[4] = [Teams.Tampa_Bay_Buccaneers, Teams.New_Orleans_Saints, 48, 40]
    data.loc[5] = [Teams.Houston_Texans, Teams.New_England_Patriots, 20, 27]
    data.loc[6] = [Teams.San_Fransisco_49ers, Teams.Minnesota_Vikings, 16, 24]
    data.loc[7] = [Teams.Tennessee_Titans, Teams.Miami_Dolphins, 20, 27]
    data.loc[8] = [Teams.Cincinnati_Bengals, Teams.Indianapolis_Colts, 34, 23]
    data.loc[9] = [Teams.Pittsburgh_Steelers, Teams.Cleveland_Browns, 21, 21]
    data.loc[10] = [Teams.Kansas_City_Chiefs, Teams.Los_Angeles_Chargers, 38, 28]
    data.loc[11] = [Teams.Seattle_Seahawks, Teams.Denver_Broncos, 24, 27]
    data.loc[12] = [Teams.Dallas_Cowboys, Teams.Carolina_Panthers, 8, 16]
    data.loc[13] = [Teams.Washington_Redskins, Teams.Arizona_Cardinals, 24, 6]
    data.loc[14] = [Teams.Chicago_Bears, Teams.Green_Bay_Packers, 23, 24]
    data.loc[15] = [Teams.New_York_Jets, Teams.Detroit_Lions, 48, 17]
    data.loc[16] = [Teams.Los_Angeles_Rams, Teams.Oakland_Raiders, 33, 13]

    data.loc[17] = [Teams.Baltimore_Ravens, Teams.Cincinnati_Bengals, 23, 34]
    data.loc[18] = [Teams.Carolina_Panthers, Teams.Atlanta_Falcons, 24, 31]
    data.loc[19] = [Teams.Indianapolis_Colts, Teams.Washington_Redskins, 21, 9]
    data.loc[20] = [Teams.Houston_Texans, Teams.Tennessee_Titans, 17, 20]
    data.loc[21] = [Teams.Philedelphia_Eagles, Teams.Tampa_Bay_Buccaneers, 21, 27]
    data.loc[22] = [Teams.Kansas_City_Chiefs, Teams.Pittsburgh_Steelers, 42, 37]
    data.loc[23] = [Teams.Miami_Dolphins, Teams.New_York_Jets, 20, 12]
    data.loc[24] = [Teams.Los_Angeles_Chargers, Teams.Buffalo_Bills, 31, 20]
    data.loc[25] = [Teams.Minnesota_Vikings, Teams.Green_Bay_Packers, 29, 29]
    data.loc[26] = [Teams.Cleveland_Browns, Teams.New_Orleans_Saints, 18, 21]
    data.loc[27] = [Teams.Detroit_Lions, Teams.San_Fransisco_49ers, 27, 30]
    data.loc[28] = [Teams.Arizona_Cardinals, Teams.Los_Angeles_Rams, 0, 34]
    data.loc[29] = [Teams.New_England_Patriots, Teams.Jacksonville_Jaguars, 20, 31]
    data.loc[30] = [Teams.Oakland_Raiders, Teams.Denver_Broncos, 19, 20]
    data.loc[31] = [Teams.New_York_Giants, Teams.Dallas_Cowboys, 13, 20]
    data.loc[32] = [Teams.Seattle_Seahawks, Teams.Chicago_Bears, 17, 24]

    data.loc[33] = [Teams.New_York_Jets, Teams.Cleveland_Browns, 17, 21]
    data.loc[34] = [Teams.New_Orleans_Saints, Teams.Atlanta_Falcons, 43, 37]
    data.loc[35] = [Teams.Green_Bay_Packers, Teams.Washington_Redskins, 17, 31]
    data.loc[36] = [Teams.Indianapolis_Colts, Teams.Philedelphia_Eagles, 16, 20]
    data.loc[37] = [Teams.Buffalo_Bills, Teams.Minnesota_Vikings, 27, 6]
    data.loc[38] = [Teams.Oakland_Raiders, Teams.Miami_Dolphins, 20, 28]
    data.loc[39] = [Teams.Denver_Broncos, Teams.Baltimore_Ravens, 14, 27]
    data.loc[40] = [Teams.Cincinnati_Bengals, Teams.Carolina_Panthers, 21, 31]
    data.loc[41] = [Teams.New_York_Giants, Teams.Houston_Texans, 27, 22]
    data.loc[42] = [Teams.Tennessee_Titans, Teams.Jacksonville_Jaguars, 9, 6]
    data.loc[43] = [Teams.San_Fransisco_49ers, Teams.Kansas_City_Chiefs, 27, 38]
    data.loc[44] = [Teams.Los_Angeles_Chargers, Teams.Los_Angeles_Rams, 23, 35]
    data.loc[45] = [Teams.Dallas_Cowboys, Teams.Seattle_Seahawks, 13, 24]
    data.loc[46] = [Teams.Chicago_Bears, Teams.Arizona_Cardinals, 16, 14]
    data.loc[47] = [Teams.New_England_Patriots, Teams.Detroit_Lions, 10, 26]
    data.loc[48] = [Teams.Pittsburgh_Steelers, Teams.Tampa_Bay_Buccaneers, 30, 27]

    data.loc[49] = [Teams.Minnesota_Vikings, Teams.Los_Angeles_Rams, 31, 38]
    data.loc[50] = [Teams.New_York_Jets, Teams.Jacksonville_Jaguars, 12, 31]
    data.loc[51] = [Teams.Miami_Dolphins, Teams.New_England_Patriots, 7, 38]
    data.loc[52] = [Teams.Philedelphia_Eagles, Teams.Tennessee_Titans, 23, 26]
    data.loc[53] = [Teams.Houston_Texans, Teams.Indianapolis_Colts, 37, 34]
    data.loc[54] = [Teams.Buffalo_Bills, Teams.Green_Bay_Packers, 0, 22]
    data.loc[55] = [Teams.Detroit_Lions, Teams.Dallas_Cowboys, 24, 26]
    data.loc[56] = [Teams.Tampa_Bay_Buccaneers, Teams.Chicago_Bears, 10, 48]
    data.loc[57] = [Teams.Cincinnati_Bengals, Teams.Atlanta_Falcons, 36, 37]
    data.loc[58] = [Teams.Seattle_Seahawks, Teams.Arizona_Cardinals, 20, 17]
    data.loc[59] = [Teams.Cleveland_Browns, Teams.Oakland_Raiders, 42, 45]
    data.loc[60] = [Teams.New_Orleans_Saints, Teams.New_York_Giants, 33, 18]
    data.loc[61] = [Teams.San_Fransisco_49ers, Teams.Los_Angeles_Chargers, 27, 29]
    data.loc[62] = [Teams.Baltimore_Ravens, Teams.Pittsburgh_Steelers, 26, 14]
    data.loc[63] = [Teams.Kansas_City_Chiefs, Teams.Denver_Broncos, 27, 23]

    data.loc[64] = [Teams.Indianapolis_Colts, Teams.New_England_Patriots, 24, 38]
    data.loc[65] = [Teams.Tennessee_Titans, Teams.Buffalo_Bills, 12, 13]
    data.loc[66] = [Teams.Atlanta_Falcons, Teams.Pittsburgh_Steelers, 17, 41]
    data.loc[67] = [Teams.Denver_Broncos, Teams.New_York_Jets, 16, 34]
    data.loc[68] = [Teams.Jacksonville_Jaguars, Teams.Kansas_City_Chiefs, 14, 30]
    data.loc[69] = [Teams.Green_Bay_Packers, Teams.Detroit_Lions, 23, 31]
    data.loc[70] = [Teams.Baltimore_Ravens, Teams.Cleveland_Browns, 9, 12]
    data.loc[71] = [Teams.New_York_Giants, Teams.Carolina_Panthers, 31, 33]
    data.loc[72] = [Teams.Miami_Dolphins, Teams.Cincinnati_Bengals, 17, 27]
    data.loc[73] = [Teams.Oakland_Raiders, Teams.Los_Angeles_Chargers, 10, 26]
    data.loc[74] = [Teams.Arizona_Cardinals, Teams.San_Fransisco_49ers, 28, 18]
    data.loc[75] = [Teams.Minnesota_Vikings, Teams.Philedelphia_Eagles, 23, 21]
    data.loc[76] = [Teams.Los_Angeles_Rams, Teams.Seattle_Seahawks, 33, 31]
    data.loc[77] = [Teams.Dallas_Cowboys, Teams.Houston_Texans, 16, 19]
    data.loc[78] = [Teams.Washington_Redskins, Teams.New_Orleans_Saints, 19, 43]

    # Week 6
    data.loc[79] = [Teams.Philedelphia_Eagles, Teams.New_York_Giants, 34, 13]
    data.loc[80] = [Teams.Tampa_Bay_Buccaneers, Teams.Atlanta_Falcons, 29, 34]
    data.loc[81] = [Teams.Carolina_Panthers, Teams.Washington_Redskins, 17, 23]
    data.loc[82] = [Teams.Seattle_Seahawks, Teams.Oakland_Raiders, 27, 3]
    data.loc[83] = [Teams.Indianapolis_Colts, Teams.New_York_Jets, 34, 42]
    data.loc[84] = [Teams.Arizona_Cardinals, Teams.Minnesota_Vikings, 17, 27]
    data.loc[85] = [Teams.Pittsburgh_Steelers, Teams.Cincinnati_Bengals, 28, 21]
    data.loc[86] = [Teams.Los_Angeles_Chargers, Teams.Cleveland_Browns, 38, 14]
    data.loc[87] = [Teams.Buffalo_Bills, Teams.Houston_Texans, 13, 20]
    data.loc[88] = [Teams.Chicago_Bears, Teams.Miami_Dolphins, 28, 31]
    data.loc[89] = [Teams.Los_Angeles_Rams, Teams.Denver_Broncos, 23, 20]
    data.loc[90] = [Teams.Baltimore_Ravens, Teams.Tennessee_Titans, 21, 0]
    data.loc[91] = [Teams.Jacksonville_Jaguars, Teams.Dallas_Cowboys, 7, 40]
    data.loc[92] = [Teams.Kansas_City_Chiefs, Teams.New_England_Patriots, 40, 43]
    data.loc[93] = [Teams.San_Fransisco_49ers, Teams.Green_Bay_Packers, 30, 33]

    # Week 7
    data.loc[94] = [Teams.Denver_Broncos, Teams.Arizona_Cardinals, 45, 10]
    data.loc[95] = [Teams.Tennessee_Titans, Teams.Los_Angeles_Chargers, 19, 20]
    data.loc[96] = [Teams.Houston_Texans, Teams.Jacksonville_Jaguars, 20, 7]
    data.loc[97] = [Teams.Carolina_Panthers, Teams.Philedelphia_Eagles, 21, 17]
    data.loc[98] = [Teams.Minnesota_Vikings, Teams.New_York_Jets, 37, 17]
    data.loc[99] = [Teams.New_England_Patriots, Teams.Chicago_Bears, 38, 31]
    data.loc[100] = [Teams.Buffalo_Bills, Teams.Indianapolis_Colts, 5, 37]
    data.loc[101] = [Teams.Cleveland_Browns, Teams.Tampa_Bay_Buccaneers, 23, 26]
    data.loc[102] = [Teams.Detroit_Lions, Teams.Miami_Dolphins, 32, 21]
    data.loc[103] = [Teams.New_Orleans_Saints, Teams.Baltimore_Ravens, 24, 23]
    data.loc[104] = [Teams.Dallas_Cowboys, Teams.Washington_Redskins, 17, 20]
    data.loc[105] = [Teams.Los_Angeles_Rams, Teams.San_Fransisco_49ers, 39, 10]
    data.loc[106] = [Teams.Cincinnati_Bengals, Teams.Kansas_City_Chiefs, 10, 45]
    data.loc[107] = [Teams.New_York_Giants, Teams.Atlanta_Falcons, 20, 23]

    # Week 8
    data.loc[108] = [Teams.Miami_Dolphins, Teams.Houston_Texans, 23, 42]
    data.loc[109] = [Teams.Philedelphia_Eagles, Teams.Jacksonville_Jaguars, 24, 18]
    data.loc[110] = [Teams.Denver_Broncos, Teams.Kansas_City_Chiefs, 23, 30]
    data.loc[111] = [Teams.Cleveland_Browns, Teams.Pittsburgh_Steelers, 18, 33]
    data.loc[112] = [Teams.Washington_Redskins, Teams.New_York_Giants, 20, 13]
    data.loc[113] = [Teams.Seattle_Seahawks, Teams.Detroit_Lions, 28, 14]
    data.loc[114] = [Teams.Tampa_Bay_Buccaneers, Teams.Cincinnati_Bengals, 34, 37]
    data.loc[115] = [Teams.New_York_Jets, Teams.Chicago_Bears, 10, 24]
    data.loc[116] = [Teams.Baltimore_Ravens, Teams.Carolina_Panthers, 21, 36]
    data.loc[117] = [Teams.Indianapolis_Colts, Teams.Oakland_Raiders, 42, 28]
    data.loc[118] = [Teams.San_Fransisco_49ers, Teams.Arizona_Cardinals, 15, 18]
    data.loc[119] = [Teams.Green_Bay_Packers, Teams.Los_Angeles_Rams, 27, 29]
    data.loc[120] = [Teams.New_Orleans_Saints, Teams.Minnesota_Vikings, 30, 20]
    data.loc[121] = [Teams.New_England_Patriots, Teams.Buffalo_Bills, 25, 6]

    # Week 9
    data.loc[122] = [Teams.Oakland_Raiders, Teams.San_Fransisco_49ers, 3, 34]
    data.loc[123] = [Teams.Chicago_Bears, Teams.Buffalo_Bills, 41, 9]
    data.loc[124] = [Teams.Tampa_Bay_Buccaneers, Teams.Carolina_Panthers, 28, 42]
    data.loc[125] = [Teams.Kansas_City_Chiefs, Teams.Cleveland_Browns, 37, 21]
    data.loc[126] = [Teams.New_York_Jets, Teams.Miami_Dolphins, 6, 13]
    data.loc[127] = [Teams.Pittsburgh_Steelers, Teams.Baltimore_Ravens, 23, 16]
    data.loc[128] = [Teams.Detroit_Lions, Teams.Minnesota_Vikings, 9, 24]
    data.loc[129] = [Teams.Atlanta_Falcons, Teams.Washington_Redskins, 38, 14]
    data.loc[130] = [Teams.Houston_Texans, Teams.Denver_Broncos, 19, 17]
    data.loc[131] = [Teams.Los_Angeles_Chargers, Teams.Seattle_Seahawks, 25, 17]
    data.loc[132] = [Teams.Los_Angeles_Rams, Teams.New_Orleans_Saints, 35, 45]
    data.loc[133] = [Teams.Green_Bay_Packers, Teams.New_England_Patriots, 17, 31]
    data.loc[134] = [Teams.Tennessee_Titans, Teams.Dallas_Cowboys, 28, 14]

    # Week 10
    data.loc[136] = [Teams.Carolina_Panthers, Teams.Pittsburgh_Steelers, 21, 52]
    data.loc[135] = [Teams.New_Orleans_Saints, Teams.Cincinnati_Bengals, 51, 14]
    data.loc[137] = [Teams.Atlanta_Falcons, Teams.Cleveland_Browns, 16, 28]
    data.loc[138] = [Teams.Detroit_Lions, Teams.Chicago_Bears, 22, 34]
    data.loc[139] = [Teams.Arizona_Cardinals, Teams.Kansas_City_Chiefs, 14, 26]
    data.loc[140] = [Teams.New_England_Patriots, Teams.Tennessee_Titans, 10, 34]
    data.loc[141] = [Teams.Washington_Redskins, Teams.Tampa_Bay_Buccaneers, 16, 3]
    data.loc[142] = [Teams.Buffalo_Bills, Teams.New_York_Jets, 41, 10]
    data.loc[143] = [Teams.Jacksonville_Jaguars, Teams.Indianapolis_Colts, 26, 29]
    data.loc[144] = [Teams.Los_Angeles_Chargers, Teams.Oakland_Raiders, 20, 6]
    data.loc[145] = [Teams.Seattle_Seahawks, Teams.Los_Angeles_Rams, 31, 36]
    data.loc[146] = [Teams.Miami_Dolphins, Teams.Green_Bay_Packers, 12, 31]
    data.loc[147] = [Teams.Dallas_Cowboys, Teams.Philedelphia_Eagles, 27, 20]
    data.loc[148] = [Teams.New_York_Giants, Teams.San_Fransisco_49ers, 27, 23]

    print(data)
    pd.to_pickle(data, to_store)


# create_data("results.pkl")
# reset_elo("elo.pkl")
