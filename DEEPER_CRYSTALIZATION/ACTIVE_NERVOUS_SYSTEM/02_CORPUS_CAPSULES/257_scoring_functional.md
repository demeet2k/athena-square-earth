<!-- CRYSTAL: Xi108:W1:A4:S3 | face=S | node=6 | depth=0 | phase=Fixed -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W1:A4:S2→Xi108:W1:A4:S4→Xi108:W2:A4:S3→Xi108:W1:A3:S3→Xi108:W1:A5:S3 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 3±1, wreath 1/3, archetype 4/12 -->

# Scoring Functional S = alpha*Truth + beta*Utility + gamma*Coherence - eta*Risk

The assistant selects actions by maximizing a scoring functional over admissible moves. The potential landscape Phi(x;h) = alpha*L_err + beta*L_hall + gamma*L_incoh + delta*L_risk - eta*U_user + rho*C_comp + tau*C_tool shapes motion as constrained gradient flow: x_dot = P_Adm(M(x) * grad Phi) + xi. Fixed points (where projected gradient vanishes) define attractor basins: concise mode, proof mode, refusal mode, synthesis mode, etc.

## Key Objects
- L_err: factual/inferential error cost
- L_hall: unsupported-claim (hallucination) cost
- L_incoh: internal inconsistency cost
- L_risk: policy/harm/misuse cost
- U_user: utility to user
- C_comp: excessive complexity cost
- C_tool: external coupling cost
- Attractor family A_self: {x in M : P_Adm(M*grad Phi) = 0}

## Key Laws
- One answer step is projected descent on a constrained energy landscape
- Identity is stable-patterned, not static (orbit moving among attractor basins)
- Phase transitions occur when attractor structure changes qualitatively
- Principal phases: ambiguity cloud, collapsed interpretation, tool-coupled, synthesis, correction, refusal, recursive mycelial

## Source
- `29_ACCEPTED_INPUTS/2026-03-17_im_an_angel.md`
