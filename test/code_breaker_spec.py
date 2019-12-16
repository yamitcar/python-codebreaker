from mamba import description, context, it
from expects import expect, equal
from models.code_breaker import CodeBreaker


with description('Code breaker') as self:
  with context('configurar numero secreto'):
    with it('si el numero es 1234 debe ser valido'):
      code_breaker = CodeBreaker('1234')
      expect(code_breaker.is_valid).to(equal(True))
    
    with it('si el numero es 12 debe ser invalido'):
      code_breaker = CodeBreaker(12)
      expect(code_breaker.is_valid).to(equal(False))

    with it('si el numero es 1123 debe ser invalido'):
      code_breaker = CodeBreaker(1123)
      expect(code_breaker.is_valid).to(equal(False))

    with it('si la cadena es "hola" debe ser invalido'):
      code_breaker = CodeBreaker("hola")
      expect(code_breaker.is_valid).to(equal(False))

    with it('si el valor es vacio debe ser invalido'):
      code_breaker = CodeBreaker(None)
      expect(code_breaker.is_valid).to(equal(False))

  with context("Adivinar el numero secreto"):
    with it("Si el numero es 12 debe devolver invalido"):
      code_breaker = CodeBreaker("1234")
      
      expect(code_breaker.guess("12")).to(equal(False))

    with it("Si el numero es 1234 adivino con 5678 debe devolver 5678: 0M-0PM"):
      code_breaker = CodeBreaker("1234")
      
      expect(code_breaker.guess("5678")).to(equal("5678: 0M-0PM"))

    with it("Si el numero es 1234 adivino con 1278 debe devolver 1278: 2M-0PM"):
      code_breaker = CodeBreaker("1234")
      
      expect(code_breaker.guess("1278")).to(equal("1278: 2M-0PM"))

    with it("Si el numero es 1234 adivino con 4321 debe devolver 4321: 0M-4PM"):
      code_breaker = CodeBreaker("1234")
      
      expect(code_breaker.guess("4321")).to(equal("4321: 0M-4PM"))

    with it("Si el numero es 1234 adivino con 1243 debe devolver 1243: 2M-2PM"):
      code_breaker = CodeBreaker("1234")
      
      expect(code_breaker.guess("1243")).to(equal("1243: 2M-2PM"))

    with it("Si el numero es 1234 adivino con 7890 debe devolver 7890: 0M-0PM"):
      code_breaker = CodeBreaker("1234")
      
      expect(code_breaker.guess("7890")).to(equal("7890: 0M-0PM"))

    with it("Si el numero es 1234 adivino con 1234 debe devolver 1234: Adivinaste!"):
      code_breaker = CodeBreaker("1234")
      
      expect(code_breaker.guess("1234")).to(equal("1234: Adivinaste!"))