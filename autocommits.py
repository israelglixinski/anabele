from datetime import datetime
import subprocess
import os


current_directory = os.path.dirname(os.path.abspath(__file__))    

def log_register(text=''):
    yyyymmdd = datetime.now().strftime('%Y%m%d')
    datetimestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open(f'{current_directory}\\logs\\autocommits\\{yyyymmdd}', 'a') as file:
        file.write(f'{datetimestamp} - {text}\n')
    pass

log_register('...')

def git_commit_and_push(repo_path, commit_message="Commit automático", branches=["main"]):
    try:
        # Navegar até o repositório
        os.chdir(repo_path)

        # Adicionar todos os arquivos ao stage
        subprocess.run(["git", "add", "."], check=True)

        # Criar o commit com a mensagem fornecida
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        complete_message = f"{commit_message} - {timestamp}"
        subprocess.run(["git", "commit", "-m", complete_message], check=True)

        # Fazer o push para cada branch especificada
        for branch in branches:
            # Certificar-se de que a branch está atualizada localmente
            subprocess.run(["git", "checkout", branch], check=True)
            
            # Realizar o push
            subprocess.run(["git", "push", "origin", branch], check=True)

        print("Commit e push realizados com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar um comando Git: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Caminho para o repositório
repository_path = "C:\\Projetos\\git_duplo\\anabele"

# Mensagem do commit
commit_message = "Atualização do código"

# Branches para fazer o push
branches_to_push = ["main", "main2"]

# Executar o commit e push para várias branches
git_commit_and_push(repository_path, commit_message, branches_to_push)