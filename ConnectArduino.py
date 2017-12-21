# -*- coding: utf-8 -*-
# You can enter a series of moves including X, Y, Z, M, E, S
# The program will convert it into some simple "one face" moves like U, D, L, R, F, B
# ***NOTICE: You can only use capitalization like "R", not "r". And use "Ri" to present the invert turn.

import serial
#ser = serial.Serial('COM9', 9600)

pre = {'U':'U', 'Ui':'u', 'D':'D', 'Di':'d', 'L':'L', 'Li':'l', 'R':'R', 'Ri':'r', 'F':'F', 'Fi':'f', 'B':'B', 'Bi':'b'}
trans = {'U':'U', 'Ui':'u', 'D':'D', 'Di':'d', 'L':'L', 'Li':'l', 'R':'R', 'Ri':'r', 'F':'F', 'Fi':'f', 'B':'B', 'Bi':'b'}



class Encoder():


    def send(self, moves):
        words = moves.split(" ")
        global trans
        for word in words:
            #word = trans.get(word, "nothing")
            try:
                word = trans[word]
            except:
            	self.expect(word)
            else:
                self.serwrite(word)

    def serwrite(self, move):
        #ser.write(move.encode())
        print move


    def expect(self, move):
        if move == 'E':
            self.serwrite('U')
            self.serwrite('Di')
            self.rotation('Yi')
        elif move == 'Ei':
            self.serwrite('Ui')
            self.serwrite('D')
            self.rotation('Y')
        elif move == 'M':
            self.serwrite('R')
            self.serwrite('Li')
            self.rotation('Xi')
        elif move == 'Mi':
            self.serwrite('Ri')
            self.serwrite('L')
            self.rotation('X')
        elif move == 'S':
            self.serwrite('Fi')
            self.serwrite('B')
            self.rotation('Z')
        elif move == 'Si':
            self.serwrite('F')
            self.serwrite('Bi')
            self.rotation('Zi')
        else:
            self.rotation(move)

    def rotation(self, direction):
        global pre
        global trans
        if direction == 'X':
            trans['U'] = pre['F']
            trans['Ui'] = pre['Fi']
            trans['D'] = pre['B']
            trans['Di'] = pre['Bi']
            trans['F'] = pre['D']
            trans['Fi'] = pre['Di']
            trans['B'] = pre['U']
            trans['Bi'] = pre['Ui']

        elif direction == 'Xi':
            trans['F'] = pre['U']
            trans['Fi'] = pre['Ui']
            trans['B'] = pre['D']
            trans['Bi'] = pre['Di']
            trans['D'] = pre['F']
            trans['Di'] = pre['Fi']
            trans['U'] = pre['B']
            trans['Ui'] = pre['Bi']

        elif direction == 'Y':
            trans['R'] = pre['B']
            trans['Ri'] = pre['Bi']
            trans['L'] = pre['F']
            trans['Li'] = pre['Fi']
            trans['F'] = pre['L']
            trans['Fi'] = pre['Li']
            trans['B'] = pre['R']
            trans['Bi'] = pre['Ri']

        elif direction == 'Yi':
            trans['B'] = pre['R']
            trans['Bi'] = pre['Ri']
            trans['F'] = pre['L']
            trans['Fi'] = pre['Li']
            trans['L'] = pre['F']
            trans['Li'] = pre['Fi']
            trans['R'] = pre['B']
            trans['Ri'] = pre['Bi']

        elif direction == 'Z':
            trans['U'] = pre['L']
            trans['Ui'] = pre['Li']
            trans['D'] = pre['R']
            trans['Di'] = pre['Ri']
            trans['R'] = pre['U']
            trans['Ri'] = pre['Ui']
            trans['L'] = pre['D']
            trans['Li'] = pre['Di']

        elif direction == 'Zi':
            trans['L'] = pre['U']
            trans['Li'] = pre['Ui']
            trans['R'] = pre['D']
            trans['Ri'] = pre['Di']
            trans['U'] = pre['R']
            trans['Ui'] = pre['Ri']
            trans['D'] = pre['L']
            trans['Di'] = pre['Li']

        pre = trans.copy()



if __name__ == '__main__':
    '''Start the application'''
    moves = raw_input("enter moves, split by space:")
    while moves != "esc":
        Encoder().send(moves)
        moves = raw_input("enter moves, split by space:")
