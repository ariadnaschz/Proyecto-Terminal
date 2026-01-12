FROM sagemath/sagemath:9.8

# Instalar utilidades extra (opcional pero recomendado)
RUN sudo apt-get update && sudo apt-get install -y \
    git \
    nano \
    vim

# Establecer directorio de trabajo
WORKDIR /home/sage

# Exponer puerto de Jupyter
EXPOSE 8888

# Instalar JupyterLab compatible (v3.x) dentro de Sage
# Usamos el pip de Sage para mantener el entorno aislado
RUN sage -python -m pip install --no-cache-dir "jupyterlab==3.6.7"