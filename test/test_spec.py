from mamba import description, context, it
from expects import expect, equal
from game.game import Game


# 

with description('Game') as self:
  with it('el game inicia 0-0'):
    game = Game()
    expect(game.score).to(equal('0-0'))

  with it('el j1 anota y vamos 15-0'):
    game = Game()
    game.pointTo('J1')
    expect(game.score).to(equal('15-0'))

  with it('el j1 anota 2 puntos y vamos 30-0'):
    game = Game()
    game.pointTo('J1')
    game.pointTo('J1')
    expect(game.score).to(equal('30-0'))

  with it('el j1 anota 3 puntos y vamos 40-0'):
    game = Game()
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J1')
    expect(game.score).to(equal('40-0'))

  with it('el j2 anota 1 punto y vamos 0-15'):
    game = Game()
    game.pointTo('J2')
    expect(game.score).to(equal('0-15'))

  with it('el j2 anota 4 punto y vamos WINJ2'):
    game = Game()
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J2')
    expect(game.score).to(equal('WINJ2'))

  with it('el j1 anota 4 puntos y vamos WINJ1'):
    game = Game()
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J1')
    expect(game.score).to(equal('WINJ1'))

  with it('el j1 anota 3 puntos y el J2 tambien y vamos DEUCE'):
    game = Game()
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J2')
    expect(game.score).to(equal('DEUCE'))

  with it('estamos en DEUCE y j1 anota vamos en ADVJ1'):
    game = Game()
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J1')
    expect(game.score).to(equal('ADVJ1'))

  with it('estamos en DEUCE y j2 anota vamos en ADVJ2'):
    game = Game()
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J2')
    expect(game.score).to(equal('ADVJ2'))

  with it('estamos en ADVJ2 y j2 anota  vamos en WINJ2'):
    game = Game()
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J2')
    expect(game.score).to(equal('WINJ2'))

  with it('estamos en ADVJ1 y j1 anota  vamos en WINJ1'):
    game = Game()
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J1')
    game.pointTo('J1')
    expect(game.score).to(equal('WINJ1'))

  with it('estamos en ADVJ1 y j2 anota vamos en DEUCE'):
    game = Game()
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J1')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J2')
    game.pointTo('J1')
    game.pointTo('J2')
    expect(game.score).to(equal('DEUCE'))