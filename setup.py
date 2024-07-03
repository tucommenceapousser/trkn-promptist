from setuptools import setup, find_packages
import subprocess
import sys

def install_packages():
    packages = [
        "torch",
        "transformers==4.23.1",
        "pytorch_lightning==1.7.7",
        "flask"
    ]

    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'installation de {package}: {e}")
            sys.exit(1)

def main():
    print("Bienvenue dans l'installation de Promptist Demo par TRHACKNON")
    print("Ce script va installer les dépendances nécessaires pour exécuter l'application.")

    while True:
        user_input = input("Souhaitez-vous continuer avec l'installation ? (oui/non): ").strip().lower()
        if user_input in ['oui', 'o', 'yes', 'y']:
            install_packages()
            print("Toutes les dépendances ont été installées avec succès.")
            break
        elif user_input in ['non', 'n', 'no']:
            print("Installation annulée.")
            sys.exit(0)
        else:
            print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")

if __name__ == "__main__":
    main()

setup(
    name="PromptistDemo",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "transformers==4.23.1",
        "pytorch_lightning==1.7.7",
        "flask"
    ],
    entry_points={
        'console_scripts': [
            'install_promptist=setup:main',
        ],
    },
)