# SDRD Website - AI Coding Instructions

## Project Overview
This is a **website project** for SDRD. The project currently contains:
- `index.html` - Main HTML entry point (currently empty, needs development)
- `studentData.xlsx` - Student data source file
- No build system, framework, or backend infrastructure currently in place

## Architecture & Key Patterns

### Current Structure
- **Frontend-only**: Plain HTML/CSS/JavaScript (no framework)
- **Data source**: `studentData.xlsx` contains student data (format TBD)
- **Deployment model**: Static file hosting expected

### Integration Points
- Student data from `studentData.xlsx` will need to be integrated into the website
- Determine if data should be embedded, fetched, or processed during build time

## Development Workflow

### Getting Started
1. Start by defining the website purpose and content structure
2. Create semantic HTML in `index.html`
3. Add CSS styling (recommend inline or separate `styles.css`)
4. Integrate student data as needed

### File Organization
- Keep all assets in the root or a simple folder structure (e.g., `assets/`, `css/`)
- No build step required unless adding preprocessing later

## Conventions & Guidelines

### HTML Best Practices
- Use semantic HTML5 tags (`<header>`, `<main>`, `<footer>`, `<section>`, etc.)
- Keep markup simple and accessible (WCAG baseline compliance)
- Link external CSS/JS in the `<head>` section

### Data Handling
- `studentData.xlsx` needs clarification on:
  - Expected data schema (fields, format)
  - How it will be consumed (embedded JSON, CSV conversion, etc.)

## Next Steps (Recommended)
1. **Define the website purpose**: Is this a portfolio, directory, or informational site?
2. **Document data schema**: What fields/structure does `studentData.xlsx` contain?
3. **Add styling**: Create `css/style.css` for consistent branding
4. **Plan scalability**: Consider adding a build process if static site grows

---
*This file will be updated as the project evolves. Key areas for expansion: build process, deployment configuration, testing strategy.*
