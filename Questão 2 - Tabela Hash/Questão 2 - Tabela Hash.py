# QUESTÃO 2 – Tabela Hash - by: Jr Brugnaro

class Node:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.next = None

class HashTable:
    def __init__(self):
        # Implementar a tabela Hash com 10 posições, onde inicialmente todas as posições possuem valor None
        self.table = [None] * 10

    # Implementar a função hash conforme enunciado
    def hash_function(self, sigla):
        if sigla == "DF":
            return 7
        else:
            # Calcular a posição com base nos valores ASCII das duas letras e aplicar MOD 10
            posicao = (ord(sigla[0]) + ord(sigla[1])) % 10
            return posicao

    # Implementar a inserção no início da lista encadeada
    def insert(self, sigla, nomeEstado):
        index = self.hash_function(sigla)
        new_node = Node(sigla, nomeEstado)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            new_node.next = self.table[index]
            self.table[index] = new_node

    # Implementar a impressão da tabela hash
    def print_table(self):
        for i in range(10):
            print(f"Posição {i}: ", end="")
            current = self.table[i]
            while current:
                print(f"{current.sigla} ({current.nomeEstado}) -> ", end="")
                current = current.next
            print("None")

def main():
    estados = [
        ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
        ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
        ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
        ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
        ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
    ]

    estado_ficticio = ("BK", "Estado Fictício")

    hash_table = HashTable()

    # CONSOLE 1 de 3: Imprimir a tabela hash antes de inserir qualquer informação
    print("Tabela Hash antes de inserir qualquer informação:")
    hash_table.print_table()
    print("\n")

    # Inserir os estados e distrito federal na tabela hash
    for sigla, nome in estados:
        hash_table.insert(sigla, nome)

    # CONSOLE 2 de 3: Imprimir a tabela hash após inserir os 26 estados e o Distrito Federal
    print("Tabela Hash após inserir os 26 estados e o Distrito Federal:")
    hash_table.print_table()
    print("\n")

    # Inserir um estado fictício
    hash_table.insert(estado_ficticio[0], estado_ficticio[1])

    # CONSOLE 3 de 3: Imprimir a tabela hash após inserir os 26 estados, Distrito Federal e o estado FICTÍCIO na posição 1
    print("Tabela Hash após inserir os 26 estados, Distrito Federal e o estado fictício:")
    hash_table.print_table()

if __name__ == "__main__":
    main()
