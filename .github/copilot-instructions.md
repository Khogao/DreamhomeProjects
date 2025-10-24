# Dreamhome Riverside - Financial Analysis Project

## Project Overview

This is a **Vietnamese real estate financial analysis application** for the Dreamhome Riverside project restructuring. The system presents 3 restructuring scenarios through interactive HTML dashboards deployed on GitHub Pages.

## Architecture & File Structure

### Core Application Files
- `index.html` - Main landing page with scenario comparison table and navigation
- `scenario1_conservative.html` - Conservative scenario (NPV -96B, not viable)
- `scenario2_balanced.html` - **Recommended scenario** (NPV +305B, 22.3% IRR)  
- `scenario3_aggressive.html` - High-risk scenario (NPV +164B, 29.4% IRR)
- `sensitivity_analysis.html` - 2D sensitivity matrices for all scenarios
- `risk_mitigation_plan.html` - Risk management framework with mitigation strategies
- `dreamhome_riverside_analysis.xlsx` - Source financial model (7 sheets)

### Project Structure Pattern
```
/
├── index.html                    # Landing page & scenario comparison
├── scenario[1-3]_*.html         # Individual scenario deep-dives
├── sensitivity_analysis.html    # Cross-scenario sensitivity analysis
├── risk_mitigation_plan.html    # Risk framework & mitigation plans
├── dreamhome_riverside_analysis.xlsx  # Excel financial model
└── dreamhome_analysis_complete/  # Backup/archive folder (identical content)
```

## Design System & UI Patterns

### CSS Architecture
- **Consistent gradient backgrounds**: `linear-gradient(135deg, primary-color 0%, secondary-color 100%)`
- **Card-based layouts**: `.scenario-card`, `.summary-card`, `.resource-card` with hover transforms
- **Color coding system**:
  - Blue (hex 0d47a1): Default/neutral
  - Green (hex 2e7d32): Positive/recommended (Scenario 2)
  - Red (hex c62828): Negative/high-risk
  - Orange (hex f57c00): Warning/medium risk

### Key UI Components
- **Comparison tables**: Always use `.comparison-table` with hover effects
- **Metric displays**: Grid layouts (`.summary-grid`) with large numbers (32px font)
- **Navigation**: Consistent `.cta-button` styling with color variants
- **Status badges**: `.scenario-badge` with semantic color classes

## Content & Data Patterns

### Vietnamese Language Conventions
- All content in Vietnamese with professional financial terminology
- Currency always in "tỷ VNĐ" (billion VND)
- Dates in DD/MM/YYYY format
- Numbers use Vietnamese decimal notation

### Financial Data Structure
- **NPV calculations** at 12% discount rate
- **IRR values** displayed as percentages (1 decimal place)
- **Timeline** in months
- **Cash flow** modeling over 24-month periods
- **Sensitivity analysis** uses 2D matrices (Price × Cost, Price × Compensation)

### Scenario Numbering System
1. **Scenario 1 (Conservative)**: Maintain all units, minimal restructuring
2. **Scenario 2 (Balanced)**: **RECOMMENDED** - Liquidate 329 units, optimal risk/return
3. **Scenario 3 (Aggressive)**: Liquidate 700 units, maximum upside with high risk

## Development Workflows

### Adding New Scenarios
1. Copy existing scenario HTML file
2. Update gradient colors in CSS (different color per scenario)
3. Modify financial metrics in `.summary-grid` cards
4. Update comparison table in `index.html`
5. Ensure navigation links are updated across all files

### Updating Financial Data
1. Modify Excel model first (`dreamhome_riverside_analysis.xlsx`)
2. Extract key metrics and update HTML files
3. Regenerate sensitivity matrices if assumptions change
4. Update risk assessments if risk profile changes

### Deployment Process
- **Primary hosting**: GitHub Pages at `khogao.github.io/DreamhomeProjects`
- **Deployment**: Direct push to `main` branch triggers auto-rebuild
- **File structure**: All HTML files must be in root directory for relative linking
- **Assets**: Excel file served directly from GitHub (no CDN needed)

## Integration Points & Dependencies

### External Dependencies
- **No JavaScript frameworks** - Pure HTML/CSS for maximum compatibility
- **No external CSS libraries** - All styling inline/embedded
- **No API calls** - Static content only

### Cross-File Linking Patterns
- All internal links use **relative paths**: `scenario1_conservative.html` (not `/scenario1_conservative.html`)
- Navigation between scenarios follows consistent pattern
- Back to home: "← Về Trang chủ" links to `index.html`

### Data Flow
1. Excel model (`dreamhome_riverside_analysis.xlsx`) → Manual data extraction
2. Financial metrics → HTML metric cards (`.summary-card`)
3. Comparison data → Main comparison table (`index.html`)
4. Risk data → Risk mitigation tables and matrices

## Project-Specific Conventions

### File Naming
- Scenarios: `scenario[number]_[name].html` pattern
- Analysis files: `[analysis_type]_analysis.html` pattern
- Documentation: `ALL_CAPS.md` for meta files

### Content Organization
- **Hero sections** always include project meta (analyst name, date)
- **Summary cards** use consistent 4-metric layout (NPV, IRR, Capital, Timeline)
- **Tables** always include hover effects and semantic color coding
- **Footer disclaimers** required on all financial analysis pages

### GitHub Pages Specific
- All files must be in repository root (no subdirectories for main content)
- Relative linking only (GitHub Pages serves from subdirectory)
- Excel files served with correct MIME types automatically

## Critical Business Logic

### Financial Model Assumptions
- **Base case pricing**: 80 tr/m² for balanced scenario
- **Discount rate**: 12% for NPV calculations  
- **Compensation rate**: 10-12% for unit liquidation
- **Construction timeline**: 21-30 months depending on scenario

### Decision Framework
- **Scenario 2 (Balanced)** is always the recommended option
- Risk assessment uses worst-case NPV as key metric
- Success probability based on sensitivity analysis breakeven points

When modifying financial content, always ensure consistency across all scenario files and maintain the Vietnamese professional tone.