ZetaCompiler

Compilador simples da linguagem fictícia Zeta para Python.
Este projeto permite criar programas na linguagem Zeta e executá-los em Python, incluindo:

Variáveis numéricas (inteiro e real)

Estruturas condicionais (se ... senao)

Estruturas de repetição (enquanto, faça ... enquanto)

Operações aritméticas e relacionais

Comandos de leitura (leia) e escrita (escreva)

Estrutura do projeto
ZetaCompiler/
│
├─ generated/                # arquivos gerados pelo ANTLR
│   ├─ __init__.py
│   ├─ ZetaLexer.py
│   ├─ ZetaParser.py
│   └─ ZetaVisitor.py
├─ MyVisitor.py              # visitor Python funcional
├─ run_zeta.py               # script para rodar o programa
├─ programa.zeta             # exemplo de programa Zeta
├─ Zeta.g4                   # gramática ANTLR
└─ README.md                 # este tutorial

Pré-requisitos

Python 3.8 ou superior

Java (para gerar os arquivos do ANTLR)

ANTLR 4.13.1 (antlr-4.13.1-complete.jar)

Passo 1: Gerar os arquivos Python do ANTLR

Baixe o ANTLR:

wget https://www.antlr.org/download/antlr-4.13.1-complete.jar


Gere os arquivos Python:

java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor Zeta.g4 -o generated


Crie o __init__.py para transformar generated em módulo Python:

touch generated/__init__.py

Passo 2: Estrutura de pastas

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

Passo 3: Rodando o compilador

No terminal:

python3 run_zeta.py


O programa irá:

Ler o arquivo programa.zeta

Interpretar o código Zeta

Executar os comandos de leitura/escrita e calcular expressões

Mostrar os resultados no terminal

Exemplo de programa.zeta
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

Exemplo de saída

Supondo a = 5 e b = 8:

Bem-vindo ao programa de teste!
Digite A:
5
Digite B:
8
A é menor que B
