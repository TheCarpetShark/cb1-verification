import time

class HHOGenerator:
    def __init__(self):
        self.host = "192.168.0.1"  # Modify based on actual device IP
        self.port = 80
        self.status_url = f"http://{self.host}/{self.port}/status"
        
    def setup(self, password="ffffffff"):
        print("Setting up as Wi-Fi hotspot...")
        time.sleep(2)
        try:
            response = requests.get(f"http://localhost:5173")
            if response.status_code == 200:
                print("Connected to device.")
            else:
                raise Exception("Failed to connect.")
        except requests.exceptions.RequestException:
            print("Connection failed. Please ensure IP is correct and try again.")

    def display_status(self):
        while True:
            try:
                response = requests.get(self.status_url)
                if response.status_code == 200:
                    data = response.json()
                    print(f"Connected device LED status: {data['led']}")
                else:
                    raise Exception("Failed to fetch status.")
            except requests.exceptions.RequestException as e:
                print(f"Error fetching status. Trying again in 5 seconds: {e}")

    def run(self):
        self.setup()
        while True:
            time.sleep(2)
            self.display_status()

# Start the hotspot module
if __name__ == "__main__":
    hho = HHOGenerator()
    hho.run()
