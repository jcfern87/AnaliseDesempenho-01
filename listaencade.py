# Aqui é o arquivo da lista encadeada.

# Esta classe define o Nó, que é o objeto que se junta com outros nós e define uma lista encadeada. Ele contém a sua própria informação (nesse caso, o número) e o endereço do próximo nó, ou o próximo item da lista.
class No:
    def __init__(self, data):
        self.data = data
        self.next = None

# Esta classe define a Lista Encadeada, que vai conter o nó cabeça, que por sua vez contém o endereço do próximo Nó, e assim por diante. A classe contém também as funções adição, remoção, e impressão.
class ListaEncadeada:
    # Define a própria lista e o atributo cabeça, que é o nó inicial da lista.
    def __init__(self):
        self.cabeca = None

    # Define a função de adição, que checa até o último Nó vazio e insere o nó com os dados do parâmetro.
    def adicao(self, data):
        novo_no = No(data)
        if not self.cabeca:
            self.cabeca = novo_no
            return
        last = self.cabeca
        while last.next:
            last = last.next
        last.next = novo_no

    # Define a função que insere um nó em uma posição especificada.
    def inserir_posicao(self, data, posicao):
        novo_no = No(data)
        # Caso o nó a ser inserido seja na pposição zero, ele troca de lugares com o nó cabeça e fecha a função.
        if posicao == 0:
            novo_no.next = self.cabeca
            self.cabeca = novo_no
            return
        # Caso não, continua daqui.
        current = self.cabeca
        contador = 0
        while current and contador < posicao - 1:
            current = current.next
            contador += 1
        if current is None:
            print("Posição fora dos limites")
            return
        novo_no.next = current.next
        current.next = novo_no