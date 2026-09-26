# Reading an AlphaSift screening result

The score is a **research queue**, not a return estimate. It helps decide which companies to examine first. The checks and evidence dates tell the analyst whether that priority deserves attention.

## The sequence

1. **Establish the universe.** The dataset stores a company identity even if the sources needed to screen it are unavailable. “Stored” and “screened” are different counts.
2. **Collect observations.** The engine reads financial history, market price and analyst context, and relevant reported holdings. It records the observation date and source; a dataset completion date does not re-date an older filing.
3. **Calculate three point totals.** The active historical method has a Buffett-style quality component (up to 10), a Lynch-style growth-versus-price component (0–10), and a Minervini-style momentum component (−5 to 10). Their sum ranges from −5 to 30.
4. **Assign a research priority.** A total of 20–30 is *Investigate*, 8–19 is *Watch*, and below 8 is *Excluded*. These labels govern the queue only. They are not recommendations or predictions.
5. **Show checks alongside the score.** Individual checks can support, conflict with, or lack enough evidence to evaluate the case. They explain context but do not add points to the three-part score.
6. **Apply the coverage rule.** A stored company counts as screened only if it has a calculated score, evaluated checks, and a classification. A company without those stays *Not evaluated*; missing data is neither a score of zero nor a negative investment verdict.

Consider two fictional records. **Alder Tools** has a score of 22, one evaluated check, and an *Investigate* label. It is screened, but an analyst would still inspect the check's date and any conflicting observations. **Brio Materials** is stored with no calculated score or evaluated checks. It is not screened and has no research-priority label. The [sample snapshot](../data/synthetic-snapshot.json) encodes exactly this distinction.

## Why the checks matter

A favorable score can coexist with weak cash conversion, a balance-sheet concern, or a price signal that has changed since observation. Conversely, a conflicting check does not automatically reverse the stored classification. The intended workflow is **shortlist → inspect the conflicting and missing evidence → compare candidates → record the next research question**.

Data Health supplies a second check on the result. It shows how much of the universe has been evaluated, which sources are current, and whether an update was activated. A successful fetch is only a candidate until it passes validation and the owner reviews its impact. Historical datasets retain the method and evidence stored at the time; the hosted interface does not silently recalculate them.

## Limits of the historical method

The active method preserves legacy missing-data defaults for reproducibility. Missing debt/equity can receive low-debt points, and unknown earnings can be treated as a beat. Those are **known methodological limitations**, not evidence that the underlying company passed a financial test. The analyst should open the company record and inspect the actual inputs before relying on the score.

The accepted 26 September 2026 beta has 1,531 screened companies out of 1,534 stored. Its three unscreened companies lack current-source price history. It has 1,307 companies with fundamental records, but none of those records are marked current after the market-only refresh. This is why the score, the checks, and the source dates must be read together.
