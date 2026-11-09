from typing import Optional #usado para indicar q um dado opcionalmente é de um determinado tipo
from typing import Any

class tabelaHashSondagemLinear:

    def __init__(self, capacidade: int = 11) -> None: # isso eh o cabecalho do metodo
        
        assert isinstance(capacidade, int) and not isinstance(capacidade, bool)
        #ou simplesmente: assert type(capacidade) is int

        assert capacidade > 0

    def _procurar_posicao(key: str | int | float, insertionFlag: bool = false) -> Optional[int]:
        assert type(key) is str or ((type(key) is int or type(key) is float) and key > 0)
        assert type(insertionFlag) is bool

    def inserir(key: str | int | float, value: Any) -> None:
         assert type(key) is str or ((type(key) is int or type(key) is float) and key > 0)

    def buscar(key: str | int | float) -> Any:
        assert type(key) is str or ((type(key) is int or type(key) is float) and key > 0)

    def remover(key: str | int | float) -> None:
        assert type(key) is str or ((type(key) is int or type(key) is float) and key > 0)
    
    def contem(value: Any)

def funcao_hash(key: str | int | float ) -> int:
    #ou a chave eh textual, ou eh numerica e positiva!
    assert type(key) is str or ((type(key) is int or type(key) is float) and key > 0)



