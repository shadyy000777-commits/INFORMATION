from flask import Flask, request, render_template
import requests
import sqlite3

app = Flask(__name__)

# Create a SQLite database and table if it doesn't exist
def init_db():
    conn = sqlite3.connect('ip_tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ip_data
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   ip_address TEXT,
                   city TEXT,
                   region TEXT,
                   country TEXT,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return "IP Tracker: Visit /track to log your IP."

@app.route('/track')
def track():
    # Get the user's IP address
    ip_address = request.remote_addr
    
    # Fetch geolocation data using ip-api.com
    response = requests.get(f'http://ip-api.com/json/{ip_address}')
    data = response.json()
    
    # Insert the data into the database
    conn = sqlite3.connect('ip_tracker.db')
    c = conn.cursor()
    c.execute("INSERT INTO ip_data (ip_address, city, region, country) VALUES (?, ?, ?, ?)",
              (ip_address, data['city'], data['regionName'], data['country']))
    conn.commit()
    conn.close()
    
    # Return the geolocation data as JSON
    return {
        "ip_address": ip_address,
        "city": data['city'],
        "region": data['regionName'],
        "country": data['country']
    }

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
