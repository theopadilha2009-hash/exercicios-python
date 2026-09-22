# exercicios-python

## Identificação
- **Estudante:** Theo Lorentz Padilha
- **Turma:** DSM3-25
- **Unidade Curricular:** Programação de Aplicativos
- **Curso:** Técnico em Desenvolvimento de Sistemas — Integrado ao Ensino Médio
- **Docente:** Ewerton de Oliveira Cercal ([@ProfCercal](https://github.com/ProfCercal))
- **Instituição:** SENAI
- **Repositório:** Privado com colaborador adicionado (`ProfCercal`)

---

## Descrição do Projeto
Este repositório reúne a resolução comentada e modular de vinte e cinco exercícios práticos de lógica de programação desenvolvidos na linguagem Python. A atividade consolida a transição entre fundamentos teóricos e desenvolvimento profissional, abrangendo conceitos essenciais como entrada e saída de dados, estruturas condicionais, laços de repetição (`while` e `for`) e manipulação de listas. Todo o projeto segue rigorosos critérios de versionamento com Git, documentação padronizada e boas práticas de arquitetura de pastas.

---

## Tecnologia Utilizada
- **Linguagem de Programação:** Python
- **Versão do Python:** `Python 3.9.6` (compatível com Python 3.9+)
- **Sistema de Controle de Versão:** Git 2.54.0
- **Hospedagem e Colaboração:** GitHub

Para verificar a versão do interpretador Python em seu terminal, execute:
```bash
python3 --version
```

---

## Como Executar os Exercícios

### Pré-requisitos
Certifique-se de que o Python 3 esteja instalado no seu computador.

### 1. Clonar o repositório
Abra o terminal e execute o comando:
```bash
git clone https://github.com/theopadilha2009-hash/exercicios-python.git
```

### 2. Acessar a pasta do projeto
```bash
cd exercicios-python
```

### 3. Executar qualquer exercício individualmente
Cada exercício pode ser executado diretamente chamando o interpretador Python com o caminho relativo do arquivo desejado.

Exemplos de execução:
```bash
# Executar o exercício 01 (Parte 1 - Variáveis)
python3 parte1-variaveis/ex01.py

# Executar o exercício 06 (Parte 2 - Condicionais)
python3 parte2-condicionais/ex06.py

# Executar o exercício 11 (Parte 3 - While)
python3 parte3-while/ex11.py

# Executar o exercício 16 (Parte 4 - For)
python3 parte4-for/ex16.py

# Executar o exercício 21 (Parte 5 - Listas)
python3 parte5-listas/ex21.py
```

### 4. Validação e compilação de todos os arquivos
Para validar a sintaxe e integridade de todos os 25 scripts sem executar entradas manuais:
```bash
python3 -m py_compile parte1-variaveis/*.py parte2-condicionais/*.py parte3-while/*.py parte4-for/*.py parte5-listas/*.py
```

---

## Estrutura do Repositório
```text
exercicios-python/
├── README.md
├── .gitignore
├── parte1-variaveis/
│   ├── ex01.py
│   ├── ex02.py
│   ├── ex03.py
│   ├── ex04.py
│   └── ex05.py
├── parte2-condicionais/
│   ├── ex06.py
│   ├── ex07.py
│   ├── ex08.py
│   ├── ex09.py
│   └── ex10.py
├── parte3-while/
│   ├── ex11.py
│   ├── ex12.py
│   ├── ex13.py
│   ├── ex14.py
│   └── ex15.py
├── parte4-for/
│   ├── ex16.py
│   ├── ex17.py
│   ├── ex18.py
│   ├── ex19.py
│   └── ex20.py
└── parte5-listas/
    ├── ex21.py
    ├── ex22.py
    ├── ex23.py
    ├── ex24.py
    └── ex25.py
```

---

## Índice dos Exercícios

### Parte 1 — Variáveis, Entrada e Saída
- **[`parte1-variaveis/ex01.py`](parte1-variaveis/ex01.py):** Declara variáveis com nome e idade e exibe cada informação em uma linha separada.
- **[`parte1-variaveis/ex02.py`](parte1-variaveis/ex02.py):** Solicita dois números ao usuário, converte as entradas e exibe a soma calculada.
- **[`parte1-variaveis/ex03.py`](parte1-variaveis/ex03.py):** Solicita o raio de um círculo e calcula sua área utilizando o valor de pi fixado em 3.14159.
- **[`parte1-variaveis/ex04.py`](parte1-variaveis/ex04.py):** Converte uma temperatura lida em graus Celsius para a escala Fahrenheit pela fórmula `F = C * 9 / 5 + 32`.
- **[`parte1-variaveis/ex05.py`](parte1-variaveis/ex05.py):** Lê o preço unitário e a quantidade comprada de um produto, calculando o valor total formatado com duas casas decimais.

### Parte 2 — Condicionais
- **[`parte2-condicionais/ex06.py`](parte2-condicionais/ex06.py):** Recebe um número inteiro e informa com precisão se ele é par ou ímpar.
- **[`parte2-condicionais/ex07.py`](parte2-condicionais/ex07.py):** Compara dois números e exibe qual é o maior ou informa se ambos são estritamente iguais.
- **[`parte2-condicionais/ex08.py`](parte2-condicionais/ex08.py):** Analisa um valor numérico informando se ele é positivo, negativo ou exatamente igual a zero.
- **[`parte2-condicionais/ex09.py`](parte2-condicionais/ex09.py):** Avalia a média escolar com tratamento de fronteiras (>= 6 Aprovado, 4 a 5.9 Recuperação, < 4 Reprovado).
- **[`parte2-condicionais/ex10.py`](parte2-condicionais/ex10.py):** Verifica a idade de uma pessoa informando se ela já possui idade suficiente para votar (mínimo 16 anos).

### Parte 3 — Repetição com while
- **[`parte3-while/ex11.py`](parte3-while/ex11.py):** Exibe a sequência de números inteiros de 1 a 10, um por linha, utilizando laço `while`.
- **[`parte3-while/ex12.py`](parte3-while/ex12.py):** Acumula valores inseridos pelo usuário em um laço `while` até a entrada da condição de parada 0, exibindo a soma final.
- **[`parte3-while/ex13.py`](parte3-while/ex13.py):** Valida repetidamente a entrada de uma senha até que a palavra-chave "senai123" seja digitada, liberando o acesso.
- **[`parte3-while/ex14.py`](parte3-while/ex14.py):** Exibe a tabuada completa de multiplicação de 1 a 10 para um determinado número informado pelo usuário.
- **[`parte3-while/ex15.py`](parte3-while/ex15.py):** Lê sucessivos números até que o valor 0 seja inserido e contabiliza quantos números estritamente positivos foram digitados.

### Parte 4 — Repetição com for
- **[`parte4-for/ex16.py`](parte4-for/ex16.py):** Percorre a faixa de 1 a 20 utilizando laço `for` com função geradora `range`, exibindo cada número em uma linha.
- **[`parte4-for/ex17.py`](parte4-for/ex17.py):** Imprime apenas os números pares de 2 a 20 aplicando parâmetros de passo (`step = 2`) no `range`.
- **[`parte4-for/ex18.py`](parte4-for/ex18.py):** Calcula e apresenta o somatório total de todos os números inteiros compreendidos no intervalo de 1 a 100.
- **[`parte4-for/ex19.py`](parte4-for/ex19.py):** Calcula o fatorial de um número natural fornecido utilizando multiplicação iterativa controlada por `for`.
- **[`parte4-for/ex20.py`](parte4-for/ex20.py):** Executa uma contagem regressiva de 10 até 1 utilizando passo negativo no `range` e finaliza exibindo a mensagem "Fim".

### Parte 5 — Listas
- **[`parte5-listas/ex21.py`](parte5-listas/ex21.py):** Cria uma lista contendo cinco números e itera sobre a coleção exibindo cada elemento individualmente.
- **[`parte5-listas/ex22.py`](parte5-listas/ex22.py):** Percorre iterativamente a lista de números do exercício anterior calculando o somatório total de seus elementos.
- **[`parte5-listas/ex23.py`](parte5-listas/ex23.py):** Determina o maior valor contido na lista inicializando a variável de comparação no primeiro índice da coleção.
- **[`parte5-listas/ex24.py`](parte5-listas/ex24.py):** Percorre a lista pré-definida `[5, 12, 8, 20, 3, 15]` e contabiliza quantos itens possuem valor estritamente superior a 10.
- **[`parte5-listas/ex25.py`](parte5-listas/ex25.py):** Exibe a lista `[3, 7, 1, 9, 4]` em ordem inversa utilizando controle explícito de índices decrementais, sem funções prontas.

---

## Justificativa das Regras do `.gitignore`
Para manter o repositório limpo, leve e focado exclusivamente no código-fonte, foram definidas regras com as seguintes justificativas:
1. `__pycache__/` e `*.py[cod]`: O Python gera arquivos compilados de bytecode `.pyc` automaticamente para acelerar inicializações subsequentes. Esses arquivos são dependentes da arquitetura da máquina e versão do interpretador, portanto não devem ser versionados.
2. `.venv/`, `venv/`, `env/`: Ambientes virtuais armazenam bibliotecas e binários locais da máquina de desenvolvimento. O versionamento de ambientes sobrecarrega o repositório e impede a portabilidade.
3. `.DS_Store`: Metadados gerados pelo Finder do sistema operacional macOS para guardar posições de ícones e preferências de exibição. Poluem o repositório e não possuem relação com o código.
4. `.vscode/` e `.idea/`: Diretórios de configuração de IDEs e editores que refletem preferências particulares de cada desenvolvedor, não devendo ser impostos a outros colaboradores.
5. `*.log`: Arquivos de registros de eventos ou depuração criados durante a execução, que mudam a cada rodada e contêm dados voláteis.

---

## Dificuldades Encontradas e Soluções Implementadas
- **Tratamento de casos de fronteira em condicionais:** No exercício de cálculo de média (`ex09.py`), foi necessário atenção para garantir que o limite inferior de recuperação (4.0) e o de aprovação (6.0) fossem testados com operadores relacionais adequados (`>=` e `<`), prevenindo falhas de arredondamento ou classificações incorretas em notas limítrofes.
- **Manipulação de laços sem contadores desnecessários:** Ao trabalhar com laços `for` (`ex16.py` ao `ex20.py`), a exploração completa dos argumentos da função `range(start, stop, step)` permitiu eliminar contadores manuais desnecessários, resultando em um código mais idiomático e limpo.
- **Inversão de lista através de índices (`ex25.py`):** Para cumprir o critério avançado da rubrica sem recorrer a funções embutidas como `reverse()` ou fatiamento `[::-1]`, foi implementada a navegação indexada calculando os índices do último elemento (`len(lista) - 1`) até o primeiro (`0`), demonstrando pleno entendimento da estrutura indexada de listas em Python.
- **Organização e versionamento semântico:** A divisão em múltiplos commits estruturados permitiu registrar o ciclo de desenvolvimento passo a passo, facilitando a rastreabilidade e a inspeção por parte do docente.
