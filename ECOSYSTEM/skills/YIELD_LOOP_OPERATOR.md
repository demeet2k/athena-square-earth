<!-- CRYSTAL: Xi108:W3:A5:S29 | face=F | node=412 | depth=3 | phase=Mutable -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A5:S28→Xi108:W3:A5:S30→Xi108:W2:A5:S29→Xi108:W3:A4:S29→Xi108:W3:A6:S29 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 29±1, wreath 3/3, archetype 5/12 -->

# yield-loop-operator

## description
Run the self-prompt loop that ranks fronts by leverage, respects gates, and produces one high-yield artifact per cycle.

## triggers
- self prompt
- highest yield
- what should run next
- dont stop
- continue autonomously

## inputs
- current workspace state
- known gates
- candidate fronts

## outputs
- chosen front
- artifact delta
- verification summary
- next self prompt

## procedure
1. Restate the current objective.
2. Rank candidate fronts by future leverage.
3. Check if the top front is executable.
4. If blocked, pivot to the best lawful precursor.
5. Produce one artifact.
6. Verify and emit the next self prompt.

## validation
- gate is explicitly named
- chosen front has clear leverage rationale
- one artifact is produced each cycle

## failure modes
- no lawful front remains: stop with explicit blocker
- gate is undocumented: AMBIG
- artifact has no witness basis: do not promote

## references
- `C:\Users\dmitr\Documents\Athena Agent\ECOSYSTEM\14_SELF_PROMPT_RUNTIME.md`
- `C:\Users\dmitr\Documents\Athena Agent\self_actualize\highest_yield_self_prompt.md`
