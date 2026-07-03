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
    python3 script.py --platform <nombre_plataforma>
"""

import argparse
import requests
from datetime import datetime
import json
import os


def verificar_dataannotation():
    """Verifica estado de cuenta en DataAnnotation.tech"""
    url = "https://api.dataannotation.tech/v1/user/status"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            status = data.get("status", "desconocido")
            approval_status = data.get("approval_status", "pending")
            return {
                "estado": "activo" if status == "active" and approval_status == "approved" else "inactivo",
                "status": status,
                "approval_status": approval_status,
                "detalle": data
            }
        return {"estado": "error", "status_code": response.status_code}
    except Exception as e:
        return {"estado": "error", "error": str(e)}


def verificar_outlier():
    """Verifica estado de cuenta en Outlier.ai"""
    url = "https://api.outlier.ai/v1/user/profile"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            skills_verified = data.get("skills_verified", False)
            account_status = data.get("account_status", "pending")
            return {
                "estado": "activo" if skills_verified and account_status == "active" else "inactivo",
                "skills_verified": skills_verified,
                "account_status": account_status,
                "detalle": data
            }
        return {"estado": "error", "status_code": response.status_code}
    except Exception as e:
        return {"estado": "error", "error": str(e)}


def verificar_mercor():
    """Verifica estado de cuenta en Mercor"""
    url = "https://api.mercor.com/v1/user/status"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            registration_status = data.get("registration_status", "pending")
            return {
                "estado": "activo" if registration_status == "registered" else "inactivo",
                "registration_status": registration_status,
                "detalle": data
            }
        return {"estado": "error", "status_code": response.status_code}
    except Exception as e:
        return {"estado": "error", "error": str(e)}


def guardar_resultado(plataforma, resultado):
    """Guarda el resultado en un archivo de tracking"""
    timestamp = datetime.now().isoformat()
    filename = "tracking.csv"
    file_exists = os.path.exists(filename)
    
    with open(filename, "a") as f:
        if not file_exists:
            f.write("timestamp,plataforma,estado,detalle\n")
        f.write(f'"{timestamp}","{plataforma}","{resultado.get("estado", "error")}","{json.dumps(resultado)}"\n')


def main():
    parser = argparse.ArgumentParser(description="Automatiza tareas de monetización.")
    parser.add_argument(
        "--platform",
        type=str,
        required=True,
        choices=["DataAnnotation.tech", "Outlier.ai", "Mercor"],
        help="Nombre de la plataforma a verificar"
    )
    args = parser.parse_args()

    platform_mapping = {
        "DataAnnotation.tech": verificar_dataannotation,
        "Outlier.ai": verificar_outlier,
        "Mercor": verificar_mercor,
    }

    verificador = platform_mapping.get(args.platform)
    if not verificador:
        print(f"❌ Plataforma no soportada: {args.platform}")
        return

    print(f"🔍 Verificando plataforma: {args.platform}...")
    resultado = verificador()
    print(f"📊 Resultado: {resultado.get('estado', 'error')}")
    
    if resultado["estado"] != "error":
        guardar_resultado(args.platform, resultado)
        print(f"✅ Resultado guardado en tracking.csv")
    else:
        print(f"⚠️ Error al verificar: {resultado.get('error', f'HTTP {resultado.get(\"status_code\", \"desconocido\")}')}")


if __name__ == "__main__":
    main()
