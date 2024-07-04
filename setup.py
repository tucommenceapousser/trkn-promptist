from setuptools import setup, find_packages
import subprocess
import sys
from colorama import Fore, Style, init, deinit, Back
import random
import string
import os
import re
import questionary
import time
from alive_progress import alive_bar
from banner.banner import fun_prompt, twinkling_text, print_mixed_colors_spider
from termcolor import colored

init(autoreset=True)

fun_prompt()

def install_packages():
    packages = [
        "torch",
        "transformers==4.23.1",
        "pytorch_lightning==1.7.7",
        "flask",
        "colorama",
        "questionary",
        "alive_progress",
        "termcolor"
    ]

    for package in packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'installation de {package}: {e}")
            sys.exit(1)

def main():
    twinkling_text("Installation de Promptist Demo par TRHACKNON", twinkling_duration=4)
    print(colored("Ce script va installer les dépendances nécessaires pour exécuter l'application.", 'cyan'))

    while True:
        user_input = input("Souhaitez-vous continuer avec l'installation ? (oui/non): ").strip().lower()
        if user_input in ['oui', 'o', 'yes', 'y']:
            install_packages()
            print("Toutes les dépendances ont été installées avec succès.")
            break
        elif user_input in ['non', 'n', 'no']:
            print("Installation annulée.")
            subprocess.check_call([sys.executable, "main.py"])
            sys.exit(0)
        else:
            print("Entrée invalide. Veuillez répondre par 'oui' ou 'non'.")

    # Lancer le script main.py après l'installation des dépendances
    subprocess.check_call([sys.executable, "main.py"])

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
        "flask",
        "colorama",
        "questionary",
        "alive_progress",
        "termcolor"
    ],
    entry_points={
        'console_scripts': [
            'install_promptist=setup:main',
        ],
    },
)
