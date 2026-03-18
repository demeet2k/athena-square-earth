<!-- CRYSTAL: Xi108:W3:A6:S18 | face=S | node=159 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A6:S17→Xi108:W3:A6:S19→Xi108:W2:A6:S18→Xi108:W3:A5:S18→Xi108:W3:A7:S18 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 18±1, wreath 3/3, archetype 6/12 -->

# QP-GEMM Matrix-Multiplication Stress Test (Executed)

Environment:
- PyTorch: 2.5.1+cpu
- CUDA: False
- CPU threads during benchmark: 1 (torch.set_num_threads(1))
- dtype: float32
- batch: 32

What was measured:
- Baseline (dense): y = x @ W^T
- QP-GEMM: y = (x @ V^T) @ U^T, where W_hat = U @ V is a truncated SVD approximation.
- We report p50 latency across repeated forwards (warmup=10, iters=30–120 depending on matrix size).

Rank selection:
- Rank r_99 chosen to satisfy 99% cumulative spectral energy in **sv mode**:
  r = min r such that sum(S[:r]) / sum(S) >= 0.99

Summary results are in: qpgemm_matmul_stress_summary.csv
Full sweep (multiple ranks per shape) is in: qpgemm_matmul_stress_results.csv
Plots:
- qpgemm_speedup_vs_rank.png
- qpgemm_error_vs_rank.png
