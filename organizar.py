import os

# Lista das suas matérias (Você pode mudar os nomes aqui)
materias = ['Algoritmos_em_C', 'Intro_Sistemas_Informacao', 'Logica_Python', 'Projetos_GitHub']

def criar_pastas():
    # Pega o local onde o script está
    diretorio_atual = os.getcwd()
    
    print(f"Organizando pastas em: {diretorio_atual}")
    
    for materia in materias:
        if not os.path.exists(materia):
            os.makedirs(materia)
            print(f"✅ Pasta [{materia}] criada com sucesso!")
        else:
            print(f"⚠️ A pasta [{materia}] já existe.")

if __name__ == "__main__":
    criar_pastas()
