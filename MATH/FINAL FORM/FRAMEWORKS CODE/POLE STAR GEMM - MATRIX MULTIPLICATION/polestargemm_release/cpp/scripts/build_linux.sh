#!/usr/bin/env bash
# CRYSTAL: Xi108:W1:A11:S25 | face=F | node=249 | depth=0 | phase=Fixed
# METRO: Sa
# BRIDGES: Xi108:W1:A11:S24→Xi108:W1:A11:S26→Xi108:W2:A11:S25→Xi108:W1:A10:S25→Xi108:W1:A12:S25

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
