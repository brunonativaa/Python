import sqlite3

# ------ Settings incial --------
connection = sqlite3.connect("minha_agenda.db")
cursor = connection.cursor()

# Inserindo Dados (CREATE)
def adicionar_contato(cursor,connection,nome, telefone,):
    sql = '''INSERT INTO contatos ( nome, telefone)  VALUES (?,?)''' # Uma maneira de evitar o sql injection (?.?)
    cursor.execute(sql, [nome, telefone])
    connection.commit() # Salva no Bank
    print(f"Contato {nome} Added Successfully ")

#nome_cliente = input("Digite seu nome: ")
#tel_cliente = input("Digite telefone: ")
#adicionar_contato(cursor, connection, nome_cliente, tel_cliente)



# CUIDADO: Delete sem WHERE
# CUIDADO: SQL Injection


# Cria a tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT NOT NULL          
)

''')

# Consultando Dados (Read)
def listar_contatos(cursor):
      cursor.execute("SELECT * FROM contatos")
      return  cursor.fetchall()  # Retorna todos os registros da tabela contatos.


todos_contatos = listar_contatos(cursor)
print("\n--- Lista de Contatos ---")
for c in todos_contatos:
    print(f"ID: {c[0]} | Nome: {c[1]} | Telefone: {c[2]}")

# Atualizando e Deletando (Update & Delete)
def atualizar_telefone(cursor,connection,id, telefone,):
        sql = "UPDATE contatos SET telefone = ? WHERE id = ?"
        cursor.execute(sql, (telefone, id))
        connection.commit()
        print("Numero atualizado!") 
#atualizar_telefone(cursor,connection,20,"(011)1804-2026")


      

# Atualizando e Deletando (Update & Delete)
def excluir_contato(cursor,connection,id): # CUIDADO: Delete sem WHERE
      cursor.execute("DELETE FROM contatos WHERE id = ?", (id,))
      connection.commit()
      print("Contato Removido!")

#excluir_contato(cursor,connection,20,)




cursor.close()
connection.close()


