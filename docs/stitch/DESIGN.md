---
name: Botanical Telemetry
colors:
  surface: '#0f1511'
  surface-dim: '#0f1511'
  surface-bright: '#353a37'
  surface-container-lowest: '#0a0f0c'
  surface-container-low: '#181d19'
  surface-container: '#1c211d'
  surface-container-high: '#262b28'
  surface-container-highest: '#313632'
  on-surface: '#dfe4de'
  on-surface-variant: '#bdcabd'
  inverse-surface: '#dfe4de'
  inverse-on-surface: '#2c322e'
  outline: '#889488'
  outline-variant: '#3e4a40'
  surface-tint: '#72dc94'
  primary: '#74de96'
  on-primary: '#00391b'
  primary-container: '#58c27d'
  on-primary-container: '#004c26'
  inverse-primary: '#006d39'
  secondary: '#a1d673'
  on-secondary: '#1a3700'
  secondary-container: '#2f5b01'
  on-secondary-container: '#9dd26f'
  tertiary: '#bacfbd'
  on-tertiary: '#233428'
  tertiary-container: '#9fb3a2'
  on-tertiary-container: '#344638'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#8ef9ae'
  primary-fixed-dim: '#72dc94'
  on-primary-fixed: '#00210d'
  on-primary-fixed-variant: '#00522a'
  secondary-fixed: '#bcf28c'
  secondary-fixed-dim: '#a1d673'
  on-secondary-fixed: '#0d2000'
  on-secondary-fixed-variant: '#285000'
  tertiary-fixed: '#d3e8d5'
  tertiary-fixed-dim: '#b7ccba'
  on-tertiary-fixed: '#0e1f14'
  on-tertiary-fixed-variant: '#394b3d'
  background: '#0f1511'
  on-background: '#dfe4de'
  surface-variant: '#313632'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 18px
    letterSpacing: 0em
  label-lg:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 18px
    letterSpacing: 0.02em
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.04em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '400'
    lineHeight: 14px
    letterSpacing: 0.06em
  telemetry-metric:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 28px
    letterSpacing: -0.03em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 0.75rem
  margin: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 0.75rem
  space-lg: 1.25rem
  space-xl: 1.75rem
---

## Brand & Style

This visual system translates rigorous data analytics into an organic, high-performance command center. The visual direction balances the precision of an aerospace or telemetry console with subtle botanical geometry. It conveys deep technical competence, disciplined curiosity, and methodical craft.

The aesthetic fuses **Tactile Technical Minimalism** with **Subtle Tonal Depth**:
- Ultra-dark verdant surfaces reminiscent of dense desert flora at night.
- Crisp, utilitarian typography pairing high-legibility geometric sans-serif body copy with structured, calibrated monospace metrics.
- Fine hairline gridlines, segmented progress indicators, and geometric cactus emblems acting as architectural accents rather than novelty graphics.
- High-contrast, legible data surfaces calibrated specifically for the constraints of an 850px markdown container without visual noise.

## Colors

The palette is strictly anchored in deep chlorophyll greens, luminescent shoots, and desaturated vegetal neutrals, explicitly avoiding cybernetic blues, magentas, or neon saturation.

### Palette Architecture
- **Canvas Base (`#0B100D`)**: The primary void; a deep black-tinted forest background reducing eyestrain and establishing maximum telemetry contrast.
- **Deep Forest (`#14221A`)**: Structural framing, section borders, and sub-card backgrounds.
- **Surface (`#1B2C20`)**: Elevated cards, telemetry widgets, data cells, and interactive rows.
- **Surface Highlight (`#243A2C`)**: Hover states, active tabs, and inline code block fills.
- **Primary / Cactus Green (`#58C27D`)**: Primary telemetry values, key status meters, success states, and dominant icon fills.
- **Secondary / Light Lime (`#B7ED87`)**: Sparks, peak data metrics, active commit beacons, and focused interactive elements.
- **Base Text (`#E7F0E8`)**: High-contrast, near-white vegetal tint ensuring optimal legibility.
- **Muted Text (`#91A799`)**: Axis labels, metric units, timestamp metadata, and secondary notes.
- **Ghost Border (`rgba(88, 194, 125, 0.15)`)**: Ultra-thin precision dividers framing telemetry blocks without visual weight.

## Typography

The typographic hierarchy distinguishes narrative human content from automated analytical output:
- **Headings & Body (`Inter`)**: Tuned for maximum clarity, low eye strain, and neutral executive communication. Tight letter tracking is applied across headings to create an authoritative, editorial density.
- **Telemetry & Labels (`JetBrains Mono`)**: Strict tabular alignment. All numerical values, timestamps, git commits, code snippets, and operational status chips use monospace numerals to ensure column alignment and data consistency.
- **Metric Scaling**: Large numeric display sizes are balanced with small uppercase units (`124.8 ms`, `42.5 km`) rendered in `Muted Text` to avoid overwhelming the 850px container viewport.

