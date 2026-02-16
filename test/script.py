import pathlib from Path

current_dir = Path.cwd()
current_file = Path(__file__).name

print(f"files in {current_dir}:")

for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue
    
    print(f"  - {filepath.name}")

    if filepath.is_file():
        content = filepath.read_text(encode = 'utf-8')
        print(f"  Content : {content}")