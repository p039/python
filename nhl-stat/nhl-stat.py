#!python2.7.5
import os
import glob
import csv
import time
import math
import os, errno
import itertools
import datetime
import getopt, sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from time import gmtime, strftime


LOG_FILENAME = 'nhl_log.csv'
DELIMITER_SEMICOLON = ';'
STAT_DIRECTORY = "c:\\nhlstat"
#STAT_DIRECTORY = 'c:\\nhlstattest'


class Logger(object):
      
    def writer(self, sOut, dateOut = True):
        try:
            if dateOut:
                sOutput = strftime('%d %b %Y %H:%M:%S', gmtime()) + DELIMITER_SEMICOLON + sOut
            else:
                sOutput = sOut            

            if not os.path.isfile(LOG_FILENAME):
                f = open(LOG_FILENAME, "w")
            else:
                f = open(LOG_FILENAME, "a")

            wr = csv.writer(f, skipinitialspace=True, lineterminator='\n')
            wr.writerow([sOutput])

        except Exception, err:
                sys.stderr.write('ERROR: %s\n' % str(err))
                raise
        finally:
            f.close()


class Abbr:
    win = 'W'
    lose = 'L'


class Team(object):
    def __init__(self, name):
        self.name = name
        self.dictStat = {}


def file_remove(fileName):
    try:
        os.remove(fileName)
    except OSError, e:
        if e.errno != errno.ENOENT:
            raise


def get_stat(dir):
    try:
        L = []

        for file in os.listdir(dir):

            dates = []
            results = []

            statFileName = os.path.splitext(file)[0]
            statFileLocation = dir + '\\' + file
            strTeamName = statFileName.split('_', 1)[0]
            objTeam = Team(strTeamName)

            with open(statFileLocation, 'rb') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for (k,v) in row.items():
                        if k == 'Date':
                            dates.append(v)                   
                        if k == 'Dec':
                            results.append(v)

                for i in xrange(len(dates)):
                    dates[i] = parse_date(dates[i])

                objTeam.dictStat = dict(zip(dates, results))
                L.append(objTeam)           
        return L
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        sys.exit(1)


def parse_date(strDate):
    d = strDate.translate(None, "?.!/;:'")  
    objTime = time.strptime(d, "%b %d %y")
    return date(objTime.tm_year, objTime.tm_mon, objTime.tm_mday)


def create_regular_season(teamCombos):
    dates = []
    for obj in teamCombos:
        for k in obj.dictStat.keys():
            if k not in dates:
                dates.append(k)
    return dates


def get_names(teamCombos):
    listNames = []
    for obj in teamCombos:
        tname = ''
        objLenght = len(obj)
        for i in xrange(objLenght):
            if i == objLenght - 1:
                tname += obj[i].name
                listNames.append(tname)
            else:
                tname += obj[i].name + ','
    return listNames


def is_date_found(objTeams, date):
    if len(objTeams) == 1:
        return date in objTeams[0].dictStat
    if date in objTeams[0].dictStat:
        return True
    else:
        return is_date_found(objTeams[1:], date)


def is_winner_found(objTeams, date):
    if len(objTeams) == 1:
        if date in objTeams[0].dictStat:
            return objTeams[0].dictStat[date] == Abbr.win
    if date in objTeams[0].dictStat:
        if objTeams[0].dictStat[date] == Abbr.win:
            return True
    else:
        return is_winner_found(objTeams[1:], date)


def generator_pset(L, numTeams):
    for comb in itertools.combinations(L, numTeams):
        yield comb


def calc_combinations(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))


def cover_season(tstat, regSeason, teamsInCombo):
    try:
        pset = generator_pset(tstat, teamsInCombo)
        seasonLength = len(regSeason)
        P = []

        for c in pset:
            found = True
            while found:
                for i in xrange(seasonLength):
                    if i == (seasonLength - 1) and is_date_found(c, regSeason[i]):
                        P.append(c)
                        found = False
                    else:
                        if not is_date_found(c, regSeason[i]):
                            found = False
                            break
        return P
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        sys.exit(1)


def cover_winners(teamCombos, regSeason):
    try:
        seasonLength = len(regSeason)
        T = []

        for c in teamCombos:
            found = True
            while found:
                for i in xrange(seasonLength):
                    if i == (seasonLength - 1) and is_winner_found(c, regSeason[i]):
                        T.append(c)
                        found = False
                    else:
                        if not is_winner_found(c, regSeason[i]):
                            found = False
                            break
        return T
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        sys.exit(1)


if __name__ == '__main__':
    try:
        file_remove(LOG_FILENAME)
        log = Logger()

        log.writer('START')
        startTime = time.time()

        teamstat = get_stat(STAT_DIRECTORY)
        rseason = create_regular_season(teamstat)
        
        covseason = cover_season(teamstat, rseason, 5)
        num_combos = calc_combinations(len(teamstat), 5)

        log.writer('Number of combinations found :' + str(num_combos))
        log.writer('Total passed time net combinations: ' + str(len(covseason)))

        if len(covseason) > 0:
            for n in get_names(covseason):
                log.writer(n, False)

        covwinners = cover_winners(covseason, rseason)
        log.writer('Total always winning combinations: ' + str(len(covwinners)))

        if len(covwinners) > 0:
            for t in get_names(covwinners):
                log.writer(t, False)

        endTime = time.time() - startTime
        log.writer('STOP')
        log.writer('Function running time: ' + str(endTime) + ' seconds', False)
        

    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        sys.exit(1)
