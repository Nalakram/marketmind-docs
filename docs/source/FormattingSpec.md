

<!-- MM:BEGIN:TITLEPAGE -->
Version 1.0.4 · April 2026 · Proprietary

Companion documents: Implementation Plan v6.5.9 · Technical Roadmap v1.4.30 · Meta-Learning Core v1.2.25 · Meta-Learning Architecture Vision v1.3.6 · Resolution Ledger v1.0.52 · README.md 7.2.2 · VERSION.md 7.2.2
<!-- MM:END:TITLEPAGE -->

# MarketMind · DOCX Formatting Specification

<!--
  DOC_ID:           MarketMind_Formatting_Spec
  VERSION:          1.0.4
  LAST_UPDATED:     2026-04-01
  MAINTAINER:       Mark Wuenschel / MindForgeLabs
  STATUS:           ACTIVE
  CHANGELOG:
    1.0.4 — Companion-sync: title page and companion references aligned to the
              4.18.5 suite baseline (Implementation Plan 6.4.26 / Technical
              Roadmap 1.4.21 / Core 1.2.19 / Architecture Vision 1.2.20 /
              Resolution Ledger 1.0.21 / README 4.18.5 / VERSION 4.18.5).
    1.0.3 — Companion-sync: title page and companion references aligned to the
              4.18.1 suite baseline (Implementation Plan 6.4.24 / Technical
              Roadmap 1.4.21 / Core 1.2.19 / Architecture Vision 1.2.20 /
              Resolution Ledger 1.0.20 / README 4.18.1 / VERSION 4.18.1).
    1.0.2 — F-2 planning-surface sync: title page, §3 table, and footer aligned to
              VERSION.md 4.9.0 and suite doc versions 6.4.14 / 1.4.15 / 1.2.13 / 1.2.14 / 1.0.6 / README 4.9.0.
    1.0.1 — Phase I-F-1 companion sync: title page, §3 table, and footer aligned to
              VERSION.md 4.8.0 and suite doc versions 6.4.13 / 1.4.14 / 1.2.13 / 1.2.14 / 1.0.5 / README 4.2.9.
    1.2.0 — Added machine-readable Markdown edition (this file).
              Source of truth remains the HTML print edition for rendered output.
    1.1.0 — Added §6 Resolution Ledger Color System (entry type identity,
              lifecycle state, phase heat, dashboard tinting, evidence pills).
              Version bump and date update on title page.
    1.0.0 — Initial release.
-->

**MindForgeLabs · Confidential & Proprietary**
Version 1.0.4 · April 2026

Companion to: Implementation Plan v6.4.34 · Technical Roadmap v1.4.21 · Meta-Learning Core v1.2.19 · Meta-Learning Architecture Vision v1.2.23 · Resolution Ledger v1.0.44 · README.md 4.18.34 · VERSION.md 4.18.34

---

## Contents

