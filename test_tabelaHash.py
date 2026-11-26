import unittest
from tabelaHash import TabelaHashSondagemLinear

# Conjunto de testes automatizados desenvolvidos a partir
# dos casos de teste documentados em "/TestesFuncionais.pdf"
# para a atividade descrita em "documents/teste_funcional.pdf"

class TesteTabelaHash(unittest.TestCase):

    def test_capacidade_negativa_levanta_AssertionError(self):
        with self.assertRaises(AssertionError):
            TabelaHashSondagemLinear(-1)

    def test_capacidade_zero_levanta_AssertionError(self):
        with self.assertRaises(AssertionError):
            TabelaHashSondagemLinear(0)

    def test_capacidade_bool_levanta_AssertionError(self):
        with self.assertRaises(AssertionError):
            TabelaHashSondagemLinear(False)

    def test_capacidade_inteiro_positivo_cria_tabela_vazia_capacidade_especificada(self):
        tabela = TabelaHashSondagemLinear(20)
        self.assertEqual(tabela.capacidade, 20)
        self.assertEqual(tabela.quantidade, 0)

    def test_capacidade_padrao_cria_tabela_vazia_capacidade_11(self):
        tabela = TabelaHashSondagemLinear()
        self.assertEqual(tabela.capacidade, 11)
        self.assertEqual(tabela.quantidade, 0)

class TesteValidarChave(unittest.TestCase):
    def setUp(self):
        self.tabela = TabelaHashSondagemLinear()
    
    def test_chave_bool_levanta_AssertionError(self):
        with self.assertRaises(AssertionError):
            self.tabela._validar_chave(True)

        with self.assertRaises(AssertionError):
            self.tabela._validar_chave(False)

    def test_chave_numerica_negativa_levanta_AssertionError(self):
        with self.assertRaises(AssertionError):
            self.tabela._validar_chave(-1)

        with self.assertRaises(AssertionError):
            self.tabela._validar_chave(-0.01)

    def test_chave_string_longa_levanta_AssertionError(self):
        with self.assertRaises(AssertionError):
            self.tabela._validar_chave("sou_uma_string_com_mais_de_dezesseis_caracteres")
        
        with self.assertRaises(AssertionError):
            self.tabela._validar_chave("string_com_17char")

    def test_chave_string_char_notASCII_levanta_AssertionError(self):
        with self.assertRaises(AssertionError):
            self.tabela._validar_chave("ĉhäŕ💘💘")

class TesteFuncaoHash(unittest.TestCase):

    def setUp(self):
        self.tabela = TabelaHashSondagemLinear(10)

    def test_inteiro_menor_que_capacidade_retorna_inteiro(self):
        self.assertEqual(self.tabela.funcao_hash(9), 9)

    def test_inteiro_maior_que_capacidade_retorna_modulo(self):
        self.assertEqual(self.tabela.funcao_hash(12), 12%self.tabela.capacidade)

    def test_string_retorna_soma_unicode(self):
        self.assertEqual(self.tabela.funcao_hash("oi"), (ord("o") + ord("i"))%self.tabela.capacidade)

    def test_float_retorna_soma_unicode(self):
        self.assertEqual(self.tabela.funcao_hash(5.5), (ord("5") + ord(".") + ord("5"))%self.tabela.capacidade)

    def test_integracao_validar_chave_recusa_chave_invalida(self):
        with self.assertRaises(AssertionError):
            self.tabela.funcao_hash(-10)
    
if __name__ == '__main__':
    unittest.main()

