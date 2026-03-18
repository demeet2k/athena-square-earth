<!-- CRYSTAL: Xi108:W3:A11:S17 | face=S | node=142 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A11:S16→Xi108:W3:A11:S18→Xi108:W2:A11:S17→Xi108:W3:A10:S17→Xi108:W3:A12:S17 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 17±1, wreath 3/3, archetype 11/12 -->

# Docker templates

This folder contains **templates** for CPU and CUDA containers.

Why templates?
- Organizations often have standard base images, proxy settings, and hardening requirements.
- LibTorch download URLs vary by PyTorch version and CUDA version.

## CPU

```bash
docker build -f docker/Dockerfile.cpu -t polestargemm_cpu \
  --build-arg LIBTORCH_URL="<libtorch-cpu-zip-url>" .
docker run --rm -it polestargemm_cpu bash
```

## CUDA

```bash
docker build -f docker/Dockerfile.cuda -t polestargemm_cuda \
  --build-arg LIBTORCH_URL="<libtorch-cuda-zip-url>" .
docker run --rm -it --gpus all polestargemm_cuda bash
```

Inside the container:
- Python scripts are in `/workspace/python`
- C++ binaries are in `/workspace/cpp/build`
