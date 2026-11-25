import unittest
from tabelaHash import TabelaHashSondagemLinear

# Conjunto de testes automatizados desenvolvidos a partir
# dos casos de teste documentados em "/TestesFuncionais.pdf"
# para a atividade descrita em "documents/teste_funcional.pdf"

class TesteTabelaHash(unittest.TestCase):

    def test_capacidade_negativa(self):
        with self.assertRaises(AssertionError):
            TabelaHashSondagemLinear(-1)

    def test_capacidade_zero(self):
        with self.assertRaises(AssertionError):
            TabelaHashSondagemLinear(0)

    def test_capacidade_bool(self):
        with self.assertRaises(AssertionError):
            TabelaHashSondagemLinear(False)

    def test_capacidade_inteiro_positivo(self):
        tabela = TabelaHashSondagemLinear(20)
        self.assertEqual(tabela.capacidade, 20)
        self.assertEqual(tabela.quantidade, 0)

    def test_capacidade_padrao(self):
        tabela = TabelaHashSondagemLinear()
        self.assertEqual(tabela.capacidade, 11)
        self.assertEqual(tabela.quantidade, 0)


if __name__ == '__main__':
    unittest.main()

