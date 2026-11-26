#Aqui vou desemvolver meu código de teste para a prova.

# Lista global (array) para armazenar os motores em memória
motores = []


def exibir_menu():
    print("\n" + "=" * 35)
    print("   SISTEMA DE CADASTRO DE MOTORES")
    print("=" * 35)
    print("1. Cadastrar novo motor")
    print("2. Listar todos os motores")
    print("3. Buscar motor por número de série")
    print("4. Atualizar dados de um motor")
    print("5. Remover motor")
    print("0. Sair")
    print("=" * 35)


def cadastrar_motor():
    print("\n--- NOVO CADASTRO ---")
    numero_serie = input("Número de série (ID único): ").strip()

    # Verifica se já existe um motor com o mesmo número de série
    for motor in motores:
        if motor["numero_serie"] == numero_serie:
            print("Erro: Já existe um motor cadastrado com este número de série.")
            return

    fabricante = input("Fabricante (ex: WEG, Siemens): ").strip()
    modelo = input("Modelo: ").strip()
    potencia = input("Potência (ex: 5 CV, 10 kW): ").strip()
    tensao = input("Tensão (ex: 220V/380V): ").strip()
    rpm = input("Rotação (RPM): ").strip()

    novo_motor = {
        "numero_serie": numero_serie,
        "fabricante": fabricante,
        "modelo": modelo,
        "potencia": potencia,
        "tensao": tensao,
        "rpm": rpm,
    }

    motores.append(novo_motor)
    print(f"Motor '{modelo}' (Série: {numero_serie}) cadastrado com sucesso!")


def listar_motores():
    print("\n--- LISTA DE MOTORES CADASTRADOS ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    for i, m in enumerate(motores, start=1):
        print(
            f"{i}. [Série: {m['numero_serie']}] {m['fabricante']} - {m['modelo']} | "
            f"Potência: {m['potencia']} | Tensão: {m['tensao']} | {m['rpm']} RPM"
        )


def buscar_motor():
    print("\n--- BUSCAR MOTOR ---")
    serie = input("Digite o número de série: ").strip()

    for m in motores:
        if m["numero_serie"] == serie:
            print("\nMotor encontrado:")
            print(f"  Número de Série: {m['numero_serie']}")
            print(f"  Fabricante:      {m['fabricante']}")
            print(f"  Modelo:          {m['modelo']}")
            print(f"  Potência:        {m['potencia']}")
            print(f"  Tensão:          {m['tensao']}")
            print(f"  Rotação:         {m['rpm']} RPM")
            return

    print("Motor não encontrado.")


def atualizar_motor():
    print("\n--- ATUALIZAR MOTOR ---")
    serie = input("Digite o número de série do motor a atualizar: ").strip()

    for m in motores:
        if m["numero_serie"] == serie:
            print("Deixe em branco para manter o valor atual.")

            novo_fab = input(f"Fabricante [{m['fabricante']}]: ").strip()
            novo_mod = input(f"Modelo [{m['modelo']}]: ").strip()
            nova_pot = input(f"Potência [{m['potencia']}]: ").strip()
            nova_ten = input(f"Tensão [{m['tensao']}]: ").strip()
            novo_rpm = input(f"Rotação RPM [{m['rpm']}]: ").strip()

            if novo_fab:
                m["fabricante"] = novo_fab
            if novo_mod:
                m["modelo"] = novo_mod
            if nova_pot:
                m["potencia"] = nova_pot
            if nova_ten:
                m["tensao"] = nova_ten
            if novo_rpm:
                m["rpm"] = novo_rpm

            print("Dados do motor atualizados com sucesso!")
            return

    print("Motor não encontrado.")


def remover_motor():
    print("\n--- REMOVER MOTOR ---")
    serie = input("Digite o número de série do motor a remover: ").strip()

    for i, m in enumerate(motores):
        if m["numero_serie"] == serie:
            confirmacao = (
                input(f"Tem certeza que deseja remover o motor {m['modelo']}? (s/n): ")
                .strip()
                .lower()
            )
            if confirmacao == "s":
                motores.pop(i)
                print("Motor removido com sucesso.")
            else:
                print("Operação cancelada.")
            return

    print("Motor não encontrado.")


def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            buscar_motor()
        elif opcao == "4":
            atualizar_motor()
        elif opcao == "5":
            remover_motor()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()