# 🎯 Real-Time Auction Platform (Django + Channels)

A real-time auction system built with Django, Django REST Framework, and Django Channels.  
It allows users to place bids on items and receive live updates via WebSockets.

## Tech Stack
- Python 3.12+
- Django 5.x
- Django REST Framework
- Django Channels
- Redis (or InMemoryChannelLayer for local dev)
- Daphne (ASGI server)

## Installation

```bash
git clone https://github.com/yourusername/live_auction.git
cd live_auction
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

