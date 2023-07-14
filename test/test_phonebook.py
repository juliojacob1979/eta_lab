from src.phonebook import Phonebook

class TestPhonebook:

    def test_add_phonebook_com_sucesso(self):
        # Setup
        name_1 = 'Fabricio'
        number_1 = '455'
        resultado_esperado = f"Numero adicionado - `{number_1}` "
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_phonebook_nome_hash_invalido(self):
        # Setup
        name_1 = '#'
        number_1 = '888'
        resultado_esperado = f"Nome `{name_1}` invalido"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_phonebook_nome_arroba_invalido(self):
        # Setup
        name_1 = '@'
        number_1 = '333'
        resultado_esperado = f"Nome `{name_1}` invalido"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_phonebook_nome_exclamacao_invalido(self):
        # Setup
        name_1 = '!'
        number_1 = '567'
        resultado_esperado = f"Nome `{name_1}` invalido"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_phonebook_nome_dolar_invalido(self):
        # Setup
        name_1 = '$'
        number_1 = '9856'
        resultado_esperado = f"Nome `{name_1}` invalido"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_phonebook_nome_percentual_invalido(self):
        # Setup
        name_1 = '%'
        number_1 = '345'
        resultado_esperado = f"Nome `{name_1}` invalido"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_phonebook_numero_menor_zero(self):
        # Setup
        name_1 = 'tata'
        number_1 = []
        resultado_esperado = f"Numero `{number_1}` invalido"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_pesquisa_phonebook_nome_hash_nao_permitido(self):
        # Setup
        name_1 = '#'
        number_1 = '532'
        resultado_esperado = f"Nome `{name_1}` invalido"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.lookup(name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_pesquisa_phonebook_nome_arroba_nao_permitido(self):
        # Setup
        name_1 = '@'
        number_1 = '7896'
        resultado_esperado = f"Nome `{name_1}` invalido"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.lookup(name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_pesquisa_phonebook_nome_exclamacao_nao_permitido(self):
        # Setup
        name_1 = '!'
        number_1 = '683'
        resultado_esperado = f"Nome `{name_1}` invalido"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.lookup(name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_pesquisa_phonebook_nome_dolar_nao_permitido(self):
        # Setup
        name_1 = '$'
        number_1 = '0987'
        resultado_esperado = f"Nome `{name_1}` invalido"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.lookup(name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_pesquisa_phonebook_nome_percentual_nao_permitido(self):
        # Setup
        name_1 = '%'
        number_1 = '3461'
        resultado_esperado = f"Nome `{name_1}` invalido"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.lookup(name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_pesquisa_phonebook_de_nome_com_numero_sucesso(self):
        # Setup
        name_1 = 'Pereira'
        number_1 = '4789'
        name_2 = 'Tarcisio'
        number_2 = '263'
        resultado_esperado = f"Numero retornado: `{number_1}` "
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)
        resultado = phonebook.add(name_1, number_2)
        resultado_consulta = phonebook.lookup(name_1)

        # Avaliacao
        assert resultado_esperado == resultado_consulta

    def test_pesquisa_phonebook_de_nome_vazio(self):
        # Setup
        name_1 = None
        number_1 = '674'
        resultado_esperado = "Não é permitido nome vazio"
        phonebook = Phonebook()

        # Chamada
        resultado_consulta = phonebook.lookup(name_1)

        # Avaliacao
        assert resultado_esperado == resultado_consulta

    def test_pesquisa_phonebook_de_nome_inexistente(self):
        # Setup
        name_1 = 'Mari'
        number_1 = '232'
        resultado_esperado = f"Nome `{name_1}` não encontado"
        phonebook = Phonebook()

        # Chamada
        resultado_consulta = phonebook.lookup(name_1)

        # Avaliacao
        assert resultado_esperado == resultado_consulta

    def test_pesquisa_phonebook_de_todos_nomes(self):
        # Setup
        name_1 = 'Jose'
        number_1 = '6785'
        name_2 = 'Dada'
        number_2 = '342'
        resultado_esperado = f"Nomes retornados: `dict_keys(['POLICIA', '{name_1}', '{name_2}'])` "
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)
        resultado = phonebook.add(name_2, number_2)
        resultado_consulta = phonebook.get_names()

        # Avaliacao
        assert resultado_esperado == resultado_consulta

    def test_pesquisa_phonebook_de_todos_numeros(self):
        # Setup
        name_1 = 'Jose'
        number_1 = '6785'
        name_2 = 'Dada'
        number_2 = '342'
        resultado_esperado = f"Nomes retornados: `dict_values(['190', '{number_1}', '{number_2}'])` "
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)
        resultado = phonebook.add(name_2, number_2)
        resultado_consulta = phonebook.get_numbers()

        # Avaliacao
        assert resultado_esperado == resultado_consulta

    def test_pesquisa_phonebook_limpeza_numeros(self):
        # Setup
        name_1 = 'Jose'
        number_1 = '6785'
        name_2 = 'Dada'
        number_2 = '342'
        resultado_esperado = "phonebook limpo"
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)
        resultado = phonebook.add(name_2, number_2)
        resultado_consulta = phonebook.clear()

        # Avaliacao
        assert resultado_esperado == resultado_consulta

    def test_localiza_phonebook_nome_escolhido(self):
        # Setup
        name_1 = 'PEDRO'
        number_1 = '3567'
        name_2 = 'GAL'
        number_2 = '99'
        name_3 = 'JOANA'
        number_3 = '454'
        search_name = 'JOANA'
        resultado_esperado = [{name_3, number_3}]
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)
        resultado = phonebook.add(name_2, number_2)
        resultado = phonebook.add(name_3, number_3)
        resultado_consulta = phonebook.search(search_name)

        # Avaliacao
        assert resultado_esperado == resultado_consulta

    def test_ordenacao_phonebook(self):
        # Setup
        name_1 = 'JOANA'
        number_1 = '3567'
        name_2 = 'GAL'
        number_2 = '99'
        name_3 = 'KAIO'
        number_3 = '876'
        resultado_esperado = {name_2: number_2, name_1: number_1, name_3: number_3, 'POLICIA': '190'}
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)
        resultado = phonebook.add(name_2, number_2)
        resultado = phonebook.add(name_3, number_3)
        resultado_ordenacao = phonebook.get_phonebook_sorted()

        # Avaliacao
        assert resultado_esperado == resultado_ordenacao

    def test_reverse_phonebook(self):
        # Setup
        name_1 = 'JOANA'
        number_1 = '3567'
        name_2 = 'GAL'
        number_2 = '99'
        name_3 = 'KAIO'
        number_3 = '876'
        resultado_esperado = {'POLICIA': '190', name_3: number_3, name_1: number_1, name_2: number_2}
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)
        resultado = phonebook.add(name_2, number_2)
        resultado = phonebook.add(name_3, number_3)
        resultado_ordenacao = phonebook.get_phonebook_reverse()

        # Avaliacao
        assert resultado_esperado == resultado_ordenacao

    def test_phonebook_delete_numero(self):
        # Setup
        name_1 = 'JOANA'
        number_1 = '3567'
        name_2 = 'GAL'
        number_2 = '99'
        name_3 = 'KAIO'
        number_3 = '876'
        resultado_esperado = f"Numero deletado - {number_1} "
        phonebook = Phonebook()

        # Chamada
        resultado = phonebook.add(name_1, number_1)
        resultado = phonebook.add(name_2, number_2)
        resultado = phonebook.add(name_3, number_3)
        resultado_deletado = phonebook.delete(name_1)

        # Avaliacao
        assert resultado_esperado == resultado_deletado