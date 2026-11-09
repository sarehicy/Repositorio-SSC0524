from typing import Optional #usado para indicar q um dado opcionalmente é de um determinado tipo
from typing import Any
from typing import Hashable

class TabelaHashSondagemLinear:

    def __init__(self, capacidade: int = 11) -> None: # isso eh o cabecalho do metodo
        
        assert isinstance(capacidade, int) and not isinstance(capacidade, bool)
        #ou simplesmente: assert type(capacidade) is int
        assert capacidade > 0
        pass

    def _procurar_posicao(self, key: str | int | float, insertionFlag: bool = False) -> Optional[int]:
        assert type(key) is str or ((type(key) is int or type(key) is float) and key >= 0)
        assert type(insertionFlag) is bool
        pass

    def inserir(self, key: str | int | float, value: Any) -> None:
        assert type(key) is str or ((type(key) is int or type(key) is float) and key >= 0)
        pass

    def buscar(self, key: str | int | float) -> Any:
        assert type(key) is str or ((type(key) is int or type(key) is float) and key >= 0)
        pass

    def remover(self, key: str | int | float) -> None:
        assert type(key) is str or ((type(key) is int or type(key) is float) and key >= 0)
        pass

    # verifica se a CHAVE esta armazenada
    def contem(self, key: str | int | float) -> bool:
        assert type(key) is str or ((type(key) is int or type(key) is float) and key >= 0)
        pass

    # Hashable aqui indica q o valor nao eh modificavel
    # um não-modificavel eh um const, se o valor eh sempre o mesmo, entao ele eh passivel de hash
    def contem_valor(self, value: Hashable) -> bool:
        assert isinstance(value, Hashable) #Hashable eh uma classe abstrata, portanto type() nao funciona aqui!
        pass

    def chaves(self) -> list[str | int | float]:
        pass

    def valores(self) -> list[Any]:
        pass

    def itens(self) -> list[tuple[str | int | float, Any]]:
        pass

    def __len__(self) -> int:
        pass

    def __str__(self) -> str:
        pass

    def funcao_hash(self, key: str | int | float ) -> int:
        #ou a chave eh textual, ou eh numerica e positiva!
        assert type(key) is str or ((type(key) is int or type(key) is float) and key >= 0)
        pass


