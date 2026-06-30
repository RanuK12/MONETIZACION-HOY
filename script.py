#!/usr/bin/env python3
"""
Script para automatizar tareas de monetización.

Autor: Ranukita
Versión: 0.1

Este script automatiza la verificación de plataformas de monetización como:
- DataAnnotation.tech
- Outlier.ai
- Mercor

Uso:
    python script.py --platform <nombre_plataforma>
"""

import argparse


def main():
    parser = argparse.ArgumentParser(description="Automatiza tareas de monetización.")
    parser.add_argument("--platform", type=str, required=True, help="Nombre de la plataforma a verificar")
    args = parser.parse_args()

    print(f"¡Hola! Verificando plataforma: {args.platform}")
    print("Ejemplo: DataAnnotation, Outlier.ai, Mercor")


if __name__ == "__main__":
    main()
