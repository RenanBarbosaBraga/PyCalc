PyCalc
======

Uma calculadora desktop desenvolvida em Python e PySide6, com interface gráfica personalizada e tema escuro.

FUNCIONALIDADES
---------------

- Adição (+), subtração (-), multiplicação (*) e divisão (/).
- Potenciação (^).
- Entrada de números decimais.
- Botão C para limpar a operação.
- Botão ◀ para apagar o último caractere.
- Tratamento de divisão por zero e resultados inválidos ou fora do intervalo.
- Interface escura utilizando QDarkStyle.
- Código organizado em módulos.

TECNOLOGIAS
-----------

- Python 3.10 ou superior
- PySide6
- QDarkStyle

ESTRUTURA DO PROJETO
--------------------

PyCalc/
|-- files/
|   |-- icon.png
|-- buttons.py
|-- display.py
|-- info.py
|-- main.py
|-- main_window.py
|-- styles.py
|-- utils.py
|-- variables.py
|-- requirements.txt
|-- README.txt

DESCRICAO DOS ARQUIVOS
----------------------

main.py
    Ponto de entrada da aplicação. Inicializa o Qt e monta a interface.

buttons.py
    Cria os botões da calculadora e implementa a lógica das operações.

display.py
    Componente responsável por exibir os números.

info.py
    Exibe a expressão matemática e o resultado.

main_window.py
    Define a janela principal e seu layout.

styles.py
    Configura o tema escuro e os estilos personalizados.

utils.py
    Contém funções auxiliares para validação de números.

variables.py
    Centraliza cores, dimensões e caminhos utilizados pela aplicação.

INSTALACAO
----------

1. Clone o repositório:

   git clone https://github.com/SEU_USUARIO/PyCalc.git

2. Entre na pasta do projeto:

   cd PyCalc

3. Crie um ambiente virtual:

   python -m venv venv

4. Ative o ambiente virtual.

   Windows PowerShell:
   venv\Scripts\Activate.ps1

   Linux / macOS:
   source venv/bin/activate

5. Instale as dependências:

   pip install -r requirements.txt

EXECUCAO
--------

Para iniciar a calculadora, execute:

    python main.py

STATUS DO PROJETO
-----------------

PyCalc é um projeto de aprendizado desenvolvido para praticar programação
Python, criação de interfaces gráficas com Qt, organização modular e
conexão de sinais e eventos.

MELHORIAS FUTURAS
-----------------

- Suporte à entrada pelo teclado.
- Histórico de cálculos.
- Funções de porcentagem e memória.
- Testes automatizados.
- Melhorias adicionais na validação de entradas.

LICENCA
-------

Nenhuma licença foi definida até o momento. Caso queira distribuir o
projeto como software de código aberto, adicione um arquivo LICENSE
com a licença escolhida.
