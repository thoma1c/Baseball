#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 14 18:11:22 2017

@author: tyler
"""
       
import random


class Player(object):
    
    def __init__(self, name, BA, number):
        
        self.name = name
        self.BA = BA
        self.number = number
        
        self.onBase = False
            
    def getPlayerName(self):        
        return self.name
        
    ##NEW:        
    def getPlayerBA(self):
        return self.BA
        
    def setOnBase(self):
        self.onBase = True
        
    def setOffBase(self):
        self.onBase = False
        
    def __str__(self):        
        return '<' + self.name + ' -#' + str(self.number) + '- BA:' + str(self.BA) + '>'

class Team(object):
    
    """
    city - sring of city name
    name - string of team's name
    Roster - a list of Player objects (So far just batters)
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


def loadRoster(teamFileName):
    
    roster = []

    with open(teamFileName) as t: ## with automatically closes the file
    
        for line in t:
            player_data = line.split(',')        
            
            roster.append(Player(player_data[0], int(player_data[1]), int(player_data[2])))
            
    return roster
    
def getTeamAverage(team):
    
    totAverages = 0

    for player in team.roster:
        
        totAverages += player.getPlayerBA() 
        
    #print(team.getTeamName() + ' Team Average: ' + str(round(totAverages / len(Angels.roster), 2)))
    return round(totAverages / len(Angels.roster)) #Decimal places is second variable

def simpleGame(awayTeam, homeTeam):
       
    awayScore = 0
    homeScore = 0

    for inning in range(1,10):
        
        newPrint('Inning:'+ str(inning) +  ' - Score:' + str(awayScore) + '-' + str(homeScore) )
        
        if random.randint(0,1000) < getTeamAverage(awayTeam):
            
            newPrint('Away scores!')
            awayScore += 1
            
        if inning == 9:
            
            if homeScore > awayScore:
                
                return homeTeam.getTeamName()
    
        if random.randint(0,1000) < getTeamAverage(homeTeam):
        
            newPrint('home scores!')
            homeScore += 1
        
    newPrint('Final Score:' + str(awayScore) + '-' + str(homeScore))


def newPrint(thing):
    
    ##Do we print?
    allow = True
    
    if allow:
        print(thing)
    
    
Angels = Team('LA','Angels',loadRoster("Teams/Angels_May_14.txt"))
newPrint(Angels)
newPrint('Angels team average: '+ str(getTeamAverage(Angels)))

Tigers = Team('Detroit', 'Tigers', loadRoster("Teams/Tigers_May_14.txt"))
newPrint(Tigers)
newPrint('Tigers team average: '+ str(getTeamAverage(Tigers)))

simpleGame(Tigers, Angels)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    
    







