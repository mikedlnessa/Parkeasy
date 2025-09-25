# Parking_Project

A web-based smart parking management system for daily, monthly, and enforcement operations.

## Features
- Pay parking tickets online
- Employee enforcement portal for writing violations
- Modern UI with purple and turquoise theme
- LocalStorage-based violation tracking

## Pages
- `index.html`: Main landing page
- `pay-ticket.html`: Pay parking tickets
- `monthly-parking.html`: Monthly parking options
- `daily-parking.html`: Daily parking options
- `enforcement.html`: Employee login and violation writing

## Employee Logins
- Angela / AT1001!!
- Mike / MD1001!!

## Violation Types & Fines
- NO PAYMENT: $50
- NO PARKING: $125
- IMPROPER PARKING: $25
- GATE RUNNING: $250

## Running Locally
You can use any static server (e.g., Python, Node.js, Docker) to serve the files.

### Python
```sh
python -m http.server 8080
```

### Node.js (http-server)
```sh
npm install -g http-server
http-server . -p 8080
```

### Docker
See Dockerfile below.

## Project Structure
```
Parking_Project/
├── .gitignore
├── README.md
├── Dockerfile
├── index.html
├── pay-ticket.html
├── enforcement.html
├── monthly-parking.html
├── daily-parking.html
```

## Documentation & Diagrams
See `docs/` folder for architecture, flowcharts, and developer guides.
