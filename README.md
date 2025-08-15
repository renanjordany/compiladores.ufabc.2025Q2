# ZetaCompiler

Compilador simples da linguagem fictícia **Zeta** para Python.  
Este projeto permite criar programas na linguagem Zeta e executá-los em Python, incluindo:

- Variáveis numéricas (inteiro e real)  
- Estruturas condicionais (`se ... senao`)  
- Estruturas de repetição (`enquanto`, `faça ... enquanto`)  
- Operações aritméticas e relacionais  
- Comandos de leitura (`leia`) e escrita (`escreva`)  

---

## Estrutura do projeto

```text
ZetaCompiler/
├─ generated/
│   ├─ __init__.py
├─ MyVisitor.py
├─ run_zeta.py
├─ programa.zeta
├─ Zeta.g4
└─ README.md


## Pré-requisitos

- Python 3.8 ou superior  
- Java (para gerar os arquivos do ANTLR)  
- ANTLR 4.13.1 (`antlr-4.13.1-complete.jar`)  

---

## Gerar os arquivos Python do ANTLR

1. Baixe o ANTLR:

```bash
wget https://www.antlr.org/download/antlr-4.13.1-complete.jar
Gere os arquivos Python:

```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor Zeta.g4 -o generated
Crie o __init__.py para transformar generated em módulo Python:

```bash
touch generated/__init__.py

---

Estrutura de pastas

O projeto deve ficar assim:


ZetaCompiler/
├─ generated/
│   ├─ __init__.py
│   ├─ ZetaLexer.py
│   ├─ ZetaParser.py
│   └─ ZetaVisitor.py
├─ MyVisitor.py
├─ run_zeta.py
├─ programa.zeta
├─ Zeta.g4
└─ README.md

## Passo 3: Rodando o compilador
No terminal:

```bash
python3 run_zeta.py

O programa irá:

1. Ler o arquivo programa.zeta

2. Interpretar o código Zeta

3. Executar os comandos de leitura/escrita e calcular expressões

4. Mostrar os resultados no terminal

## Exemplo de programa.zeta

programa
declare a,b,c,media.

escreva("Bem-vindo ao programa de teste!").

escreva("Digite A").
leia(a).

escreva("Digite B").
leia(b).

c := a + b.
media := (a + b) / 2.

se (a < b) entao {
    escreva("A é menor que B").
} senao {
    escreva("A não é menor que B").
}

fimprog.
---

## Exemplo de saída
Supondo a = 5 e b = 8:


Bem-vindo ao programa de teste!
Digite A:
5
Digite B:
8
A é menor que B
--

## Observações
Para adicionar novos programas, basta criar arquivos .zeta e rodar com run_zeta.py.

A gramática Zeta (Zeta.g4) pode ser modificada para expandir recursos.

Todas as variáveis devem ser declaradas antes de usar.