## Layout & Spacing

Designed precisely for the fixed **850px GitHub README container**, the layout employs a compact data-dense grid system without horizontal overflow.

### Grid Architecture
- **Master Container**: Max-width capped at `850px`, horizontally centered with `0 auto`.
- **Column Structure**: Built on a fractional 12-column layout utilizing CSS Grid or flex equivalent in SVG/HTML embeds:
  - Full-width hero metrics: 12 columns (`850px`).
  - Dual metric splits (Track Viz vs. Code Velocity): 6 columns each (`~415px`).
  - Tri-card telemetry blocks: 4 columns each (`~270px`).
  - Micro-stat grids: 3 columns each (`~198px`).

### Vertical Rhythm & Density
- Keep vertical section gaps consistent at `space-lg` (1.25rem / 20px) to balance high density with structural clarity.
- Internal component padding relies on `space-md` (0.75rem / 12px) for cards, and `space-xs` (0.25rem / 4px) to `space-sm` (0.5rem / 8px) for badge pill interiors.
- Mobile/Responsive Fallback: On screens below 640px, all multi-column splits collapse into a single stacked column with `gutter` of `0.75rem`.

## Elevation & Depth

Because GitHub README rendering environments natively flatten layers and restrict box-shadow styling, elevation is established strictly through **Tonal Surface Stacking** and **Subtle Luminous Outlines**:

- **Layer 0 (Canvas Base - `#0B100D`)**: Backing canvas behind all containers.
- **Layer 1 (Recessed/Track - `#14221A`)**: Used for running track outlines, metric troughs, and background progress bars.
- **Layer 2 (Raised Cards - `#1B2C20`)**: Primary widget and telemetry surfaces. Features a hairline border of `1px solid rgba(88, 194, 125, 0.18)` to clearly separate cards from the dark backdrop.
- **Layer 3 (Interactive & Highlights - `#243A2C`)**: Highlighted table rows, active badges, or nested micro-cells within cards.
- **Luminous Bloom (Accents Only)**: Running paths and primary line charts feature a soft internal SVG drop-shadow: `drop-shadow(0 0 4px rgba(88, 194, 125, 0.45))` to create the feel of an illuminated tactical radar without bleed.

## Shapes

The shape system utilizes soft, precise industrial corners (Level 1):
- **Base Components**: Outer cards, stats panels, code snippets, and callout boxes use `rounded` (0.25rem / 4px) to `rounded-lg` (0.5rem / 8px) to maintain an instrument-panel aesthetic.
- **Status Indicators & Chips**: High-density tags and state pills retain a small radius (0.25rem) rather than full pill circular ends, maintaining the engineered aesthetic.
- **Botanical Emblems**: Cactus motifs, thorns, and coordinate glyphs are constructed from clean 45-degree and 90-degree geometric vectors, avoiding hand-drawn or cartoonish silhouettes.

## Components

### Telemetry Cards
- **Base**: Background `#1B2C20`, border `1px solid rgba(88, 194, 125, 0.18)`, border-radius `6px`, padding `12px 16px`.
- **Header**: Includes an optional geometric botanical glyph (12x12px), title in `label-sm` (`#91A799`, uppercase), and real-time status beacon (4x4px circle, `#B7ED87`).
- **Value**: Displayed in `telemetry-metric` (`#E7F0E8`), with trailing units in `#91A799`.

### Badges & Filter Chips
- **Surface**: `#14221A` background with `1px solid rgba(88, 194, 125, 0.25)`.
- **Text**: `label-md` using JetBrains Mono, text color `#58C27D`.
- **Active State**: Inverted with `#58C27D` fill, `#0B100D` bold text, zero border.

### Running Track & Telemetry Visualizations
- **Track Bed**: SVG path with `#14221A` stroke, width `4px`, cap `round`.
- **Paced Route**: Dynamic foreground stroke using `#58C27D` with a `drop-shadow(0 0 3px rgba(88, 194, 125, 0.5))`.
- **Splits / Pins**: `#B7ED87` filled diamonds or 45-degree rotated squares (6x6px) denoting personal records and milestone markers.

### Segmented Progress Bars
- **Container**: Flex row with 10 to 20 discrete 2px-wide segments spaced by 1px gaps.
- **Inactive Cells**: `#14221A`.
- **Active Cells**: `#58C27D` scaling upward into `#B7ED87` for peak completion tiers.

### Data Tables & Lists
- **Rows**: Alternating `#1B2C20` and transparent backgrounds with a bottom divider of `1px solid rgba(88, 194, 125, 0.08)`.
- **Key-Value Pairs**: Labels left-aligned in `body-sm` (`#91A799`), values right-aligned in `label-md` (`#E7F0E8`).