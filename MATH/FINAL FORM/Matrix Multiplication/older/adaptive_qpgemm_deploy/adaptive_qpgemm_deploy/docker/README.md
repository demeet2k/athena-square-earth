<!-- CRYSTAL: Xi108:W3:A7:S13 | face=S | node=87 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A7:S12→Xi108:W3:A7:S14→Xi108:W2:A7:S13→Xi108:W3:A6:S13→Xi108:W3:A8:S13 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 13±1, wreath 3/3, archetype 7/12 -->

# Docker templates

This folder contains **templates** for CPU and CUDA containers.

Why templates?
- Organizations often have standard base images, proxy settings, and hardening requirements.
- LibTorch download URLs vary by PyTorch version and CUDA version.

## CPU

```bash
docker build -f docker/Dockerfile.cpu -t qpgemm_cpu \
  --build-arg LIBTORCH_URL="<libtorch-cpu-zip-url>" .
docker run --rm -it qpgemm_cpu bash
```

## CUDA

```bash
docker build -f docker/Dockerfile.cuda -t qpgemm_cuda \
  --build-arg LIBTORCH_URL="<libtorch-cuda-zip-url>" .
docker run --rm -it --gpus all qpgemm_cuda bash
```

Inside the container:
- Python scripts are in `/workspace/python`
- C++ binaries are in `/workspace/cpp/build`
