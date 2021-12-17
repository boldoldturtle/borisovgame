import unittest
from main import goal
from main import pobed
from main import run
from main import raketki
from main import ball
# на функцию zapusk() нельзя написать тесты, так как эта функция - инициализация всего на экране
# тесты срабатывают, по завершении игры(победы одного из игроков или закрытия игры)
class TestGame(unittest.TestCase):


    #Тесты, проверяющие функцию счета в матче
    def test_score1(self):
        self.assertEqual(goal(),['0','1'])
    def test_score2(self):
        self.assertEqual(goal(),['1','0'])
    def test_score3(self):
        self.assertEqual(goal(),['5','5'])
    def test_score4(self):
        self.assertEqual(goal(),['10','1'])
    def test_score5(self):
        self.assertEqual(goal(),['4','7'])
    def test_score6(self):
        self.assertEqual(goal(),['2','6'])
    def test_score7(self):
        self.assertEqual(goal(),['5','10'])
    def test_score8(self):
        self.assertEqual(goal(),['0','0'])


    #тесты, показывающие, кто победил в матче
    def test_who_win1(self):
        self.assertEqual(pobed(),'Player1 win')
    def test_who_win2(self):
        self.assertEqual(pobed(),'Player2 win')


    #тест, на закрытие игры, и если игра идет
    def test_game_process(self):
        self.assertEqual(run(), 'Game closed')


    #тест, что ракетки каснулись границ
    def test_levaya_raketka_verh(self):
        self.assertEqual(raketki()[0],0)
    def test_levaya_raketka_niz(self):
        self.assertEqual(raketki()[0], 520)
    def test_pravaya_raketka_verh(self):
        self.assertEqual(raketki()[1],0)
    def test_pravaya_raketka_niz(self):
        self.assertEqual(raketki()[1],520)


    #тест на количество касаний мяча платформами
    def test_ball1(self):
        self.assertEqual(ball(),1)
    def test_ball2(self):
        self.assertEqual(ball(),5)
    def test_ball3(self):
        self.assertEqual(ball(),10)
    def test_ball4(self):
        self.assertEqual(ball(),20)
    def test_ball5(self):
        self.assertEqual(ball(),35)




if __name__ == '__main__':
    unittest.main()
