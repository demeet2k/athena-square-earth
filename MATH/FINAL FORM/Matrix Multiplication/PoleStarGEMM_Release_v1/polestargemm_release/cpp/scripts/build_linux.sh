#!/usr/bin/env bash
# CRYSTAL: Xi108:W1:A4:S11 | face=C | node=402 | depth=0 | phase=Cardinal
# METRO: Sa
# BRIDGES: Xi108:W1:A4:S10→Xi108:W1:A4:S12→Xi108:W2:A4:S11→Xi108:W1:A3:S11→Xi108:W1:A5:S11

set -euo pipefail

# Build helper for Linux/macOS (CPU or CUDA LibTorch).
# Usage:
#   export LIBTORCH=/absolute/path/to/libtorch
#   ./scripts/build_linux.sh
#
# The CMake command uses CMAKE_PREFIX_PATH to find TorchConfig.cmake.

if [[ -z "${LIBTORCH:-}" ]]; then
  echo "ERROR: Please set LIBTORCH to the directory where you extracted libtorch."
  echo "Example: export LIBTORCH=$HOME/libtorch"
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="${ROOT_DIR}/build"

mkdir -p "${BUILD_DIR}"
cd "${BUILD_DIR}"

cmake -DCMAKE_PREFIX_PATH="${LIBTORCH}" -DCMAKE_BUILD_TYPE=Release ..
cmake --build . --config Release -j
echo "[OK] Build finished. Binaries are in: ${BUILD_DIR}"
