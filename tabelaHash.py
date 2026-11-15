from collections.abc import Hashable
from typing import Any, TypeAlias, Union
#from typeguard import typechecked


Chave: TypeAlias = Union[str, int, float]
Entrada: TypeAlias = Union[tuple[Chave, Any], "MarcadorRemovido", None]


class MarcadorRemovido:
	"""
	Objeto especial usado para marcar posições removidas logicamente.

	Não usamos None, porque None significa "posição que nunca foi ocupada".
	"""
	pass


REMOVIDO = MarcadorRemovido()


#@typechecked


class TabelaHashSondagemLinear:
	def __init__(self, capacidade: int = 11) -> None:
		"""
		Cria uma tabela hash vazia com a capacidade indicada.
		"""
		assert isinstance(capacidade,int)
		assert not isinstance(capacidade, bool)
		assert capacidade > 0 
		self.capacidade: int = capacidade
		self.tabela: list[Entrada] = [None] * capacidade
		self.quantidade: int = 0



	def funcao_hash(self, chave: Chave) -> int:
		"""
		Função de hash manual e previsível.

		- Para int, utiliza o próprio valor.
		- Para str e float, soma os códigos dos caracteres de sua
		  representação textual.
		Em todos os métodos, a chave deve ser: 
			- um string com no máximo 16 carateres contendo apenas letras
			  digitos ou _
			- um númeto (int ou float) não negativo		
		"""
		self._validar_chave(chave)

		if isinstance(chave, int):
			posicao = chave % self.capacidade
		else:
			soma = 0

			for caractere in str(chave):
				soma += ord(caractere)

			posicao = soma % self.capacidade


		return posicao

	def _procurar_posicao(
		self,
		chave: Chave,
		para_insercao: bool = False
	) -> int | None:
		"""
		Procura a posição de uma chave na tabela.

		Se para_insercao=False:
			- retorna o índice da chave, se ela existir;
			- retorna None, se ela não existir.

		Se para_insercao=True:
			- retorna o índice da própria chave, se ela já existir;
			- retorna a melhor posição livre para inserir;
			- retorna None, se não houver posição disponível.
		"""
		self._validar_chave(chave)

		posicao_inicial = self.funcao_hash(chave)
		posicao = posicao_inicial
		primeira_removida: int | None = None
		passos = 0


		while passos < self.capacidade:

			entrada = self.tabela[posicao]

			if entrada is None:
				if para_insercao:
					if primeira_removida is not None:
						return primeira_removida

					return posicao

				return None

			if entrada is REMOVIDO:
				if para_insercao and primeira_removida is None:
					primeira_removida = posicao
			else:

				chave_guardada, _ = entrada

				if chave_guardada == chave:
					return posicao

			posicao = (posicao + 1) % self.capacidade
			passos += 1


		if para_insercao and primeira_removida is not None:
			return primeira_removida

		return None

	def inserir(self, chave: Chave, valor: Any) -> None:
		"""
		Insere um novo par (chave, valor) na tabela.

		Se a chave já existir, apenas atualiza o valor.
		"""
		self._validar_chave(chave)

		posicao = self._procurar_posicao(
			chave,
			para_insercao=True
		)

		if posicao is None:
			raise OverflowError("Tabela hash cheia.")


		entrada_atual = self.tabela[posicao]

		if entrada_atual is None or entrada_atual is REMOVIDO:
			self.tabela[posicao] = (chave, valor)
			self.quantidade += 1

		else:
			self.tabela[posicao] = (chave, valor)




	def buscar(self, chave: Chave) -> Any:
		"""
		Retorna o valor associado à chave.

		Lança KeyError se a chave não existir.
		"""
		self._validar_chave(chave)

		posicao = self._procurar_posicao(
			chave,
			para_insercao=False
		)

		if posicao is None:
			raise KeyError(f"Chave não encontrada: {chave}")


		entrada = self.tabela[posicao]


		return entrada[1]

	def remover(self, chave: Chave) -> None:
		"""
		Remove logicamente uma chave da tabela.
		"""
		self._validar_chave(chave)

		posicao = self._procurar_posicao(
			chave,
			para_insercao=False
		)

		if posicao is None:
			raise KeyError(f"Chave não encontrada: {chave}")

		assert self.tabela[posicao] is not None
		assert self.tabela[posicao] is not REMOVIDO

		self.tabela[posicao] = REMOVIDO
		self.quantidade -= 1



	def contem(self, chave: Chave) -> bool:
		"""
		Devolve True se a chave estiver na tabela e False caso contrário.
		"""
		self._validar_chave(chave)

		resultado = self._procurar_posicao(
			chave,
			para_insercao=False
		) is not None


		return resultado

	def contem_valor(self, valor: Any) -> bool:
		assert isinstance(valor, Hashable), (
			"O valor procurado não pode ser modificável."
		)

		for entrada in self.tabela:
			if isinstance(entrada, tuple):
				if entrada[1] == valor:
					return True

		return False
	
	def chaves(self) -> list[Chave]:
		"""
		Devolve uma lista com todas as chaves presentes na tabela.
		"""

		resultado: list[Chave] = []

		for entrada in self.tabela:
			if entrada is not None and entrada is not REMOVIDO:

				chave = entrada[0]
				self._validar_chave(chave)
				resultado.append(chave)


		return resultado

	def valores(self) -> list[Any]:
		"""
		Devolve uma lista com todos os valores presentes na tabela.
		"""

		resultado: list[Any] = []

		for entrada in self.tabela:
			if entrada is not None and entrada is not REMOVIDO:
				resultado.append(entrada[1])


		return resultado

	def itens(self) -> list[tuple[Chave, Any]]:
		"""
		Devolve uma lista de pares (chave, valor) presentes na tabela.
		"""

		resultado: list[tuple[Chave, Any]] = []

		for entrada in self.tabela:
			if entrada is not None and entrada is not REMOVIDO:

				self._validar_chave(entrada[0])
				resultado.append(entrada)


		return resultado

	def __len__(self) -> int:


		return self.quantidade

	def __str__(self) -> str:
		"""
		Gera uma representação textual da tabela,
		útil para depuração.
		"""

		linhas: list[str] = []

		for i, entrada in enumerate(self.tabela):
			if entrada is None:
				linhas.append(f"{i}: VAZIO")
			elif entrada is REMOVIDO:
				linhas.append(f"{i}: REMOVIDO")
			else:

				chave, valor = entrada
				linhas.append(f"{i}: {chave} -> {valor}")


		return "\n".join(linhas)

	def _validar_chave(self, chave: Chave) -> None:
		"""
		Verifica as pré-condições definidas para uma chave.

		Uma chave válida deve ser:
		- uma string com no máximo 16 caracteres, contendo somente
		  letras, dígitos ou "_"; ou
		- um número int ou float não negativo.

		Valores booleanos não são aceitos como chaves numéricas, embora
		bool seja uma subclasse de int em Python.
		"""
		assert not isinstance(chave, bool), (
			"A chave não pode ser um valor booleano."
		)

		if isinstance(chave, str):
			assert len(chave) <= 16, (
				"A chave textual deve ter no máximo 16 caracteres."
			)
			assert all(
				caractere.isascii()
				and (caractere.isalnum() or caractere == "_")
				for caractere in chave
			), (
				"A chave textual pode conter somente letras ASCII, "
				"dígitos ou '_'."
			)
		else:
			assert isinstance(chave, (int, float))
			assert chave >= 0, (
				"A chave numérica deve ser não negativa."
			)


