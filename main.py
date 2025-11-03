import sqlite3

# Conexão com o banco
conn = sqlite3.connect("Hospital.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Disciplina (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    Carga_horaria INTEGER
    
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matriculas INTEGER,
    nacionalidade TEXT
    
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Matrículas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    Disciplina TEXT,
    id_aluno INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES aluno(id)
)
""")










#cursor.execute ("DELETE FROM RESTAURANTE WHERE id = 2")

cursor.execute("INSERT INTO Matrículas (titulo,Disciplina) VALUES (?,?)", ('Professor','Ed.Física'))
# cursor.execute("INSERT INTO RESTAURANTE (nome,PRATO,PRECO,ITENS_PEDIDO) VALUES (?,?,?,?)", ('MARCELLA','PRATO RUA SEM SAIDA',10, 'doce' ))
# cursor.execute("INSERT INTO livros (titulo, ano, id_autor) VALUES (?, ?, ?)", ("Dom Casmurro", 1899, 1))
# cursor.execute("INSERT INTO autores ()")

# 👉 TAREFA: Inserir mais autores e livros

# 3 - UPDATE: Atualizar a data de devolução de um livro
# 👉 COMPLETE:
# cursor.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (..., ...))

# 4 - SELECT: Consultar os livros emprestados por um aluno
# 👉 COMPLETE:
# cursor.execute("SELECT ... FROM ... WHERE nome_aluno = ?", (...,))
# print(cursor.fetchall())

# 5 - DELETE: Remover um empréstimo concluído
# 👉 COMPLETE:
# cursor.execute("DELETE FROM ... WHERE id = ?", (...,))

conn.commit()

conn.close()