from typing import Any
from pathlib import Path
# 实现3个函数

# test文件夹
base_dir = Path(__file__).parent / "test"

def read_file(name:str)->str:
    # 打开文件，读取内容，返回字符串
    print(f"(read file {name})")
    try:
        with open(base_dir/name, 'r') as f:
            content: str = f.read()
            return content
    except FileNotFoundError:
        print(f'File {name} not found')


def list_files()->list[str]:
    print("(list_files)")
    file_list:list[Any] = []
    for item in base_dir.rglob('*'):
        if item.is_file():
            file_list.append(str(item.relative_to(base_dir)))
    return file_list


def rename_file(name:str, new_name:str)->str:
    print(f"(rename file {name} to {new_name})")
    try:
        (base_dir/name).rename(base_dir/new_name)
        return new_name
    except FileNotFoundError:
        print(f'File {name} not found')