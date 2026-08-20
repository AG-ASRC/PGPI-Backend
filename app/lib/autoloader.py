from pathlib import Path
from importlib import import_module

def autoloader(app):
    """
    Autoloader load all routes from app/modules or app/customs
    """

    paths = {
        "modules": Path('app/modules'),
        "customs": Path('app/customs'),
    }

    for type, path in paths.items():
        for p in path.iterdir():
            if p.is_dir() and not p.name.startswith("__"):

                routes = import_module(f"app.{type}.{p.name}.routes")

                for router in routes.routers:
                    app.include_router(router)

def modelsAutoloader():
    """
    """

    paths = {
        "modules": Path("app/modules"),
        "customs": Path("app/customs"),
    }

    for category, path in paths.items():
        for p in path.iterdir():

            if p.is_dir() and not p.name.startswith("__"):
                import_module(f"app.{category}.{p.name}.models")