1. [Title Page Layout](#1-title-page-layout)
2. [Page Structure & Table of Contents](#2-page-structure--table-of-contents)
3. [Per-Document Title Page Content](#3-per-document-title-page-content)
4. [Typography & Layout](#4-typography--layout)
5. [Callout Block Reference](#5-callout-block-reference)
   - [5.1 Reference Table — Callout Blocks](#51-reference-table--callout-blocks)
   - [5.2 Color System Rationale & Badge Systems](#52-color-system-rationale--badge-systems)
   - [5.3 Live Examples](#53-live-examples)
6. [Resolution Ledger Color System](#6-resolution-ledger-color-system)
   - [6.1 Entry Type Identity](#61-entry-type-identity)
   - [6.2 Lifecycle State & Status Badges](#62-lifecycle-state--status-badges)
   - [6.3 Phase Heat & Section Banners](#63-phase-heat--section-banners)
   - [6.4 Dashboard Heat Tinting](#64-dashboard-heat-tinting)
   - [6.5 Evidence Pills & Inline Elements](#65-evidence-pills--inline-elements)

---

## 1. Title Page Layout

Every document opens with a full-bleed two-column title page (page 1). Zero page margins; the sidebar bleeds to all edges. No page number on this page.

| Zone | Specification |
|---|---|
| MarketMind wordmark | IM Fell English (print) / Aptos Serif (DOCX) · 40–44pt · `#1F3864` |
| Sub-label | DM Mono / Consolas · 7.5–8pt · `#8AACBF` · wide letter-spacing |
| Horizontal rule | Border-bottom · 1.5pt · `#0EA5E9` |
| Document title | Crimson Pro / Aptos Serif · 18–19pt · bold/600 · `#1F3864` |
| Description | 10–10.5pt · italic · `#5A7088` · 1–2 lines |
| Audience | 10pt · italic · `#7A9AAA` |
| Companion line | DM Mono / Consolas · 7.5pt · `#9ABACC` |
| Visual motif | Per-document SVG watermark, lower-right quadrant. Formatting Spec: none. |
| Sidebar | `#071020` bg · 20% page width · right border `#1A4A6B` · Consolas metadata |
| Page break | Explicit break after title page — never blank paragraphs |

### Sidebar metadata fields

| Key | Content |
|---|---|
| Version | Document version (e.g. `1.2.0`) |
| Date | ISO date of last update (e.g. `2026-03-20`) |
| Author | `Mark Wuenschel` |
| Org | `MindForgeLabs` |
| Class. | `Confidential` |

Sidebar key style: DM Mono 6.5pt · `#38BDF8` · uppercase · wide letter-spacing.
Sidebar value style: DM Mono 8.5pt weight 500 · `#CDE8FA`.
Background: `#071020` with 18px grid texture at 4% opacity.

---

## 2. Page Structure & Table of Contents

All documents follow a fixed three-zone layout. Page breaks are explicit `PageBreak` elements throughout — never blank paragraphs.

| Page | Content | Implementation notes |
|---|---|---|
| 1 | Title page | Full-bleed sidebar + content area. No page number. |
| 2 | Table of Contents | `docx TableOfContents` · `hyperlink:true` · `headingStyleRange "1-3"`. H1 entries: bold. H2: indent 360 DXA. H3: indent 720 DXA. Dot-leader page numbers. Title "Contents" 16pt bold `#1F3864`. |
| 3+ | Body content | H1/H2/H3 headings and body paragraphs. Page numbers restart Arabic 1. Running header: doc name left · "MarketMind" right. |

---

## 3. Per-Document Title Page Content

Canonical reference for each companion document. Description and audience text: 10pt italic Aptos Serif / Crimson Pro. Companion line: 7.5pt Consolas / DM Mono `#9ABACC`.

| Document | Title & description | Audience | Companions · Motif |
|---|---|---|---|
| Technical Roadmap v1.4.15 | **Technical Roadmap & Feature Plan** — *Strategic build order, research sequencing, and go/no-go checkpoints* | Internal engineering, technical stakeholders | Implementation Plan v6.4.14 · README v4.9.0 · Meta-Learning Core v1.2.13 · Meta-Learning Architecture Vision v1.2.14 · Resolution Ledger v1.0.6 · VERSION.md 4.9.0 — *Motif: TBD* |
| Implementation Plan v6.4.14 | **Implementation Plan & Execution Roadmap** — *Execution plan for the governed substrate and the validation-gated meta-learning program* | Internal engineering, technical stakeholders | Technical Roadmap v1.4.15 · README v4.9.0 · Meta-Learning Core v1.2.13 · Meta-Learning Architecture Vision v1.2.14 · Resolution Ledger v1.0.6 · VERSION.md 4.9.0 — *Motif: TBD* |
| README v4.9.0 | **Algorithmic Trading Platform** — *README & Technical Overview* | Internal engineering, onboarding, technical stakeholders | Implementation Plan v6.4.14 · Technical Roadmap v1.4.15 · Meta-Learning Core v1.2.13 · Meta-Learning Architecture Vision v1.2.14 · Resolution Ledger v1.0.6 · VERSION.md 4.9.0 — *Motif: TBD* |
| Meta-Learning Core v1.2.13 | **Meta-Learning Core** — *Research supplement — empirical validation program, task contracts, and acceptance hierarchy* | Internal engineering, technical stakeholders | Technical Roadmap v1.4.15 · Implementation Plan v6.4.14 · Meta-Learning Architecture Vision v1.2.14 · Resolution Ledger v1.0.6 · README v4.9.0 · VERSION.md 4.9.0 — *Motif: Node network (neural/graph topology)* |
| Meta-Learning Architecture Vision v1.2.14 | **Meta-Learning Architecture Vision** — *Runtime shape, interface contracts, and validation-gated defaults* | Internal engineering, technical stakeholders | Meta-Learning Core v1.2.13 · Technical Roadmap v1.4.15 · Implementation Plan v6.4.14 · Resolution Ledger v1.0.6 · README v4.9.0 · VERSION.md 4.9.0 — *Motif: TBD* |
| Resolution Ledger v1.0.6 | **Resolution Ledger** — *Canonical registry of blockers, normative locks, gates, and research/program dependencies* | Internal engineering, technical stakeholders | Implementation Plan v6.4.14 · Technical Roadmap v1.4.15 · Meta-Learning Core v1.2.13 · Meta-Learning Architecture Vision v1.2.14 · README v4.9.0 · VERSION.md 4.9.0 — *Motif: none* |

---

## 4. Typography & Layout

All body and heading text uses Aptos Serif (DOCX) / Crimson Pro (print). The sidebar and companion lines use Consolas (DOCX) / DM Mono (print). Callout blocks are single-cell tables with a 1.5pt left accent border. Font column omitted — Aptos Serif throughout except Code (Consolas / DM Mono).

| Element | Size | Color / fill | Notes |
|---|---|---|---|
| **Page** | — | US Letter 8.5″×11″ | 1″ margins (body); 0 margins (title page) |
| H1 | 16pt bold | `#1F3864` | outlineLevel 0; spacing before/after 240/240 |
| H2 | 13pt bold | `#1F3864` | outlineLevel 1; spacing 200/160 |
| H3 | 11pt bold | `#2E5496` | outlineLevel 2; spacing 160/100 |
| Body text | 11pt | `#000000` | Default paragraph style |
| Bold inline | 11pt bold | Inherits | `**text**` → TextRun bold:true |
| Italic inline | 11pt italic | Inherits | `*text*` → TextRun italics:true |
| Table header row | 9pt bold | `#FFFFFF` on `#1F3864` | ShadingType.CLEAR fill `#1F3864` |
| Table body row | 9pt | `#000000` on `#FFFFFF` | Borders `#CCCCCC` all sides |
| Sidebar key | 7pt · Consolas | `#38BDF8` | Wide letter-spacing; bg `#071020` |
| Sidebar value | 8.5pt · Consolas | `#CDE8FA` | Bold; bg `#071020` |
| ❖ Note | 10pt | Fill `#EBF3FF` | Left accent `#3D7EBF` · planned / implemented |
| ⚠ Warning | 10pt | Fill `#FFF8E6` | Left accent `#E8A000` · arch constraints |
| DECISION | 10pt | Fill `#E0EEEE` | Left accent `#2A7A7A` · committed decisions |
| Code block | 8pt · Consolas | Fill `#F3F3F3` | Left accent `#9E9E9E` |
| Plain blockquote | 10pt italic | Fill `#F8F8F8` | Left accent `#C0C0C0` |
| ◆ Gate | 10pt | Fill `#EBF0F8` | Left accent `#4A6FA5` · phase gate criteria |
| Gate: Pending | 9pt bold | Fill `#EBF0F8` · text `#1D3D6B` | Left accent `#4A6FA5` |
| Gate: Passed | 9pt bold | Fill `#E4F5EC` · text `#1E5C28` | Left accent `#27A85A` |
| Gate: Bypassed | 9pt bold | Fill `#F5F0FF` · text `#4A2880` | Left accent `#7B4DBF` |
| ⛔ HALT / FAIL | 10pt | Fill `#FDF0EE` | Left accent `#B03020` · blocking gates |
| ✅ PASS | 10pt | Fill `#E4F5EC` | Left accent `#27A85A` · confirmed pass |
| Badge: Accepted | 9pt bold | Fill `#DFF0DC` · text `#1E5C28` | Left accent `#27A85A` |
| Badge: Proposed | 9pt bold | Fill `#FFF3D6` · text `#7A4800` | Left accent `#E8A000` |
| Badge: Open | 9pt bold | Fill `#E8F0FB` · text `#1D4E89` | Left accent `#3D7EBF` |
| Badge: Rejected | 9pt bold | Fill `#F9E8E8` · text `#7A1E1E` | Left accent `#C04040` |
| Badge: Deprecated | 9pt bold | Fill `#EFEFEF` · text `#555555` | Left accent `#909090` |
| Badge: Superseded | 9pt bold | Fill `#F0EAF8` · text `#4A2880` | Left accent `#7B4DBF` |

---

## 5. Callout Block Reference

Callout blocks render as single-cell tables with a 1.5pt left accent border and filled background. Block type is determined by the leading symbol (❖ ⚠ ◆ ⛔ ✅) or prefix keyword (DECISION, HALT gate, FAIL, PASS, Gate:).

### 5.1 Reference Table — Callout Blocks

| Block | Markdown trigger | Fill | Accent | Use case |
|---|---|---|---|---|
| ❖ Note | `> ❖ ...` | `#EBF3FF` | `#3D7EBF` | Planned or implemented items |
| ⚠ Warning | `> ⚠ ...` | `#FFF8E6` | `#E8A000` | Architectural constraints, pitfalls |
| DECISION | `> **DECISION:** ...` | `#E0EEEE` | `#2A7A7A` | Committed architectural decisions |
| Code | `> ``` ... ``` ` | `#F3F3F3` | `#9E9E9E` | Monospace code (Consolas 8pt) |
| Blockquote | `> plain text` | `#F8F8F8` | `#C0C0C0` | General quoted content (italic) |
| ◆ Gate | `> ◆ Gate: ...` | `#EBF0F8` | `#4A6FA5` | Phase gate criteria (forward-looking) |
| Gate: Pending | `◆ Pending` | Fill `#EBF0F8` · text `#1D3D6B` | `#4A6FA5` | Criteria defined, not yet evaluated |
| Gate: Passed | `◆ Passed` | Fill `#E4F5EC` · text `#1E5C28` | `#27A85A` | All criteria met |
| Gate: Bypassed | `◆ Bypassed` | Fill `#F5F0FF` · text `#4A2880` | `#7B4DBF` | Explicitly waived with documented reason |
| ⛔ HALT / FAIL | `⛔ HALT gate: ...` / `⛔ FAIL: ...` | `#FDF0EE` | `#B03020` | Blocking; triggered when gate criteria fail |
| ✅ PASS | `✅ PASS: ...` | `#E4F5EC` | `#27A85A` | Confirmed pass (saturated green) |

**Badges & Inline Elements**

| Block | Markdown trigger | Fill | Accent | Use case |
|---|---|---|---|---|
| Badge: Accepted | `**Accepted** (ADR)` | Fill `#DFF0DC` · text `#1E5C28` | `#27A85A` | Decision accepted, in effect |
| Badge: Proposed | `**Proposed** (ADR)` | Fill `#FFF3D6` · text `#7A4800` | `#E8A000` | Under review |
| Badge: Open | `**Open** (ADR)` | Fill `#E8F0FB` · text `#1D4E89` | `#3D7EBF` | Decision needed, not yet proposed |
| Badge: Rejected | `**Rejected** (ADR)` | Fill `#F9E8E8` · text `#7A1E1E` | `#C04040` | Explicitly declined |
| Badge: Deprecated | `**Deprecated** (ADR)` | Fill `#EFEFEF` · text `#555555` | `#909090` | Governed item being phased out |
| Badge: Superseded | `**Superseded** (ADR)` | Fill `#F0EAF8` · text `#4A2880` | `#7B4DBF` | Replaced by a newer ADR |
| # H1 | `# ...` | — | — | Aptos Serif 16pt bold `#1F3864` |
| ## H2 | `## ...` | — | — | Aptos Serif 13pt bold `#1F3864` |
| ### H3 | `### ...` | — | — | Aptos Serif 11pt bold `#2E5496` |
| **bold** | `**text**` | — | — | TextRun bold:true |
| *italic* | `*text*` | — | — | TextRun italics:true |
| \| table \| | `\| col \| col \|` | — | — | Header fill `#1F3864` · text `#FFFFFF` |
| - bullet | `- item` | — | — | LevelFormat.BULLET · indent 720 DXA |

### 5.2 Color System Rationale

Semantic temperature maps hue to category; saturation distinguishes certainty within a group. Gate and PASS share the green family but are visually distinct — Gate is muted (forward-looking criteria), PASS is saturated (confirmed outcome). Note and DECISION both use cool hues but differ by family: steel blue vs. teal, preventing collision under poor print conditions.

| Block | Hue family | Accent | Semantic logic |
|---|---|---|---|
| ❖ Note | Steel blue | `#3D7EBF` | Informational; cool and neutral |
| ⚠ Warning | Amber | `#E8A000` | Universal caution signal |
| DECISION | Teal / slate | `#2A7A7A` | Authoritative; distinct from Note's blue |
| Code / Quote | Neutral grey | `#9E9E9E` / `#C0C0C0` | No semantic weight |
| ◆ Gate | Blue-steel | `#4A6FA5` | Evaluative / neutral — criteria not yet resolved |
| ✅ PASS | Emerald green | `#27A85A` | Green family, saturated — confirmed done |
| ⛔ HALT / FAIL | Deep red | `#B03020` | Blocking; triggered when gate criteria fail |

**ADR Status Badge System**

Six lifecycle states cover the full ADR arc from open question through accepted, deprecated, superseded, or explicitly rejected. Violet (Superseded) is the only hue not used elsewhere — it reads as "historical record" without triggering any active-state association.

| Badge | Hue | Meaning |
|---|---|---|
| Accepted | Emerald green | Decision accepted and in effect |
| Proposed | Amber | Formally proposed, under review |
| Open | Steel blue | Decision needed, not yet proposed |
| Rejected | Dusty rose | Explicitly evaluated and declined |
| Deprecated | Neutral grey | Accepted; governed item being phased out |
| Superseded | Violet | Replaced by a newer ADR — closes history without deletion |

**Gate Status Badge System**

Three states track a gate's lifecycle. No "Failed" badge exists on Gate — when a gate fails it becomes a ⛔ HALT block, enforcing the semantic handoff between the two block types.

| Badge | Hue | Meaning |
|---|---|---|
| ◆ Pending | Blue-steel | Criteria defined; not yet evaluated |
| ◆ Passed | Emerald green | All criteria met — gate closed |
| ◆ Bypassed | Violet | Explicitly waived with documented justification |

### 5.3 Live Examples

One rendered instance per callout type. In Markdown source these are blockquotes; the DOCX converter maps them to single-cell styled tables.

**❖ Note — steel blue · informational**
> ❖ Implemented: Artifact Registry with content-addressable storage. RFC8785 JCS canonicalization. 14 integration tests.

**⚠ Warning — amber · caution**
> ⚠ Do not define tasks as fixed-length windows without regime indexing — window-based tasks eliminate the distribution p(T) meta-learning requires.

**DECISION — teal · committed**
> **DECISION:**
> Inner loop adapts ψ_condnorm + h_alloc (~1,100 parameters) in 3–5 gradient steps. Base encoder and regime head frozen during inner loop.

```mm-format-json
{
  "callouts": {
    "styles": {
      "badge_accepted": {
        "block_type": "paragraph",
        "style_name": "MM Badge Accepted"
      },
      "badge_open": {
        "block_type": "paragraph",
        "style_name": "MM Badge Open"
      },
      "badge_proposed": {
        "block_type": "paragraph",
        "style_name": "MM Badge Proposed"
      },
      "blockquote": {
        "block_type": "paragraph",
        "style_name": "MM Blockquote"
      },
      "code": {
        "block_type": "paragraph",
        "style_name": "MM Code"
      },
      "decision": {
        "block_type": "paragraph",
        "style_name": "MM Decision"
      },
      "gate": {
        "block_type": "paragraph",
        "style_name": "MM Gate"
      },
      "halt": {
        "block_type": "paragraph",
        "style_name": "MM Halt"
      },
      "note": {
        "block_type": "paragraph",
        "style_name": "MM Note"
      },
      "pass": {
        "block_type": "paragraph",
        "style_name": "MM Pass"
      },
      "warning": {
        "block_type": "paragraph",
        "style_name": "MM Warning"
      }
    }
  },
  "document_defaults": {
    "base_font_family": "Aptos Serif",
    "base_font_size_pt": 10.0,
    "body_style_name": "Normal",
    "code_style_name": "Code",
    "line_spacing": "1.15",
    "list_bullet_style_name": "List Bullet",
    "list_number_style_name": "List Number",
    "page_margins_mm": {
      "bottom": 25.4,
      "left": 25.4,
      "right": 25.4,
      "top": 25.4
    }
  },
  "headings": {
    "levels": {
      "1": {
        "after_spacing_pt": 4.0,
        "before_spacing_pt": 12.0,
        "keep_with_next": true,
        "outline_level": 1,
        "style_name": "Heading 1"
      },
      "2": {
        "after_spacing_pt": 4.0,
        "before_spacing_pt": 12.0,
        "keep_with_next": true,
        "outline_level": 2,
        "style_name": "Heading 2"
      },
      "3": {
        "after_spacing_pt": 2.0,
        "before_spacing_pt": 8.0,
        "keep_with_next": true,
        "outline_level": 3,
        "style_name": "Heading 3"
      }
    },
    "max_toc_level": 3
  },
  "paragraphs": {
    "styles": {
      "body": {
        "style_name": "Normal"
      },
      "caption": {
        "keep_with_previous": true,
        "style_name": "Caption"
      },
      "code_block": {
        "font_family": "Consolas",
        "style_name": "Code"
      }
    }
  },
  "profiles": {
    "default": {}
  },
  "rules_schema_version": "1.0.0",
  "title_page": {
    "classification_style_name": "MM Classification",
    "companion_line_style_name": "MM Companion Line",
    "keep_with_next_for_title": true,
    "subtitle_style_name": "MM Subtitle",
    "title_style_name": "MM Title",
    "version_line_style_name": "MM Version Line",
    "wordmark_style_name": "MM Wordmark"
  },
  "toc": {
    "heading_style_mappings": {
      "1": "TOC 1",
      "2": "TOC 2",
      "3": "TOC 3"
    },
    "include_levels": [
      1,
      2,
      3
    ],
    "toc_style_name": "TOC Heading"
  }
}
```

**Code block — neutral grey**
```
@dataclass
class MetaTask:
    task_id: str        # hash of (regime_id, t0, t1)
    support_set: pl.DataFrame
    query_set:   pl.DataFrame
```

**Plain blockquote — light grey · italic**
> Reproducibility is a tiered contract. A run is credible when all required bundle artifacts are present and hashed.

**◆ Gate — blue-steel · forward-looking criteria**
> ◆ Gate: Kalman beta converges within 15 days on both 2020 and 2022 breaks. Hedging residual variance reduces by ≥ 10% vs. 60-day rolling OLS.

**⛔ HALT / FAIL — deep red · blocking**
> ⛔ HALT gate: If baseline OOS IC is negative or PBO > 0.60, halt and diagnose before adding complexity.
> ⛔ FAIL: Net portfolio performance collapses after costs/turnover constraints.

**✅ PASS — emerald green · confirmed**
> ✅ PASS: Constraint feasibility ≥ 99% of runs; violations are explainable, gated, and logged with reason codes.

---

## 6. Resolution Ledger Color System

The Resolution Ledger (MRL) renderer uses a three-layer color scheme. The layers are independent and composable: type identity sets the card's dominant hue, lifecycle state sets badge color, and phase heat sets contextual tinting on chips and section banners. A reader should be able to orient to type, urgency, and phase without reading body text.

### 6.1 Entry Type Identity

Each first-class MRL entry type gets a fixed hue that appears on the card's left border (4pt solid), the solid-fill type chip (white text on color), and the row accent cell in the count matrix. The accent and background pair are drawn from the spec's existing semantic palette.

| Type | Accent | Chip bg | Card bg tint | Semantic rationale |
|---|---|---|---|---|
| `OI` | `#2E5496` | `#E8F0FB` | `#E8F0FB` | Steel blue — actionable work item. Shares H3 heading hue to signal implementation-facing content. |
| `ADR` | `#1F3864` | `#EBF0F8` | `#EBF0F8` | Deep navy — authoritative decision record. Uses the primary heading hue to signal permanence. |
| `GATE` | `#4A6FA5` | `#EBF0F8` | `#EBF0F8` | Blue-steel — evaluative, forward-looking. Lighter than ADR navy to distinguish criteria-not-yet-resolved from decided records. |
| `MLC` | `#2A7A7A` | `#E0EEEE` | `#E0EEEE` | Teal — meta-learning component. Shares DECISION callout hue; signals committed Phase II ML scope. |
| `MOM` | `#5A2D82` | `#F5F0FF` | `#F5F0FF` | Violet — momentum strategy items. Distinct from all other type hues; violet reads as "strategy-specific" without triggering active-state associations. |
| `RG` | `#7A5800` | `#FFF8E6` | `#FFF8E6` | Amber/dark gold — research gap. Shares ⚠ Warning callout family; signals an open question without confirmed answer. |
| `AQ` | `#B03020` | `#FDF0EE` | `#FDF0EE` | Deep red — architectural question. Shares ⛔ HALT callout hue; signals a pre-ADR decision fork that must be resolved before implementation. |

**Type chip rendering:**

- HTML print: solid fill chip — `background: {accent}; color: #fff; font-family: DM Mono; font-size: 7pt; padding: 2px 7px`
- DOCX: shaded inline run — fill `{accent}`, text `#FFFFFF`, Consolas 7pt, small caps

### 6.2 Lifecycle State & Status Badges

Status badges in the MRL follow §5's existing ADR and Gate badge systems. The mapping below extends those systems to all MRL entry types.

| MRL status | Badge class | Color family | When applied |
|---|---|---|---|
| OPEN | badge-open | Steel blue (`#3D7EBF`) | OI, RG, AQ, ADR, GATE awaiting action |
| PARTIAL | badge-proposed | Amber (`#E8A000`) | Core slice delivered; acceptance criteria not fully met |
| BLOCKED | badge-rejected | Dusty rose (`#C04040`) | Cannot proceed due to external dependency |
| DEFERRED | badge-deprecated | Neutral grey (`#909090`) | Intentionally deferred to a later phase |
| CLOSED | badge-accepted | Emerald green (`#27A85A`) | All acceptance criteria met and verified |
| SUPERSEDED | badge-superseded | Violet (`#7B4DBF`) | Replaced by a later entry without deletion |
| ADR: PROPOSED | badge-proposed | Amber (`#E8A000`) | ADR formally proposed, under review |
| ADR: ACCEPTED | badge-accepted | Emerald green (`#27A85A`) | ADR accepted and governing |
| GATE: Pending | badge-gate-pending | Blue-steel (`#4A6FA5`) | Gate criteria defined; not yet evaluated |
| GATE: Passed | badge-gate-passed | Emerald green (`#27A85A`) | All gate criteria met — gate closed |
| GATE: Deferred | badge-gate-bypassed | Violet (`#7B4DBF`) | Gate evaluation deferred to a later phase |

**Blocking indicator:**

Entries where `blocking: YES` AND `status ∈ {OPEN, PARTIAL}` receive an additional inline chip:

- Label: `⚑ BLOCKING`
- Style: `background: #FDF0EE; color: #B03020; border: 1px solid #B03020`
- Font: DM Mono 7pt

### 6.3 Phase Heat & Section Banners

Phase chips appear inline on every entry card header and in the blocking hotlist. Section banners use the same palette as full-bleed left-accented dividers at each H1 boundary in the rendered ledger.

| Phase | Accent | Chip / banner bg | Semantic rationale |
|---|---|---|---|
| 0 · I-A · I-B · I-C · I-D | `#1E5C28` | `#E4F5EC` | Emerald green — CLOSED phases. Green reads as "done and verified"; safe to treat as stable foundation. |
| I-E | `#1E5C28` | `#E4F5EC` | Emerald green — CLOSED on the canonical path as of `VERSION.md` **4.5.4** (substrate); companion baseline **4.9.0** records the F-2 planning-surface sync. |
| I-F (active / honesty gate) | `#7A4800` | `#FFF3D6` | Amber — active Phase I closure work (architecture truthfulness, canonical-path verification). Shares ⚠ Warning family. |
| II (DEFERRED) | `#4A2880` | `#F5F0FF` | Violet — intentionally deferred. Shares Superseded/Bypassed badge hue; signals historical record, not active scope. |
| III · IV | `#555555` | `#EFEFEF` | Neutral grey — far-future phases. Shares Deprecated badge hue; no urgency signal. |
| Cross-Phase | `#2A7A7A` | `#E0EEEE` | Teal — cross-cutting concerns not bound to a single phase. Shares DECISION callout hue; signals an authoritative cross-phase commitment. |

**Phase chip rendering:**

- Label: `Phase {value}` (e.g. `Phase I-E`)
- Style: `background: {chip_bg}; color: {accent}; border: 1px solid {accent}; font-family: DM Mono; font-size: 6.5pt; padding: 2px 6px`

**Section banner rendering:**

- Full-width div with `border-left: 4px solid {accent}; background: {chip_bg}`
- Title in IM Fell English 16pt · color `{accent}`
- Appears at every H1 phase boundary in the rendered ledger

### 6.4 Dashboard Heat Tinting

The §1 count matrix and blocking hotlist use cell-level tinting to communicate urgency without prose. Rules apply in addition to the row type accent.

| Cell condition | Fill | Weight | Notes |
|---|---|---|---|
| OPEN count ≥ 5 | `#FFF3D6` amber | Bold · `#7A4800` | High-urgency open work; shares ⚠ Warning family |
| OPEN count 1–4 | `#FFF8E6` light amber | Normal | Moderate open count; gentle caution signal |
| CLOSED count > 0 | `#E4F5EC` green | Bold · `#1E5C28` | Completed work; positive reinforcement |
| DEFERRED count > 0 | `#F5F0FF` violet | Bold · `#4A2880` | Intentional deferral; not urgent but visible |
| Zero count | — (no fill) | Normal | Neutral |
| HALT count (gate readiness) | `#FFF8E6` amber — full row | Bold red `#B03020` at 11pt | HALT count styled in deep red to read as alert |
| Gate CLOSED row | `#E4F5EC` green — full row | Normal | Gate passed badge |
| Gate DEFERRED row | `#F5F0FF` violet — full row | Normal | Gate bypassed badge |

**Row type accent (count matrix):**

Each type row carries a colored left border (3pt solid `{type_accent}`) and a colored label cell with `background: {type_bg}; color: {type_accent}; font-family: DM Mono; font-weight: 600`. See §6.1 for accent/bg pairs per type.

### 6.5 Evidence Pills & Inline Elements

`evidence_needed` fields render as compact inline pills. Each pill type has a fixed semantic color from the existing palette. Impact callouts and resolution callouts reuse the §5 callout block system.

| Evidence type | Label | Accent / bg | Semantic family |
|---|---|---|---|
| `code` | `</>` | `#2E5496` / `#E8F0FB` | Steel blue — implementation artifact |
| `tests` | `✓ tests` | `#1E5C28` / `#DFF0DC` | Emerald green — verified / acceptance evidence |
| `doc-update` | `📄 doc` | `#7A4800` / `#FFF3D6` | Amber — documentation change required |
| `adr-decision` | `⚖ ADR` | `#2A7A7A` / `#E0EEEE` | Teal — DECISION callout family; formal ADR required |
| `artifact` | `⬡ artifact` | `#4A2880` / `#F5F0FF` | Violet — produced run bundle artifact |
| `benchmark` | `📊 bench` | `#6B3A00` / `#FFF0D6` | Dark amber — empirical measurement required |

**Pill rendering:**

```
background: {bg};
color: {accent};
border-left: 2px solid {accent};
font-family: DM Mono;
font-size: 7pt;
padding: 1px 6px;
margin-right: 4px;
```

**Impact & resolution callout routing:**

| Condition | Callout style | Icon |
|---|---|---|
| `blocking: YES` + impact present | ⛔ HALT / FAIL (`#B03020` / `#FDF0EE`) | ⛔ |
| `blocking: NO` + impact present | ⚠ Warning (`#E8A000` / `#FFF8E6`) | ⚠ |
| `status: CLOSED` + resolution present | ✅ PASS (`#27A85A` / `#E4F5EC`) | ✅ |
| Any other status + resolution present | ❖ Note (`#3D7EBF` / `#EBF3FF`) | ❖ |

---

*This specification is the source of truth for the MarketMind document converter. The HTML print edition (`MarketMind_Formatting_Spec_v1_1_0_print.html`) is the canonical rendered form; this Markdown edition is the machine-readable companion introduced in v1.2.0.*

*Companion suite: Implementation Plan v6.4.14 · Technical Roadmap v1.4.15 · Meta-Learning Core v1.2.13 · Meta-Learning Architecture Vision v1.2.14 · Resolution Ledger v1.0.6 · README.md 4.9.0 · VERSION.md 4.9.0*
