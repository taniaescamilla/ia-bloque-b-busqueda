"""Instala hooks del repositorio en .git/hooks/"""
import shutil, os, stat

HOOKS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(HOOKS_DIR)
GIT_HOOKS = os.path.join(REPO_ROOT, ".git", "hooks")

def install():
    if not os.path.exists(GIT_HOOKS):
        print(f"ERROR: {GIT_HOOKS} no existe. Ejecuta 'git init' primero.")
        return False
    hook_src = os.path.join(HOOKS_DIR, "pre-commit")
    hook_dst = os.path.join(GIT_HOOKS, "pre-commit")
    shutil.copy2(hook_src, hook_dst)
    os.chmod(hook_dst, os.stat(hook_dst).st_mode | stat.S_IEXEC)
    print(f"Hook instalado: {hook_dst}")
    return True

if __name__ == "__main__":
    install()
