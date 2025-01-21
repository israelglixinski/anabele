from datetime import datetime
import subprocess
import os

current_directory = os.path.dirname(os.path.abspath(__file__))    

def git_commit(repo_path, commit_message="Commit automático"):
    try:
        os.chdir(repo_path)
        timestamp           = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        complete_message    = f"{commit_message} - {timestamp}"
        subprocess.run(["git", "add"        , "."                                           ], check=True)
        subprocess.run(["git", "commit"     , "-m"      ,               complete_message    ], check=True)
        subprocess.run(["git", "push"       ,                                               ], check=True)
        subprocess.run(["git", "checkout"   , "main2"   ,                                   ], check=True)
        subprocess.run(["git", "merge"      , "main"    , "-m"      ,   complete_message    ], check=True)
        subprocess.run(["git", "add"        , "."                                           ], check=True)
        subprocess.run(["git", "push"       , "github"  , "main2"   ,                       ], check=True)
        subprocess.run(["git", "checkout"   , "main"    ,                                   ], check=True)
    except Exception as e:
        pass

