# 🌐 Nexus: AI Smart Supply Chain Optimizer

![Project Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Stack-FastAPI%20%7C%20Vanilla%20JS-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

**Nexus** is an enterprise-grade AI Logistics Platform built to predict, analyze, and optimize global shipping operations. By analyzing telemetric data—such as weather patterns, traffic congestion, and baseline delays—the system autonomously computes real-time risk vectors and provides actionable routing optimizations.

---

## ✨ Features

- **📊 Multi-Tab Command Dashboard**: A sleek, dark-mode-first, glassmorphic UI featuring a persistent navigation system and a customizable command palette.
- **🧠 Risk Prediction Engine**: Leverages the Google Gemini AI API via a highly optimized prompt pipeline to analyze complex transit variables.
- **🗺️ Route Visualization**: Integrates interactive, high-contrast Leaflet.js maps displaying shipping nodes, dispatch tracking, and alternative paths.
- **📈 Advanced Analytics**: Real-time Chart.js integrations rendering live global shipment volumes, risk distributions, and trend forecasting.
- **🛡️ Autonomous Fallback Simulation**: Built-in system resilience. If the live AI API experiences rate limits, the frontend gracefully engages a deterministic predictive matrix with zero downtime.
- **⚡ Operational Intelligence Layer**: Features a live telemetry activity feed, animated metric strips, toast notifications, historical session persistence, and a built-in neural chat assistant.

---

## 🛠️ Technology Stack

### Backend
- **FastAPI**: High-performance asynchronous backend framework.
- **Uvicorn**: Lightning-fast ASGI server.
- **Python-dotenv**: Secure environment variable management.

### Frontend
- **HTML5 & Vanilla CSS3**: Highly optimized, framework-less, custom enterprise design system.
- **Vanilla JavaScript**: DOM manipulation, event delegation, and asynchronous API communication.
- **Leaflet.js**: Lightweight, open-source interactive mapping.
- **Chart.js**: Client-side, canvas-based dynamic data visualization.

---

## 🚀 How It Works

1. **Scenario Initialization**: The user inputs a starting node, a destination node, current weather severity, traffic gridlock levels, and reported baseline delays into the *Analyze Shipment* panel.
2. **Data Processing**: The frontend packages this payload and sends a `POST` request to the FastAPI `/analyze` endpoint.
3. **AI Evaluation**: The backend constructs a highly detailed context prompt and passes the variables to the Gemini Pro API.
4. **Actionable Output**: The AI returns a structured JSON object containing a Risk Index (0-100), AI Reasoning, and an Optimization Suggestion.
5. **Dynamic Rendering**: The frontend parses the response, visually updates the risk gauge, plots the coordinates on the interactive map, triggers color-coded timeline alerts, and saves the payload to the local history cache.

---

## 💻 Installation & Setup

### Prerequisites
- Python 3.8+
- A Google Gemini API Key

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn python-dotenv requests
   ```
3. Create a `.env` file in the backend folder and add your API key:
   ```env
   API_KEY=your_gemini_api_key_here
   ```
4. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   *(The server will run at `http://127.0.0.1:8000`)*

### Frontend Setup
1. Simply open `index.html` located in the `frontend/` directory in any modern web browser.
2. Ensure the backend server is running so the frontend can communicate with the local API.

---

## 🎛️ Dashboard Shortcuts

- Press `A` - Instantly open the Analyze Shipment tab.
- Press `D` - Return to the Main Dashboard.
- Press `/` - Open the global Command Palette.
- Press `ESC` - Close active overlays or chat panels.

---

## 📌 Status

The core infrastructure and enterprise UI are fully stable and deployed locally.

**Upcoming Roadmap**:
- Integration with live real-world shipping API providers (e.g., Mapbox, MarineTraffic).
- Migrating the local session storage to a fully managed PostgreSQL database.
- Multi-user JWT authentication.

---
*Built for the future of global logistics.*
