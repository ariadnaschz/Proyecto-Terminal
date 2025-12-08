FROM sagemath/sagemath:latest

# Instalar utilidades extra (opcional pero recomendado)
RUN sudo apt-get update && sudo apt-get install -y \
    git \
    nano \
    vim

# Establecer directorio de trabajo
WORKDIR /home/sage

# Exponer puerto de Jupyter
EXPOSE 8888
