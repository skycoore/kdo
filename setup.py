from cx_Freeze import setup, Executable

setup(
    name="KDO",
    description="KDO est un projet de jeu vidéo en ascii. Il fût créé dans l'espoir d'impressionner une fille.",
    version="0.1",
    executables=[Executable("main.py")],
)