import unittest
from src.cadastro_user import add, cadastrar_usuario, usuarios

class TestCadastroUser(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1, 1), 2)
    
    def setUp(self):
        
        usuarios.clear()

    def test_cadastrar_novo_usuario(self):
        resultado = cadastrar_usuario("João", "joao@example.com")
        self.assertEqual(resultado, "Usuário cadastrado com sucesso")
        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0]['nome'], "João")
        self.assertEqual(usuarios[0]['email'], "joao@example.com")

    def test_cadastrar_usuario_email_duplicado(self):
        cadastrar_usuario("João", "joao@example.com")
        resultado = cadastrar_usuario("Maria", "joao@example.com") 
        self.assertEqual(resultado, "Email já cadastrado")
        self.assertEqual(len(usuarios), 1)

    def test_cadastrar_varios_usuarios(self):
        cadastrar_usuario("João", "joao@example.com")
        cadastrar_usuario("Maria", "maria@example.com")
        self.assertEqual(len(usuarios), 2)
        self.assertEqual(usuarios[1]['nome'], "Maria")
        self.assertEqual(usuarios[1]['email'], "maria@example.com")

    def test_cadastrar_usuario_email_vazio(self):
        resultado = cadastrar_usuario("João", "")
        self.assertEqual(resultado, "Email inválido")
        self.assertEqual(len(usuarios), 0)

if __name__ == '__main__':
    unittest.main()