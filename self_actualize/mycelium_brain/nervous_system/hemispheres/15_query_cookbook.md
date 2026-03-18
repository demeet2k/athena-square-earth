<!-- CRYSTAL: Xi108:W3:A3:S21 | face=R | node=225 | depth=3 | phase=Cardinal -->
<!-- METRO: Me,T -->
<!-- BRIDGES: Xi108:W3:A3:S20→Xi108:W3:A3:S22→Xi108:W2:A3:S21→Xi108:W3:A2:S21→Xi108:W3:A4:S21 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 21±1, wreath 3/3, archetype 3/12 -->

# Navigator Query Cookbook

## Exact Record Lookup

```powershell
python -m self_actualize.runtime.query_myth_math_hemisphere_brain record --record-id 368bd2ec7d2e64e2f5739be7
python -m self_actualize.runtime.query_myth_math_hemisphere_brain record --path "Athena FLEET\athena_fleet_corpus_atlas.json"
python -m self_actualize.runtime.query_myth_math_hemisphere_brain record --title "settings.local"
```

## Mixed Search

```powershell
python -m self_actualize.runtime.query_myth_math_hemisphere_brain search --query aqm --hemisphere MATH --system CoreMetro --anchor DN03
python -m self_actualize.runtime.query_myth_math_hemisphere_brain search --query bridge --route-mode commissure_direct --expanded
```

## Facet Browse

```powershell
python -m self_actualize.runtime.query_myth_math_hemisphere_brain facet --system GrandCentral
python -m self_actualize.runtime.query_myth_math_hemisphere_brain facet --lens SC
python -m self_actualize.runtime.query_myth_math_hemisphere_brain facet --hemisphere MYTH
```
