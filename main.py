# Classe que representa um autômato finito para o comportamento de um veículo autônomo
class AutomatoVeiculoAutonomo:
    def __init__(self):
        # Estado inicial do autômato
        self.estado_inicial = "Desligado"
        self.estado_atual = self.estado_inicial

        # Estados finais válidos
        self.estados_finais = {"DestinoAlcancado"}

        # Dicionário de transições: (estado_atual, entrada) -> novo_estado
        self.transicoes = {
            ("Desligado", "Ligar"): "Ligado",
            ("Ligado", "DetectaRua"): "InicializandoSensores",
            ("InicializandoSensores", "DetectaRua"): "ProntoParaRodar",
            ("ProntoParaRodar", "Avancar"): "Rodando",
            ("Rodando", "DetectaSemaforoVermelho"): "ParadoSemaforo",
            ("ParadoSemaforo", "DetectaSemaforoVerde"): "Avancando",
            ("Avancando", "Avancar"): "Rodando",
            ("Rodando", "ObstaculoDetectado"): "ParadoObstaculo",
            ("ParadoObstaculo", "ObstaculoLivre"): "DesviandoObstaculo",
            ("DesviandoObstaculo", "Avancar"): "Rodando",
            ("Rodando", "CurvaEsquerda"): "CurvandoEsquerda",
            ("CurvandoEsquerda", "Avancar"): "Rodando",
            ("Rodando", "CurvaDireita"): "CurvandoDireita",
            ("CurvandoDireita", "Avancar"): "Rodando",
            ("Rodando", "ReduzirVelocidade"): "ReduzindoVelocidade",
            ("ReduzindoVelocidade", "Avancar"): "Rodando",
            ("Rodando", "DestinoAlcancado"): "DestinoAlcancado"
        }

    # Processa uma lista de entradas (fita) e retorna as transições realizadas e se foi aceita
    def processar_entrada(self, fita):
        self.estado_atual = self.estado_inicial  # Reinicia o estado
        transicoes_realizadas = []  # Lista para armazenar o histórico de transições

        for simbolo in fita:
            chave = (self.estado_atual, simbolo)
            if chave in self.transicoes:
                # Transição válida
                proximo_estado = self.transicoes[chave]
                transicoes_realizadas.append(f"({self.estado_atual}, {simbolo}) ⇒ {proximo_estado}")
                self.estado_atual = proximo_estado
            else:
                # Transição inválida
                transicoes_realizadas.append(f"({self.estado_atual}, {simbolo}) ⇒ transição inválida!")
                return transicoes_realizadas, False  # Rejeita a entrada

        # Aceita se o estado final for um dos estados aceitos
        return transicoes_realizadas, self.estado_atual in self.estados_finais


# Instancia o autômato
automato = AutomatoVeiculoAutonomo()

# Teste 1: sequência válida completa com curva à esquerda, obstáculo e semáforo
entrada1 = [
    "Ligar", "DetectaRua", "DetectaRua", "Avancar", "DetectaSemaforoVermelho", 
    "DetectaSemaforoVerde", "Avancar", "ObstaculoDetectado", "ObstaculoLivre", 
    "Avancar", "CurvaEsquerda", "Avancar", "ReduzirVelocidade", "Avancar", 
    "DestinoAlcancado"
]
resultado1, aceita1 = automato.processar_entrada(entrada1)

# Teste 2: sequência inválida (pula o estado "DetectaRua" após ligar)
entrada2 = ["Ligar", "Avancar", "DestinoAlcancado"]
resultado2, aceita2 = automato.processar_entrada(entrada2)

# Teste 3: sequência alternativa válida com curva à direita
entrada3 = [
    "Ligar", "DetectaRua", "DetectaRua", "Avancar", "CurvaDireita", "Avancar", 
    "ReduzirVelocidade", "Avancar", "DestinoAlcancado"
]
resultado3, aceita3 = automato.processar_entrada(entrada3)

# Teste 4: sequência inválida (detecta semáforo verde sem antes o vermelho)
entrada4 = [
    "Ligar", "DetectaRua", "DetectaRua", "Avancar", "DetectaSemaforoVerde", 
    "Avancar", "DestinoAlcancado"
]
resultado4, aceita4 = automato.processar_entrada(entrada4)

# Impressão dos resultados dos testes
print("Resultado 1:", *resultado1, sep="\n")
print("Aceita 1:", aceita1)

print("\nResultado 2:", *resultado2, sep="\n")
print("Aceita 2:", aceita2)

print("\nResultado 3:", *resultado3, sep="\n")
print("Aceita 3:", aceita3)

print("\nResultado 4:", *resultado4, sep="\n")
print("Aceita 4:", aceita4)
