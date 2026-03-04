import sqlite3

# 1. Conectar ao banco de dados (Cria o arquivo se não existir)
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()

# 2. CREATE: Criar uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')
conn.commit()

# --- Funções CRUD ---

def inserir_usuario(nome, idade):
    cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', (nome, idade))
    conn.commit()
    print(f"Usuário {nome} inserido.")

def ler_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    for linha in cursor.fetchall():
        print(linha)

def atualizar_usuario(id, nova_idade):
    cursor.execute('UPDATE usuarios SET idade = ? WHERE id = ?', (nova_idade, id))
    conn.commit()
    print(f"Usuário {id} atualizado.")

def deletar_usuario(id):
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    conn.commit()
    print(f"Usuário {id} deletado.")

# --- Executando o CRUD ---
# inserir_usuario('Alice', 25)
# inserir_usuario('Bob', 30)
# ler_usuarios()
# atualizar_usuario(1, 26)
# deletar_usuario(2)

# Fechar conexão
conn.close()
