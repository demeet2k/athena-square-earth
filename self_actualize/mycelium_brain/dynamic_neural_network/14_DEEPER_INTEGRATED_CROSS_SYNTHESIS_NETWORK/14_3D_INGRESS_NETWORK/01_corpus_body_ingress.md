<!-- CRYSTAL: Xi108:W3:A9:S21 | face=R | node=219 | depth=3 | phase=Cardinal -->
<!-- METRO: Me -->
<!-- BRIDGES: Xi108:W3:A9:S20→Xi108:W3:A9:S22→Xi108:W2:A9:S21→Xi108:W3:A8:S21→Xi108:W3:A10:S21 -->
<!-- REGENERATE: From this coordinate, adjacent nodes are: shell 21±1, wreath 3/3, archetype 9/12 -->

# Corpus Body Ingress

This surface names the deterministic `3D` body stations that receive atlas traffic
before the traffic is lifted into the canonical basis.

| body_id | corpus body | station_role | ingress line | transfer_hubs | feeds_basis |
| --- | --- | --- | --- | --- | --- |
| `B01` | `self_actualize` | runtime control hub | `Atlas-to-Replay Line` | `AppA,AppH,AppI` | `02,14,15,16` |
| `B02` | `NERVOUS_SYSTEM` | cortex publication hub | `Canonical-Bridge Line` | `AppA,AppI,AppM` | `02,03,15,16` |
| `B03` | `ECOSYSTEM` | governance kernel | `Kernel Line` | `AppA,AppD,AppM` | `02,03,13,15` |
| `B04` | `MATH` | theorem reservoir | `Kernel Line` | `AppB,AppC,AppM` | `03,04,05,06,07,08,09,11,12,13` |
| `B05` | `NERUAL NETWORK` | runtime emergence lab | `Runtime Line` | `AppC,AppF,AppP` | `07,08,10,16` |
| `B06` | `DEEPER CRYSTALIZATION` | manuscript incubator | `Manuscript Line` | `AppE,AppG,AppL` | `01,02,14` |
| `B07` | `Voynich` | text-computer hub | `Manuscript Line` | `AppI,AppL,AppM` | `01,11,12` |
| `B08` | `Trading Bot` | external memory gate | `External Memory Gate Line` | `AppE,AppN,AppP` | `06,08,09` |

All other top-level folders inherit this same schema:

- choose the nearest lawful body station by top-level scope,
- publish transfer hubs and candidate basis refs,
- remain `pressure_gap` only when no lawful basis mapping can be witnessed locally.
