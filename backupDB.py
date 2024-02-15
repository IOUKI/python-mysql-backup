import subprocess
import platform

def backup_database(host, user, password, database, output_file):
    # 取得作業系統
    system_platform = platform.system()
    
    # 依照作業系統選擇 mysqldump 命令
    if system_platform == 'Windows':
        mysqldump_cmd = r'C:\Program Files\MySQL\MySQL Server 8.0\bin\mysqldump'
    elif system_platform == 'Linux':
        mysqldump_cmd = '/usr/bin/mysqldump'  # 請確保這是 mysqldump 的實際路徑
    else:
        raise Exception("Unsupported operating system")

    # mysqldump 指令
    command = [
        mysqldump_cmd,
        '-h', host,
        '-u', user,
        f'-p{password}',
        database
    ]
    
    # 執行 mysqldump 命令並將輸出寫入文件
    with open(output_file, 'w') as f:
        subprocess.run(command, stdout=f)

# 設置數據庫連接信息和備份文件路徑
host = ''
user = ''
password = ''
database = ''
output_file = 'backup.sql'

# 執行備份
backup_database(host, user, password, database, output_file)
