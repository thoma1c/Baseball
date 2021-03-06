#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 21:18:56 2017

Tyler's baseball Sim

A very, VERY simple version of baseball

@author: tyler

Ran this for Jays vs Mariners, May 14
Mariners Favoured roughly 63%
Actual result, Jays win 3-2, walkoff in the ninth

"""

#import time
#import os
import random
import pylab
import numpy as np


class Player(object):
    
    def __init__(self, name, BA, number):
        
        self.name = name
        self.BA = BA
        self.number = number
        
        self.onBase = False
            
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
    Roster - a list of JUST BATTERS, no other positions
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

    def homeRun(self): # For this simulation this isn't necessary
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
        self.fBase = '▢' #First base
        self.sBase = '▢' #Second base, etc
        self.tBase = '▢'
        
        self.onBase = []
        
    def baseHit(self, team, player):
        
        newPrint('Base hit!') 

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

    def gameWon(winningTeamName, awayTeam, homeTeam, inning):
        
        newPrint(' \n --------------- \n')
        newPrint(winningTeamName + ' win in inning ' + str(inning) + '! \n')
        newPrint('Score: \n' + awayTeam.getTeamName() + ': ' + str(awayTeam.getScore()))
        newPrint(homeTeam.getTeamName() + ': ' + str(homeTeam.getScore()))
        
        diamond.inningOver()
        awayTeam.inningOver()
        awayTeam.score = 0
        
        homeTeam.inningOver()
        homeTeam.score = 0
        
        return winningTeamName
        
  
    def oneHalfInning(teamBatting, diamond, batter, walkoff=False):
        
        """
        Teambatting is the home or away team
        diamond is the diamond
        batter is an int of the current batter in the roster 
        walkoff is for if we're in the bottom of 9+ inning and the home team breaks a tie or pulls ahead
        """
         
        while teamBatting.getNumOuts() < 3:               
            
            newPrint('Now batting for the ' + teamBatting.getTeamName() + ': ' + teamBatting.roster[batter].getPlayerName())
            newPrint('Number of Outs: ' + str(teamBatting.getNumOuts()))
            newPrint(diamond)
            
            if random.randint(0,1000) < teamBatting.roster[batter].BA:              
                ##Add the batter to the base
                diamond.baseHit(teamBatting, batter)                                
                
                if batter +1 > len(teamBatting.roster) - 1:
                    batter = 0
                else:
                    batter += 1
                
            else:
                teamBatting.addOut()
                if batter +1 > len(teamBatting.roster) - 1:
                    batter = 0
                else:
                    batter += 1           
                
        teamBatting.inningOver()
        diamond.inningOver()
        return batter
        
    #Start game loop for innings 1 - 9.5    
        
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
        
    # If home team is winning, there is no bottom of the ninth
    
    newPrint('Score: \n' + teamsPlaying[0].getTeamName() + ': ' + str(teamsPlaying[0].getScore()) )
    newPrint(teamsPlaying[1].getTeamName() + ': ' + str(teamsPlaying[1].getScore()))
    
    if teamsPlaying[1].getScore() > teamsPlaying[0].getScore():
        
        return gameWon(teamsPlaying[1].getTeamName(), teamsPlaying[0], teamsPlaying[1], inning)
        
    else:      
        
        #Home team has a lesser score in the bottom of the 9th
             
        while teamsPlaying[0].getScore() >= teamsPlaying[1].getScore(): 
            
            if inning == 100:
                newPrint('Overtime! Extra innings.')
            
            if inning % 10 == 0: # Top of the inning
                newPrint('Inning: ' + str(inning))
                awayBatter = oneHalfInning(teamsPlaying[0], diamond, awayBatter)
                
                newPrint('Score: \n' + teamsPlaying[0].getTeamName() + ': ' + str(teamsPlaying[0].getScore()) + ' , ' + teamsPlaying[1].getTeamName() + ': ' + str(teamsPlaying[1].getScore()) )
                                
                inning += 5
                
            else: # Bottom of the inning
                newPrint('Inning: ' + str(inning))
                homeBatter = oneHalfInning(teamsPlaying[1], diamond, homeBatter)
                
                newPrint('Score: \n' + teamsPlaying[0].getTeamName() + ': ' + str(teamsPlaying[0].getScore()) + ' , ' + teamsPlaying[1].getTeamName() + ': ' + str(teamsPlaying[1].getScore()) )
                               
                if teamsPlaying[1].getScore() > teamsPlaying[0].getScore():
                    
                    #TODO Need to account for the walkoff win
            
                    return gameWon(teamsPlaying[1].getTeamName(), teamsPlaying[0], teamsPlaying[1], inning)
                    
                elif teamsPlaying[0].getScore() > teamsPlaying[1].getScore():
                    return gameWon(teamsPlaying[0].getTeamName(), teamsPlaying[0], teamsPlaying[1], inning)
                
                else: 
                        
                    inning += 5
    
        return gameWon(teamsPlaying[1].getTeamName(), teamsPlaying[0], teamsPlaying[1], inning)
#            
#            newPrint(teamsPlaying[1].getTeamName() + ' wins in inning ' + str(inning))
    
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
    allow = False
    
    if allow:
        print(thing)
##Apr 6, 2016 vs. Visiting Yankees- actual scrore was 7-2 win for the Jays

BlueJays = Team('Toronto','Blue Jays',loadRoster("Teams/BlueJays_May_14.txt"))
print(BlueJays)

Mariners = Team('Seattle', 'Mariners', loadRoster("Teams/Mariners_May_14.txt"))
print(Mariners)

numGames = 1000
winners = []


myDiamond = Diamond('the Sky Dome')
#playOneGame(Mariners,BlueJays, myDiamond)


for game in range(numGames):

    myDiamond = Diamond('the Sky Dome') #TODO: this is in here because the diamond might not reset
    if playOneGame(Mariners,BlueJays, myDiamond) == 'Mariners':

        winners.append(0)
        
    else:
        
        winners.append(1)
        
#    winners.append(playOneGame(Mariners,BlueJays, myDiamond))

#winners = np.array(winners) 

labels = ['Mariners','Blue Jays']

sizes = [(numGames/100)*winners.count(0), (numGames/100)*winners.count(1)]

pylab.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True)
pylab.axis('equal')
pylab.show()




#pylab.hist(winners, bins=2)
#pylab.xlabel('Teams')
#pylab.ylabel('Wins')
#pylab.title('Who won the most games?')
#pylab.show()

















        

