Para calcular a tensão de saída (VOUT) no ponto TP1 do CN-0336, que é a saída do amplificador operacional U1A, 
precisamos considerar a contribuição da corrente de entrada e da tensão de referência. A fórmula fornecida no 
documento para a função de transferência é:

Vout = I in × R3 ×(1+ R5/R4 ∣∣ R6 )−VREF × R5/R4
​
Onde:

I in​ : é a corrente de entrada (em Amperes).

R3 :é o resistor de conversão de corrente para tensão (120 Ω).

R4, R5 e R6 :são os resistores na rede de realimentação do amplificador operacional.

R4 = 5.11kΩ=5110Ω 
R5 =1kΩ=1000Ω 
R6 =124kΩ=124000Ω 

VREF é a tensão de referência, que é de 2.5 V.

R4 ∣∣ R6 representa o paralelo de R4 e R6
​, calculado por:
 R4∣∣[cite start]R6= R4+R6 R4×R6
​≈4907.75Ω
 
​
 

​
