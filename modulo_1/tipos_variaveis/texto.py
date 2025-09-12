# Declaração
nome_completo = "Igor Landi"

nome_completo_aspas = """Igor
Landi"""

nome_completo_quebra = "Igor \
Landi"

nome = "Igor"
sobrenome = "Landi"

# Formatação
print("nome completo (1a forma):", nome_completo)
print("nome completo (2a forma):" + nome_completo)
print("nome completo (3a forma):" + "Igor" + "Landi")
print("nome completo (4a forma):" + "Igor", "Landi")
print("nome completo (5a forma):", nome_completo_aspas)
print("nome completo (6a forma):", nome_completo_quebra)
print("nome completo (7a forma): %s" % nome_completo)
print("nome completo (8a forma): %s %s" % (nome, sobrenome))
print(f"nome completo (9a forma): {nome} {sobrenome}")
print("nome completo (10a forma): {} {}".format(nome, sobrenome))