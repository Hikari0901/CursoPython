from pathlib import Path, PureWindowsPath

carpeta = Path('F:\\Ronnald\\Documents\\Curso Python\\32-archivos\\otra carpeta')
ruta_windows= PureWindowsPath(carpeta)
print(ruta_windows)

if not carpeta.exists():
    print("Este archivo no existe")
else:
    print("Genial, existe")