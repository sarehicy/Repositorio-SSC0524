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

class TesteProcurarPosicao(unittest.TestCase):
    def setUp(self):
        self.tabelaHash = TabelaHashSondagemLinear(5)
        self.tabelaHash.inserir(4, "ola!")


    def test_chave_armazenada_sem_insercao_retorna_indice(self):
        pos = self.tabelaHash.funcao_hash(4)
        self.assertEqual(self.tabelaHash._procurar_posicao(4, False), pos)

    def test_chave_inexistente_sem_insercao_retorna_none(self):
        self.assertEqual(self.tabelaHash._procurar_posicao(2, False), None)

    def test_chave_armazenada_com_insercao_retorna_indice(self):
        pos = self.tabelaHash.funcao_hash(4)
        self.assertEqual(self.tabelaHash._procurar_posicao(4, True), pos)

    def test_chave_inexistente_com_insercao_retorna_melhor_pos(self):
        pos = self.tabelaHash.funcao_hash(2)
        self.assertEqual(self.tabelaHash._procurar_posicao(2, True), pos)

        #com colisao
        pos = (self.tabelaHash.funcao_hash(9) + 1)% self.tabelaHash.capacidade
        self.assertEqual(self.tabelaHash._procurar_posicao(9, True), pos)

    def test_chave_inexistente_com_insercao_tabela_cheia_retorna_none(self):
        self.tabelaHash.inserir(0, "preenchendo tabela..")
        self.tabelaHash.inserir(1, "preenchendo tabela..")
        self.tabelaHash.inserir(2, "preenchendo tabela..")
        self.tabelaHash.inserir(3, "preenchendo tabela..")

        self.assertEqual(self.tabelaHash._procurar_posicao(5), None)

class TesteInserir(unittest.TestCase):
    def setUp(self):
        self.tabelaHash = TabelaHashSondagemLinear(10)

    def test_chave_inedita_consegue_inserir(self):
        self.tabelaHash.inserir(15, "oie!")
        pos = self.tabelaHash.funcao_hash(15)
        self.assertEqual(self.tabelaHash.tabela[pos], (15, "oie!"))
        self.assertEqual(self.tabelaHash.quantidade, 1)

    def test_chave_repetida_atualiza_valor(self):
        self.tabelaHash.inserir(15, "oie!")
        pos = self.tabelaHash.funcao_hash(15)
        self.assertEqual(self.tabelaHash.tabela[pos], (15, "oie!"))
        self.tabelaHash.inserir(15, "tchauu!")
        self.assertEqual(self.tabelaHash.tabela[pos], (15, "tchauu!"))
        self.assertEqual(self.tabelaHash.quantidade, 1)

    def test_tabela_cheia_levanta_OverflowError(self):
        self.tabelaHash.inserir(1, "um")
        self.tabelaHash.inserir(2, "dois")
        self.tabelaHash.inserir(3, "tres")
        self.tabelaHash.inserir(4, "quatro")
        self.tabelaHash.inserir(5, "cinco")
        self.tabelaHash.inserir(6, "seis")
        self.tabelaHash.inserir(7, "sete")
        self.tabelaHash.inserir(8, "oito")
        self.tabelaHash.inserir(9, "nove")
        self.tabelaHash.inserir(10, "dez")

        self.assertEqual(self.tabelaHash.quantidade, 10)
        with self.assertRaises(OverflowError):
            self.tabelaHash.inserir(11, "overflow!!")
    
    def test_colisao_insere_na_melhor_posicao(self):
        self.tabelaHash.inserir(1, "um")
        self.tabelaHash.inserir(11, "colisao!!")

        pos = (self.tabelaHash.funcao_hash(11) + 1) % self.tabelaHash.capacidade
        self.assertEqual(self.tabelaHash.tabela[pos], (11, "colisao!!"))
        self.assertEqual(self.tabelaHash.quantidade, 2)

    
if __name__ == '__main__':
    unittest.main()

