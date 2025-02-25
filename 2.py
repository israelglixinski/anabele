import subprocess
import os

# Defina a data retroativa desejada
commit_date = "2024-06-01 12:00:00"

# Nome do arquivo a ser criado/modificado
filename = "retro_commit.txt"

# Criar/modificar o arquivo
with open(filename, "w") as file:
    file.write("Este é um commit retroativo em 1º de dezembro de 2024.\n")

# Adicionar o arquivo ao staging
subprocess.run(["git", "add", filename], check=True)

# Criar o commit normal
subprocess.run(["git", "commit", "-m", "Commit retroativo para 01/12/2024"], check=True)

# Alterar a data do commit
subprocess.run([
    "git", "commit", "--amend", "--no-edit",
    "--date", commit_date
], env={**os.environ, "GIT_COMMITTER_DATE": commit_date, "GIT_AUTHOR_DATE": commit_date}, check=True)

# Enviar ao repositório remoto
subprocess.run(["git", "push", "--force"], check=True)

print(f"Commit retroativo para {commit_date} realizado com sucesso!")
