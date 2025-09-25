# Parking_Project Architecture

## Overview
This is a static web application for parking management, ticket payment, and enforcement. All logic is client-side (HTML, CSS, JS) with localStorage for demo data.

## Main Components
- **index.html**: Landing page, navigation, and service cards
- **pay-ticket.html**: Ticket payment, violation lookup
- **enforcement.html**: Employee login, violation entry

## Data Flow
- Violations are written in `enforcement.html` and stored in browser localStorage
- `pay-ticket.html` reads localStorage to show fines for vehicles

## Extending
- Backend integration can be added for real data persistence
- UI is modular and easy to extend
