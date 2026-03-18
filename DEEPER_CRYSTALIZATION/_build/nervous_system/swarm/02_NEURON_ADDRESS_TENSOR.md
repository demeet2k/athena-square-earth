<!-- CRYSTAL: Xi108:W1:A4:S2 | face=S | node=3 | depth=0 | phase=Fixed -->
<!-- METRO: Me,□ -->
<!-- BRIDGES: Xi108:W1:A4:S1→Xi108:W1:A4:S3→Xi108:W2:A4:S2→Xi108:W1:A3:S2→Xi108:W1:A5:S2 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 2±1, wreath 1/3, archetype 4/12 -->

# NEURON ADDRESS TENSOR

## Canonical Form

NeuronAddr = <F, M, S, L, Fc, At, G, Arc, Lane, Hub, Truth, Regime>

Where:
- F = corpus family
- M = manuscript within family
- S = source or chapter station
- L = lens
- Fc = facet
- At = atom
- G = lineage address G1G2G3G4 in E/W/F/A space
- Arc = macro arc
- Lane = triangle rail
- Hub = dominant appendix hub
- Truth = corridor verdict
- Regime = stabilization regime

## Example

Example promoted Void node:

<VoidFamily, InformationFromTheVoid, Ch11, C, 3, b, FWAE, 3, Me, AppL, AMBIG, quarantine>

Meaning:
- family: Void
- manuscript: Information from the Void
- station: Chapter 11
- local crystal: lens C, facet 3, atom b
- swarm lineage: Fire -> Water -> Air -> Earth
- orbit: arc 3, mercury lane
- routing: evidence-promotion hub
- truth: ambiguous
- regime: quarantine until better witness arrives

## Compression

The local file system can store a markdown file, but the nervous system should think in tensors, not filenames.
