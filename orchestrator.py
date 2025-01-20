import common
import obtaining_data
import autocommits

last_quote = None

def execute_routine():
    global last_quote
    current_quote = obtaining_data.get_dollar_quote()
    common.log_register(f'The current dollar exchange rate: R$ {current_quote:.2f}')
    if last_quote is None or current_quote != last_quote:
        last_quote = current_quote
        repository_path = "C:\\Projetos\\git_duplo\\anabele"
        commit_message = "Log update"
        autocommits.git_commit(repository_path, commit_message)

if __name__ == '__main__':
    execute_routine()