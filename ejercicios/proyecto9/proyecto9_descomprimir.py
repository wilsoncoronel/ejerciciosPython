import shutil
from pathlib import Path
ruta = Path("Proyecto+Dia+9.zip").resolve()
shutil.unpack_archive(ruta,"proyecto9", "zip")
