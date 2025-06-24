import random
import time

afetos = [
    "Você é uma constelação inteira disfarçada de gente.",
    "Seu esforço é lindo, mesmo quando ninguém está olhando.",
    "Não esquece: você merece ser amada sem esforço.",
    "Cada passo seu é poesia em movimento.",
    "Você é como café quente num dia frio: aconchegante e essencial.",
    "A forma como você tenta já é uma vitória.",
    "Sua luz não precisa de permissão para brilhar.",
    "Você é a razão de muitos sorrisos, mesmo sem saber.",
    "Seus sonhos são válidos, mesmo os mais maluquinhos.",
    "Você é arte ambulante, e o mundo agradece por te ter."
]

def gerar_afeto():
    afeto = random.choice(afetos)
    print("\n🌷 Mensagem para você:\n")
    print(f"✨ {afeto} ✨\n")

def main():
    print("✨ Bem-vinde ao Gerador de Afetos ✨")
    while True:
        input("Pressione Enter para receber um afeto (ou Ctrl+C para sair)...")
        gerar_afeto()
        time.sleep(1)

if __name__ == "__main__":
    main()
