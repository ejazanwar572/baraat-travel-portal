# Lessons & Pattern Prevention

## 1. Indian Railways Coach Numbering vs Class
- **Pattern**: Dot-matrix printed counter tickets for Class **3A (Third AC)** print coach designations starting with **B** (e.g., `B1`, `B2`, `B3`). Because dot-matrix fonts render `B` with faint vertical bars, visual OCR can misread `B2` as `M2`.
- **Rule**:
  - Class **3A (Third AC)** has coaches: `B1`, `B2`, `B3`, etc.
  - Class **3E (Third AC Economy)** has coaches: `M1`, `M2`, `M3`, etc.
  - Whenever inspecting printed tickets, cross-verify the Class column: if Class is `3A`, a coach starting with `M` is invalid; it is `B` (e.g. `B2`). Always verify against live CRIS / IRCTC PNR API records when PNR is known.
