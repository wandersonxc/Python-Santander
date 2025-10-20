# boletim_modular.py

def cadastrar_aluno():
    """Função para cadastrar um único aluno e retornar um dicionário"""
    nome = input("Digite o nome do aluno: ")
    while True:
        try:
            nota1 = float(input(f"Digite a primeira nota de {nome}: "))
            nota2 = float(input(f"Digite a segunda nota de {nome}: "))
            if not (0 <= nota1 <= 10 and 0 <= nota2 <= 10):
                print("Erro: notas devem estar entre 0 e 10.")
                continue
            break
        except ValueError:
            print("Erro: digite apenas números válidos para as notas.")
    
    media = (nota1 + nota2) / 2
    status = "APROVADO" if media >= 7 else "REPROVADO"
    
    return {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "media": media,
        "status": status
    }

def exibir_boletim(alunos):
    """Função para exibir o boletim completo"""
    print("\nBoletim Completo:")
    for aluno in alunos:
        print(f"Aluno: {aluno['nome']} - Nota 1: {aluno['nota1']}, Nota 2: {aluno['nota2']}, Média: {aluno['media']:.2f}, Status: {aluno['status']}")

def consultar_aluno(alunos):
    """Função para consultar notas de alunos específicos"""
    while True:
        consulta = input("\nDeseja consultar as notas de algum aluno? (S/N): ").strip().upper()
        if consulta == "N":
            break
        
        nome_consulta = input("Digite o nome do aluno: ")
        aluno_encontrado = next((aluno for aluno in alunos if aluno['nome'].lower() == nome_consulta.lower()), None)
        
        if aluno_encontrado:
            print(f"Notas de {aluno_encontrado['nome']}: Nota 1 = {aluno_encontrado['nota1']}, Nota 2 = {aluno_encontrado['nota2']}, Média = {aluno_encontrado['media']:.2f}, Status = {aluno_encontrado['status']}")
        else:
            print("Aluno não encontrado. Tente novamente.")

def resumo_turma(alunos):
    """Função para gerar e exibir o resumo da turma"""
    total_alunos = len(alunos)
    aprovados = sum(1 for aluno in alunos if aluno['media'] >= 7)
    reprovados = total_alunos - aprovados
    media_geral = sum(aluno['media'] for aluno in alunos) / total_alunos
    
    print("\nResumo da turma:")
    print(f"Total de Alunos: {total_alunos}")
    print(f"Aprovados: {aprovados}")
    print(f"Reprovados: {reprovados}")
    print(f"Média geral da turma: {media_geral:.2f}")
    
    return total_alunos, aprovados, reprovados, media_geral

def salvar_boletim(alunos, resumo):
    """Função para salvar boletim em arquivo de texto"""
    total_alunos, aprovados, reprovados, media_geral = resumo
    with open("boletim_modular.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Boletim Completo:\n")
        for aluno in alunos:
            arquivo.write(f"Aluno: {aluno['nome']} - Nota 1: {aluno['nota1']}, Nota 2: {aluno['nota2']}, Média: {aluno['media']:.2f}, Status: {aluno['status']}\n")
        arquivo.write("\nResumo da turma:\n")
        arquivo.write(f"Total de Alunos: {total_alunos}\n")
        arquivo.write(f"Aprovados: {aprovados}\n")
        arquivo.write(f"Reprovados: {reprovados}\n")
        arquivo.write(f"Média geral da turma: {media_geral:.2f}\n")
    print("\nBoletim salvo em 'boletim_modular.txt'.")

# --- PROGRAMA PRINCIPAL ---
def main():
    alunos = []
    
    while True:
        alunos.append(cadastrar_aluno())
        continuar = input("Deseja adicionar outro aluno? (S/N): ").strip().upper()
        if continuar == "N":
            break

    exibir_boletim(alunos)
    consultar_aluno(alunos)
    resumo = resumo_turma(alunos)
    salvar_boletim(alunos, resumo)

# Executa o programa
if __name__ == "__main__":
    main()
