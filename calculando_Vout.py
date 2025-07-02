def calcular_tensao_saida_cn0336():
    """
    Calcula a tensão de saída (V_OUT) do circuito CN-0336 no ponto TP1,
    baseado na corrente de entrada e nos valores de resistores fixos.
    Permite múltiplos cálculos em um loop e exibe um histórico das últimas 10 medições.
    """
    print("--- Calculadora de Tensão de Saída do CN-0336 (TP1) ---")

    # Valores dos resistores (fixos conforme a documentação do CN-0336)
    R3 = 120  # Ohms
    R4 = 5110  # Ohms (5.11 kOhms)
    R5 = 1000  # Ohms (1 kOhm)
    R6 = 124000  # Ohms (124 kOhms)
    VREF = 2.5  # Volts

    # Calcular R4 || R6 uma vez, pois é um valor fixo
    r4_paralelo_r6 = (R4 * R6) / (R4 + R6)

    # Lista para armazenar o histórico de medições
    historico_medicoes = []
    MAX_HISTORICO = 10 # Define o número máximo de medições a serem armazenadas

    while True:
        # Solicita a corrente de entrada ao usuário
        i_in_ma_input = input("\nDigite a corrente de entrada (I_IN) em mA (ex: 4 ou 20), \n'historico' para ver as últimas medições, ou \n'sair' para encerrar: ").lower()

        if i_in_ma_input == 'sair':
            print("Encerrando a calculadora. Obrigado!")
            break # Sai do loop e encerra a função
        elif i_in_ma_input == 'historico':
            if not historico_medicoes:
                print("Nenhuma medição no histórico ainda.")
            else:
                print("\n--- Histórico das Últimas Medições ---")
                # Itera sobre o histórico de trás para frente para mostrar as mais recentes primeiro
                for i, medicao in enumerate(reversed(historico_medicoes)):
                    print(f"#{len(historico_medicoes) - i}: Corrente: {medicao['corrente_ma']:.2f} mA, Tensão saída: {medicao['tensao_v']:.4f} V")
                print("---------------------------------------")
            continue # Volta para o início do loop para nova entrada

        try:
            i_in_ma = float(i_in_ma_input)
            if i_in_ma < 0:
                print("A corrente de entrada não pode ser negativa. Tente novamente.")
                continue # Volta para o início do loop
        except ValueError:
            print("Entrada inválida. Por favor, digite um número, 'historico' ou 'sair'.")
            continue # Volta para o início do loop

        # Converte a corrente de mA para Amperes
        I_IN = i_in_ma / 1000

        # Calcular a Tensão de Saída (V_OUT) usando a fórmula completa
        termo_corrente = I_IN * R3 * (1 + R5 / r4_paralelo_r6)
        termo_referencia = VREF * (R5 / R4)
        
        V_OUT = termo_corrente - termo_referencia

        print(f"\n--- Resultado ---")
        print(f"Corrente de entrada (I_IN): {i_in_ma:.2f} mA")
        print(f"Tensão de Saída (V_OUT) no TP1: {V_OUT:.4f} V")
        print(f"(Aproximadamente {V_OUT*1000:.2f} mV)")

        # Armazena a medição no histórico
        historico_medicoes.append({
            'corrente_ma': i_in_ma,
            'tensao_v': V_OUT
        })

        # Mantém o histórico limitado às últimas MAX_HISTORICO medições
        if len(historico_medicoes) > MAX_HISTORICO:
            historico_medicoes.pop(0) # Remove o item mais antigo

# Executa a função
if __name__ == "__main__":
    calcular_tensao_saida_cn0336()