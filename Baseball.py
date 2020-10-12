#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:18:56 2017

Tyler's baseball sim

@author: tyler
"""

#import time
import os
import random


class Player(object):
    
    def __init__(self, name, BA, number):
        
        self.name = name
        self.BA = BA
        self.number = number
        
        self.onBase = False
        
        ## This is a list of outcomes of an at bat based on their average
        ##which will be chosen at random
        ## 0 is an out and 1 is a base hit        
        self.pList = []
        for hit in range(self.BA):
            self.pList.append(1)            
        for strikeOut in range(1000 - self.BA):
            self.pList.append(0)
        
    def getPlayerName(self):        
        return self.name
        
    def setOnBase(self):
        self.onBase = True
        
    def setOffBase(self):
        self.onBase = False
        
    def __str__(self):        
        return '<' + self.name + ' -#' + str(self.number) + '- BA:' + str(self.BA) + '>'

class Team(object):
    
    """
    Roster - a list of JUST BATTERS
    """
    
    def __init__(self, city, name, roster):
        
        self.city = city
        self.name = name
        self.roster = roster
        
        self.score = 0
        self.outs = 0
        
    def addPlayer(self, player):
        
        self.roster.append[player]

    def homeRun(self):
        self.score += 1
        
    def inningOver(self):
        self.outs = 0
        
    def getTeamName(self):
        return self.name
        
    def getNumOuts(self):
        return self.outs
        
    def addOut(self):
        print('Strike out.')
        self.outs += 1
        
    def __str__(self):
        
        print('\n----------')
        print('Batters on the ' + self.city +' '+ self.name + ':')
               
        for player in self.roster:
            
            print(player)       
        
        return 'Go ' + str(self.name) + '!' + '\n----------'
        
        
class Roster(object):
    
    def __init__(self, players):
        
        self.players = players
        
class Diamond(object):
    
    def __init__(self, name):
        self.name = name     
        
        # ▢ is empty base, ▣ is on base
        self.fBase = '▢'
        self.sBase = '▢'
        self.tBase = '▢'
        
        self.onBase = []
        
    def baseHit(self, player):
        
        print('Base hit!')

        if len(self.onBase) == 0:
            self.onBase.append(player)
            self.fBase = '▣'
            print(self.onBase[0].getPlayerName() + ' is on first!')
            
        elif len(self.onBase) == 1:
        
            self.onBase.append(self.onBase[0])
            self.onBase[0] = player
            self.sBase = '▣'
            print(self.onBase[1].getPlayerName() + ' moves to second, \n' + self.onBase[0].getPlayerName() + ' is on first.')

        elif len(self.onBase) == 2:
            
            self.onBase[2] = self.onBase[1]
            self.onBase[1] = self.onBase[0]
            self.onBase[0] = player
            self.tBase = '▣'
            print('Bases loaded! \n' + self.onBase[0].getPlayerName() + ' on first, \n' + self.onBase[1].getPlayerName() + ' on second, \n' + self.onBase[2].getPlayerName() + ' on third.')

    def inningOver(self):
        
        self.onBase = []

        self.fBase = '▢'
        self.sBase = '▢'
        self.tBase = '▢'
        
    def getDiamondName(self):
        return self.name
        
        
    def __str__(self):
        
        #print('Currently on base at '+ str(self.name)+':' )
                
        return '  ' + self.sBase + '\n' + ' / \\' + '\n' + self.tBase + '   ' + self.fBase + '\n' + ' \\ /' + '\n' + '  ▤'

def playOneGame(homeTeam, awayTeam, diamond):  
    
    def oneHalfInning(teamBatting, diamond, batter):
        
        def getNextBatter(batter): ##TODO return next available batter. 
            
            if (batter + 1) > len(teamBatting.roster):
                batter = 0
                
            else:
                batter += 1
                
            while (teamBatting.roster[batter].onBase):
                
                if (batter + 1) > len(teamBatting.roster):
                    batter = 0                
                else:
                    batter += 1
                    
            return batter
        
        while teamBatting.getNumOuts() < 3:               
        
            print('Now batting for the ' + teamBatting.getTeamName() + ': ' + teamBatting.roster[batter].getPlayerName())
            print('Number of Outs: ' + str(teamBatting.getNumOuts()))
            print(diamond)
            
            if random.choice(teamBatting.roster[batter].pList) == 1:                
                ##Add the batter to the base
                diamond.baseHit(teamBatting.roster[batter])                                
                batter = getNextBatter(batter) ##TODO need to add a check if they're on base                
            else:
                teamBatting.addOut()
                batter = getNextBatter(batter) ##TODO need to add a check if they're on base               
                
        teamBatting.inningOver()
        diamond.inningOver()
        return batter
        
    teamsPlaying = [awayTeam, homeTeam]
    batter = 0
    inning = 1.0 
        
    print('Starting a game between the ' + awayTeam.getTeamName() + ' and the ' + homeTeam.getTeamName() + ' at ' + diamond.getDiamondName())
    while(inning < 9.5):        
        batter = oneHalfInning(teamsPlaying[0], diamond, batter)
        inning += 0.5
        
def loadRoster(teamName):
    
    roster = []

    t = open(teamName, 'r')
    
    for line in t:
        player_data = line.split(',')        
        
        roster.append(Player(player_data[0], int(player_data[1]), int(player_data[2])))
        
    return roster
        
        
        
        
#JoseBautista = Player('Jose Bautista', 255, 19)
#JoshDonaldson = Player('Josh Donaldson', 279, 20)
#torontoRoster = [JoseBautista, JoshDonaldson]
#
#CoreyKluber = Player('Corey Kluber', 500, 28)
#FranciscoLindor = Player('Fancisco Lindor',308,12)
#cleavelandRoster = [CoreyKluber, FranciscoLindor]
#
#Jays = Team('Toronto', 'Blue Jays', torontoRoster)
#print(Jays)
#
#Indians = Team('Cleaveland', 'Indians', cleavelandRoster)
#print(Indians)
#
#time.sleep(3)
#
#os.system('cls')
#
#myDiamond = Diamond('the Sky Dome')
#
#playOneGame(Jays, Indians, myDiamond)

jays = loadRoster("BlueJays.txt")
Jays = Team('Toronto','Blue Jays',jays)
print(Jays)
















        

