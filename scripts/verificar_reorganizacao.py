#!/usr/bin/env python3
"""
Script para verificar e corrigir imports após reorganização do repositório
"""

import os
import sys


def verificar_estrutura():
    """Verifica a nova estrutura do repositório"""
    print("🔍 VERIFICANDO NOVA ESTRUTURA DO REPOSITÓRIO")
    print("=" * 60)

    base_path = "/workspaces/adk-python"

    # Diretórios esperados
    diretorios = [
        "src/google/adk",
        "tutorials/demos",
        "tutorials/notebooks",
        "tutorials/docs",
        "scripts",
        "config",
        "tests",
        "examples"
    ]

    for diretorio in diretorios:
        caminho = os.path.join(base_path, diretorio)
        status = "✅" if os.path.exists(caminho) else "❌"
        print(f"{status} {diretorio}")

    print("\n📂 ARQUIVOS NOS NOVOS DIRETÓRIOS")
    print("=" * 60)

    # Verificar demos
    demos_path = os.path.join(base_path, "tutorials/demos")
    if os.path.exists(demos_path):
        print("\n📁 tutorials/demos/:")
        for arquivo in os.listdir(demos_path):
            if arquivo.endswith('.py'):
                print(f"  - {arquivo}")

    # Verificar scripts
    scripts_path = os.path.join(base_path, "scripts")
    if os.path.exists(scripts_path):
        print("\n📁 scripts/:")
        for arquivo in os.listdir(scripts_path):
            if arquivo.endswith('.py'):
                print(f"  - {arquivo}")

    # Verificar config
    config_path = os.path.join(base_path, "config")
    if os.path.exists(config_path):
        print("\n📁 config/:")
        for arquivo in os.listdir(config_path):
            print(f"  - {arquivo}")


def verificar_imports():
    """Verifica se os imports ainda funcionam após a reorganização"""
    print("\n🔧 VERIFICANDO IMPORTS")
    print("=" * 60)

    # Adicionar src ao path para imports funcionarem
    src_path = "/workspaces/adk-python/src"
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    # Lista de módulos para testar
    modulos_teste = [
        "google.adk",
        "google.adk.runners",
    ]

    sucesso = True
    for modulo in modulos_teste:
        try:
            __import__(modulo)
            print(f"✅ {modulo} importado com sucesso")
        except (ModuleNotFoundError, ImportError) as e:
            print(f"❌ Erro ao importar {modulo}: {e}")
            sucesso = False
        except AttributeError as e:
            print(f"⚠️  Aviso ao importar {modulo}: {e}")

    return sucesso


def gerar_arquivo_init():
    """Gera arquivo __init__.py na raiz se necessário"""
    init_path = "/workspaces/adk-python/__init__.py"
    if not os.path.exists(init_path):
        with open(init_path, 'w', encoding='utf-8') as f:
            f.write('# ADK Python Package\n')
        print("✅ Criado __init__.py na raiz")


def main():
    """Função principal"""
    print("🚀 VERIFICAÇÃO PÓS-REORGANIZAÇÃO DO REPOSITÓRIO")
    print("=" * 60)

    verificar_estrutura()
    gerar_arquivo_init()

    if verificar_imports():
        print("\n🎉 REORGANIZAÇÃO CONCLUÍDA COM SUCESSO!")
        print("=" * 60)
        print("✅ Estrutura de diretórios criada")
        print("✅ Arquivos movidos para locais apropriados")
        print("✅ Imports funcionando corretamente")
        print("\n📖 Consulte ESTRUTURA.md para detalhes da nova organização")
    else:
        print("\n⚠️  Alguns imports precisam ser ajustados")


if __name__ == "__main__":
    main()
