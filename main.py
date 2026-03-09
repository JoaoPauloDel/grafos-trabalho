from grafos import grafos
import teoremas

def executar_analise():
    print(f"{'Grafo':<10} | {'Dirac':<8} | {'Ore':<8} | {'Bondy & Chvátal'}")
    print("-" * 50)

    for nome, estrutura in grafos.items():
        res_dirac = "Sim" if teoremas.verificar_dirac(estrutura) else "Não"
        res_ore = "Sim" if teoremas.verificar_ore(estrutura) else "Não"
        res_bc = "Sim" if teoremas.verificar_bondy_chvatal(estrutura) else "Não"

        print(f"{nome:<10} | {res_dirac:<8} | {res_ore:<8} | {res_bc}")

if __name__ == "__main__":
    executar_analise()