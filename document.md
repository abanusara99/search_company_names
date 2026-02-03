# Technical Documentation

## Project Overview
A Flask-based web application that generates direct links to company official pages (website, careers, LinkedIn) using natural search patterns.

## Tech Stack
- **Backend**: Python 3.10+, Flask 2.3+
- **Frontend**: HTML5, CSS3 (no JavaScript frameworks)
- **Deployment**: Standard WSGI server (Gunicorn recommended)

## Design Philosophy
- **Zero external dependencies** (no APIs, databases, or storage)
- **Privacy-focused**: No user data collection
- **Mobile-first responsive design**
- **Flip-card UI** for intuitive navigation

## Key Features
1. **Smart Link Generation**  
   Uses natural Google search patterns (`{company} company`, `{company} careers`) to surface official pages without hardcoding URLs.

2. **Dual-Mode Results**  
   - Main search: Direct Google search links  
   - Example pages: Predefined flip cards for top companies (Google, PwC, Stripe, etc.)

3. **Responsive Layout**  
   - Desktop: 3-column grid  
   - Mobile: Single-column stack with touch-friendly elements

## File Structure
