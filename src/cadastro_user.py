usuarios = []

def add(a, b):
    return a + b

def cadastrar_usuario(nome, email):    
    for usuario in usuarios:
        if usuario['email'] == email:
            return "Email já cadastrado"
        
    if not email.strip():
        return "Email inválido"
        
    novo_usuario = {
        'nome': nome,
        'email': email
    }
    usuarios.append(novo_usuario)
    return "Usuário cadastrado com sucesso"