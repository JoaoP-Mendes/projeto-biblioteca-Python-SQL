# Sistema de Gerenciamento de Biblioteca

Projeto acadêmico em Python + MySQL, rodando via terminal.

## Estrutura do projeto

```
biblioteca/
├── banco.sql       # Script SQL: cria o banco e as 3 tabelas
├── config.py       # Dados de conexão com o MySQL
├── banco.py        # Classe Bancodados: conexão e execução de queries
├── livro.py        # Classe Livro: CRUD de livros
├── usuario.py      # Classe Usuario: CRUD de usuários
├── emprestimo.py   # Classe Emprestimo: regras de empréstimo/devolução
└── main.py         # Menu do terminal, ponto de entrada do programa
```

## Como rodar

### 1. Instalar dependência
```
pip install pymysql
```

### 2. Criar o banco de dados
Execute o conteúdo de `banco.sql` no MySQL. Isso cria o banco `biblioteca`
e as 3 tabelas: `livros`, `usuario` e `emprestimo`.

### 3. Configurar a conexão
Edite `config.py` com o usuário/senha do seu MySQL local:
```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "passwd": "sua_senha_aqui",
    "database": "biblioteca"
}
```

### 4. Rodar o programa
```
python main.py
```

Isso abre o menu principal, com acesso aos 3 submenus: usuários, livros
e empréstimos.

## Arquitetura

O projeto é dividido em 4 camadas:

- **`config.py`** — guarda os dados de conexão (host, user, senha, database).
- **`banco.py`** (classe `Bancodados`) — responsável por conectar,
  desconectar e executar qualquer query SQL. Tem os métodos `conectar()`,
  `desconectar()` e `executar(query)`, que cria o cursor, roda a query e
  devolve o resultado (via `fetchall()` para SELECT, ou `lastrowid` após
  commit para INSERT/UPDATE/DELETE).
- **`livro.py`, `usuario.py`, `emprestimo.py`** — cada classe recebe um
  objeto `Bancodados` já conectado e usa `self.conexao.executar(...)`
  para todas as suas operações. Concentram o SQL e as regras de cada
  entidade.
- **`main.py`** — o menu de terminal. Cria os objetos (`Bancodados`,
  `Livro`, `Usuario`, `Emprestimo`) uma única vez no topo do arquivo, e
  tem um menu principal (`while True`) que chama as funções
  `menu_usuario()`, `menu_livro()` e `menu_emprestimo()`, cada uma com
  seu próprio submenu.

### Classe `Livro`
Métodos: `novoLivro()`, `listarLivros()`, `buscarPorId()`,
`buscarPorTituloOuAutor()`, `removerLivro()`, `atulizarLivro()`.

### Classe `Usuario`
Métodos: `novoUsuario()`, `listarUsuario()`, `buscaUsuarioPorId()`,
`buscarPorNome()`, `removerUsuario()`, `atualizarUsuario()`.

### Classe `Emprestimo`
Recebe no `__init__` a conexão, um objeto `Livro` e um objeto `Usuario`
— porque precisa consultar e alterar as tabelas `livros` e `usuario`
além da própria `emprestimo`.

- `registrarEmprestimo(idusuario, idlivro)`: busca o usuário e o livro
  pelo id, verifica se há exemplar disponível (`quantidade_disponivel`),
  e só então insere o registro na tabela `emprestimo` e diminui a
  quantidade do livro em 1. Se o usuário ou livro não existir, cai num
  `except IndexError` com aviso amigável.
- `registraDevolucao(idemprestimo)`: atualiza o status do empréstimo
  para `'devolvido'` (com a data de devolução), busca o `livro_id`
  daquele empréstimo, e devolve 1 unidade à quantidade disponível do
  livro.
- `buscaEmprestimoId()` e `listarEmprestimo()`: consultas de leitura.

## Tabelas (banco.sql)

- **`livros`**: id, titulo, autor, ano, quantidade_disponivel
- **`usuario`**: id, nome, email, telefone
- **`emprestimo`**: id, livro_id (FK), usuario_id (FK), data_emprestimo,
  data_devolucao, status (`'emprestado'` ou `'devolvido'`)
