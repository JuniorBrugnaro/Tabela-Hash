# Classe Nodo representa um cartão numerado contendo: número, cor e um ponteiro para o próximo
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

# Classe ListaEncadeadaSimples contém um ponteiro para a cabeça da lista (head)
class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None
    
    # Função inserirSemPrioridade(nodo) insere o nodo no final da lista
    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo
    
    # Função inserirComPrioridade(nodo) insere o nodo após todos os nodos com cor “A” que estão na lista
    def inserirComPrioridade(self, nodo):
        if self.head is None or self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo
    
    # Função inserir() solicita ao usuário a cor e o número, cria um nodo e insere na lista conforme prioridade
    def inserir(self):
        cor = input("Digite a cor do cartão (A para amarelo, V para verde): ").strip().upper()
        numero = int(input("Digite o número do cartão: "))
        novo_nodo = Nodo(numero, cor)
        
        if self.head is None:
            self.head = novo_nodo
        elif cor == 'V':
            self.inserirSemPrioridade(novo_nodo)
        elif cor == 'A':
            self.inserirComPrioridade(novo_nodo)
    
    # Função imprimirListaEspera() imprime todos os cartões e seus respectivos números a partir do primeiro até o último da lista
    def imprimirListaEspera(self):
        if self.head is None:
            print("A lista está vazia.")
        else:
            atual = self.head
            while atual:
                print(f"Cartão {atual.cor} {atual.numero}")
                atual = atual.proximo
    
    # Função atenderPaciente() remove os dois primeiros pacientes da fila e imprime uma mensagem chamando-os para atendimento
    def atenderPaciente(self):
        if self.head is None:
            print("Nenhum paciente na fila.")
        elif self.head.proximo is None:
            paciente = self.head
            self.head = self.head.proximo
            print(f"Chamando paciente com cartão {paciente.cor} {paciente.numero} para atendimento.")
        else:
            paciente1 = self.head
            paciente2 = self.head.proximo
            self.head = self.head.proximo.proximo
            print(f"Chamando paciente com cartão {paciente1.cor} {paciente1.numero} para atendimento.")
            print(f"Chamando paciente com cartão {paciente2.cor} {paciente2.numero} para atendimento.")
    
    # Função menu apresenta as opções de interação com o sistema
    def menu(self):
        while True:
            print("\nMenu:")
            print("1 – Adicionar paciente a fila")
            print("2 – Mostrar pacientes na fila")
            print("3 – Chamar pacientes")
            print("4 – Sair")
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == '1':
                self.inserir()
            elif opcao == '2':
                self.imprimirListaEspera()
            elif opcao == '3':
                self.atenderPaciente()
            elif opcao == '4':
                print("Encerrando o programa.")
                break
            else:
                print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")

# Execução do programa
fila = ListaEncadeadaSimples()
fila.menu()
