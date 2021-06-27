from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Ismael', email='ismael@ismael.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)




def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome='Ismael', email='ismael@ismael.com'), 
        Usuario(nome='Miranda', email='miranda@ismael.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
