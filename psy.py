#!/home/developer/520-domingo/venv/bin/python3
from psycopg2 import connect


try:
    con = connect('host=127.0.0.1 dbname=projeto user=admin password=4linux')
    cur = con.cursor()
except Exception as e:
    print("Erro: {}".format(e))
    exit()

cur.execute("select * from usuario;")
print(cur.fetchall())

#cur.execute("insert into usuario (nome, linguagem) values ('maria', 'php');")
ling = input('Digite nova linguagem? ' )
cur.execute("UPDATE usuario SET linguagem='{}' where id=1".format(ling))

cur.execute("delete from usuario")

cur.execute("insert into usuario (nome, linguagem) values ('maria', 'php');")
con.commit()
cur.close()
con.close()