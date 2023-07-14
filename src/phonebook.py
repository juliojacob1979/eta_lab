class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """
        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if '#' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '@' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '!' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '$' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '%' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if len(number) == 0:
            msg = 'Numero `{}` invalido'.format(number)
            return msg
        if name not in self.entries:
            self.entries[name] = number
            msg = 'Numero adicionado - `{}` '.format(self.entries[name])
            return msg

    # Bug 1 Linha 17 - na mensagem esta 'Nme' esperava 'Nome'
    # Bug 2 Linha 23 - na mensagem esta 'invalio' esperava 'invalido'
    # Bug 3 Linha 28 - a função usando len não está atendendo a verificação esperada foi ajustada para len(number) == 0
    # Bug 4 Linha 29 - na mensagem esta 'invalid' esperava 'invalido'
    # Refatorado - inclusao da variavel msg contendo melhor complemento da informação enviada ao usuario

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if name is None:
            msg = 'Não é permitido nome vazio'
            return msg
        if '#' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '@' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '!' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '$' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        if '%' in name:
            msg = 'Nome `{}` invalido'.format(name)
            return msg
        for name_pesquisa in self.entries.keys():
            if name_pesquisa == name:
                msg = 'Numero retornado: `{}` '.format(self.entries[name])
                return msg
        msg = 'Nome `{}` não encontado'.format(name)
        return msg

    # Refatorado - Linha 47 foi inserido uma verificação para name vazio
    # Refatorado - inclusao da variavel msg contendo melhor complemento da informação enviada ao usuario
    # Refatorado - Linha 64 ate Linha 67 inserido uma verificação para consulta um name na lista e retorna o numero
    # Bug 1 Linha 51 - na mensagem esta 'invaldo' esperava 'invalido'
    # Bug 2 Linha 57 - na mensagem esta 'Nme' esperava 'Nome'
    # Bug 3 Linha 63 - na mensagem esta 'nvalido' esperava 'invalido'

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        msg = 'Nomes retornados: `{}` '.format(self.entries.keys())
        return msg

    # Refatorado - inclusao da variavel msg contendo melhor complemento da informação enviada ao usuario

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        msg = 'Nomes retornados: `{}` '.format(self.entries.values())
        return msg

    # Refatorado - inclusao da variavel msg contendo melhor complemento da informação enviada ao usuario

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpo'

    # Refatorado Linha 104 - Mensagem alterada de 'limpado' para 'limpo'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():

            if search_name in name:
                result.append({name, number})
        return result

    # Bug 1 Linha 117 - Foi removido o 'not' da função, pois não estava retornando o resultado esperado

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """

        print(self.entries)
        return dict(sorted(self.entries.items()))

    # Refatorado Linha 130 - Foi feito uma validação para que retornasse o phonebook em ordem crescente

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return dict(sorted(self.entries.items(), reverse=True))

    # Refatorado Linha 139 - Foi feito uma validação para que retornasse o phonebook em ordem decrescente

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        msg = 'Numero deletado - {} '.format(self.entries[name])
        self.entries.pop(name)
        return msg

    # Refatorado - inclusao da variavel msg contendo melhor complemento da informação enviada ao usuario
