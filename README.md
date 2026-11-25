# Repositorio-SSC0524
Repositório para anotações e algoritmos desenvolvidos para a disciplina de Verificação, Validação e Teste de Software do curso de Sistemas de Informação da USP.

## Programação por contrato
Paradigma de desenvolvimento de software que defende que todo módulo (classe, função) deve estabelecer um contrato com o restante do sistema. Este contrato deve declarar as **pré-condições**, **pós-condições** e **invariantes** que devem ser respeitadas durante a execução daquele módulo.

- Pré-condições: condições que devem ser verdadeiras antes da execução do módulo.
- Pós-condições: condições que devem ser verdadeiras após a execução do módulo.
- Invariantes: condições que devem permanecer verdadeiras antes e após a execução do módulo.
  
## Teste funcional
Objetivo: avaliar se um determinado recurso do sistema opera em conformidade com os requisitos funcionais. Trata-se de um teste baseado nas especificações, o código não deve ser considerado.

Etapas para o desenvolvimento de um teste funcional:
- Identificar o **domínio** (tipo e valor) dos dados de entrada e saída
- Identificar as **classes de equivalência** (normais e excepcionais): intervalos no domínio, sendo que todos os valores de um mesmo intervalo devem ser processados da mesma maneira
- Identificar representantes (valores) de cada classe: é interessante incluir os limites dos intervalos
- Criar casos de teste

Use da sua criatividade para identificar casos de borda (Ex: array tamanho 0, null)

## Teste unitário em Python com Unittest
Teste unitário: teste realizado em uma parte isolada do sistema, como uma função.
Conceitos fundamentais para a compreensão de teste unitário:

- **Caso de teste**
Unidade individual de teste, verifica a resposta de um componente em razão de um conjunto de valores de entrada. No unittest, um caso de teste é criado com a classe Testcase, e então os testes são adicionados através de métodos.

- **Test suite**
Coleção de casos de teste que são executados conjuntamente para demonstrar algum comportamento do software.

- **Fixtures**
Conjunto de ações dedicadas a criação de um ambiente apropriado para a execução dos testes. Em unittest costuma-se usar o método setUp().

- **Test runner**
Componente que executa os casos de teste e comunica os resultados ao usuário.

Unittest: biblioteca padrão do python utilizada para produzir e executar testes automatizados.
```
    import unittest

    class TestCalculatorSum(unittest.Testcase):
        def test_positive_sum(self):
            assertEqual(add(1,2), 3)

        def test_negative_sum(self)
            pass

    class TestCalculatorSub(unittest.Testcase):
        def test_positive_sub(self):
            assertEqual(sub(5,3) 2)

```
 