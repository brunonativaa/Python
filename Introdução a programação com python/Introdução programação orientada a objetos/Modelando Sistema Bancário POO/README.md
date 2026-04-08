# Sistema Bancário com Python e POO 🏦

"Este projeto marca minha primeira interação prática com POO. Enfrentei desafios durante o processo, mas, com dedicação e auxílio, utilizei cada dificuldade como um ponto de partida para o aprendizado."

## 🚀 Funcionalidades

- **Cadastro de Clientes:** Registra nome, CPF, endereço e data de nascimento.
- **Criação de Contas:** Permite criar contas correntes vinculadas a um cliente.
- **Operações Financeiras:**
  - Depósitos.
  - Saques (com verificação de saldo e limites).
- **Histórico/Extrato:** Registro detalhado de todas as transações realizadas.
- **Listagem:** Visualização de todas as contas cadastradas no sistema.


## 🛠️ Tecnologias e Conceitos Aplicados

- **Python 3**
- **POO (Programação Orientada a Objetos):**
  - **Classes Abstratas (ABC):** Utilizadas para definir a estrutura de Transações.
  - **Herança:** Classe `PessoaFisica` herdando de `Cliente`.
  - **Encapsulamento:** Uso de propriedades (`@property`) e atributos protegidos (`_saldo`).
  - **Polimorfismo:** Métodos de saque e depósito com comportamentos específicos.

## 🧠 Desafios Superados e Aprendizados

Durante o desenvolvimento deste projeto, enfrentei desafios técnicos que foram fundamentais para consolidar meu entendimento sobre Programação Orientada a Objetos em Python:

### 1. Métodos Especiais (Dunder Methods)
*   **Problema:** Ao listar as contas, o terminal exibia apenas o endereço de memória do objeto (ex: `<__main__.ContaCorrente object...>`).
*   **Solução:** Implementei corretamente o método especial `__str__`. Aprendi que esses métodos "mágicos" permitem que o Python converta objetos em strings legíveis para o usuário final.

### 2. Encapsulamento e @property
*   **Problema:** Erro de `AttributeError: can't set attribute` ao tentar inicializar o histórico de transações.
*   **Causa:** Conflito de nomes entre o atributo de inicialização e o método decorado com `@property`.
*   **Solução:** Adotei a convenção de usar atributos "protegidos" com underline (ex: `self._transacoes`). Isso garantiu que o acesso fosse feito via propriedade, mantendo a integridade dos dados e respeitando o conceito de encapsulamento.

### 3. Herança e Inicialização de Superclasses
*   **Problema:** Erro de `TypeError` por falta de argumentos na criação da `ContaCorrente`.
*   **Causa:** O construtor da classe base (`Conta`) exigia parâmetros que não estavam sendo passados corretamente via `super().__init__`.
*   **Solução:** Ajustei a passagem de argumentos no `super()`, garantindo que o saldo inicial fosse definido corretamente e que o vínculo com o objeto `Cliente` fosse estabelecido sem erros de posição.

### 4. Gestão de Fluxo e Tipagem
*   **Problema:** Erro `AttributeError: 'list' object has no attribute 'contas'`.
*   **Causa:** Passagem da lista completa de clientes para funções que esperavam um objeto cliente individual.
*   **Solução:** Melhorei a lógica de filtragem com `filtrar_cliente` e padronizei a nomenclatura de variáveis (plural para coleções, singular para instâncias), evitando confusão no fluxo de dados do programa.


