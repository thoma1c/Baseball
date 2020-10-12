#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:18:56 2017

Tyler's baseball Sim

A very, VERY simple version of baseball

@author: tyler
"""

#import time
#import os
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

    def addOut(self):
        newPrint('Strike out.') 
        self.outs += 1
        
    def addPoint(self):
        self.score += 1

    def homeRun(self):
        self.score += 1
        
    def inningOver(self):
        self.outs = 0
        
    def getTeamName(self):
        return self.name
        
    def getNumOuts(self):
        return self.outs
        
    def getScore(self):
        return self.score
        
    
        
    def __str__(self):
        
        newPrint('\n----------')
        newPrint('Batters on the ' + self.city +' '+ self.name + ':')
               
        for player in self.roster:
            
            newPrint(player)       
        
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
        
    def baseHit(self, team, player):
        
        newPrint('Base hit!') #TODO: review this.

        if len(self.onBase) == 0:
            self.onBase.append(team.roster[player])
            self.fBase = '▣'
            newPrint(self.onBase[0].getPlayerName() + ' is on first!')
            
        elif len(self.onBase) == 1:
        
            self.onBase.append(self.onBase[0])
            self.onBase[0] = team.roster[player]
            self.sBase = '▣'
            newPrint(self.onBase[1].getPlayerName() + ' moves to second, \n' + self.onBase[0].getPlayerName() + ' is on first.')

        elif len(self.onBase) == 2:
            
            self.onBase.append(self.onBase[1])
            self.onBase[1] = self.onBase[0]
            self.onBase[0] = team.roster[player]
            self.tBase = '▣'
            newPrint('Bases loaded! \n' + self.onBase[0].getPlayerName() + ' on first, \n' + self.onBase[1].getPlayerName() + ' on second, \n' + self.onBase[2].getPlayerName() + ' on third.')
        
        elif len(self.onBase) == 3:
            
            newPrint('RBI for ' + team.roster[player].getPlayerName() + '!')
            newPrint(self.onBase[0].getPlayerName() + 'scores.')
            self.onBase[2] = self.onBase[1]
            self.onBase[1] = self.onBase[0]
            self.onBase[0] = team.roster[player]
            newPrint('Bases loaded. \n' + self.onBase[0].getPlayerName() + ' on first, \n' + self.onBase[1].getPlayerName() + ' on second, \n' + self.onBase[2].getPlayerName() + ' on third.')
            
            team.addPoint()
            
    def inningOver(self):
        
        self.onBase = []

        self.fBase = '▢'
        self.sBase = '▢'
        self.tBase = '▢'
        
    def getDiamondName(self):
        return self.name
        
        
    def __str__(self):
        
        #print('Currently on base at '+ str(self.name)+':' )
                
        return '\n  ' + self.sBase + '\n' + ' / \\' + '\n' + self.tBase + '   ' + self.fBase + '\n' + ' \\ /' + '\n' + '  ▤'

def playOneGame(awayTeam, homeTeam, diamond):  
    
    def oneHalfInning(teamBatting, diamond, batter):
        
        def getNextBatter(batter): 
            
            if (batter + 1) > len(teamBatting.roster) - 1:
                batter = 0
                
            else:
                 batter += 1
                 return batter
                
            while (teamBatting.roster[batter].onBase):
                
                if (batter + 1) > len(teamBatting.roster):
                    batter = 0                
                else:
                    batter += 1
                    
            return batter
        
        while teamBatting.getNumOuts() < 3:               
            
            newPrint('Now batting for the ' + teamBatting.getTeamName() + ': ' + teamBatting.roster[batter].getPlayerName())
            newPrint('Number of Outs: ' + str(teamBatting.getNumOuts()))
            newPrint(diamond)
            
            if random.choice(teamBatting.roster[batter].pList) == 1:                
                ##Add the batter to the base
                diamond.baseHit(teamBatting, batter)                                
                batter = getNextBatter(batter)                 
            else:
                teamBatting.addOut()
                batter = getNextBatter(batter)                
                
        teamBatting.inningOver()
        diamond.inningOver()
        return batter
        
    teamsPlaying = [awayTeam, homeTeam]
    awayBatter = 0
    homeBatter = 0
    inning = 10 
        
    newPrint('Starting a game between the ' + awayTeam.getTeamName() + ' and the ' + homeTeam.getTeamName() + ' at ' + diamond.getDiamondName())
    
    while(inning < 95):
        if inning % 10 == 0:
            newPrint('Inning: ' + str(inning))
            awayBatter = oneHalfInning(teamsPlaying[0], diamond, awayBatter)
        else:
            newPrint('Inning: ' + str(inning))
            homeBatter = oneHalfInning(teamsPlaying[1], diamond, homeBatter)
        inning += 5
    
    if teamsPlaying[1].getScore() > teamsPlaying[0].getScore():
        
        newPrint(teamsPlaying[1].getTeamName() + ' wins in the ninth.')
        
    else:
        
        inning += 5 #TODO: something is happening here
        
        while teamsPlaying[0].getScore() > teamsPlaying[1].getScore(): 
            if inning % 10 == 0:
                newPrint('Inning: ' + str(inning))
                awayBatter = oneHalfInning(teamsPlaying[0], diamond, awayBatter)
            else:
                newPrint('Inning: ' + str(inning))
                homeBatter = oneHalfInning(teamsPlaying[1], diamond, homeBatter)
                
            inning += 5
    
        if teamsPlaying[1].getScore() > teamsPlaying[0].getScore():
            
            newPrint(teamsPlaying[1].getTeamName() + ' wins in inning ' + str(inning))
    
    ## Keep these separate
    ##____________________    
#    print('At the bottom of the ninth, the score is: ')  
#    print(teamsPlaying[0].getTeamName() + ':' + str(teamsPlaying[0].getScore()))
#    print(teamsPlaying[1].getTeamName() + ':' + str(teamsPlaying[1].getScore()))
        
def loadRoster(teamName):
    
    roster = []

    with open(teamName) as t: ## with automatically closes the file
    
        for line in t:
            player_data = line.split(',')        
            
            roster.append(Player(player_data[0], int(player_data[1]), int(player_data[2])))
            
    return roster
    
def newPrint(thing):
    
    ##Do we print?
    allow = True
    
    if allow:
        print(thing)

##Apr 6, 2016 vs. Visiting Yankees- actual scrore was 7-2 win for the Jays

BlueJays = Team('Toronto','Blue Jays',loadRoster("Teams/BlueJays.txt"))
print(BlueJays)

Yankees = Team('New York', 'Yankees', loadRoster("Teams/Yankees.txt"))
print(Yankees)

myDiamond = Diamond('the Sky Dome')

playOneGame(Yankees,BlueJays, myDiamond)

#time.sleep(3)
#
#os.system('cls')


#

















        

