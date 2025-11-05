import logging
import os
from datetime import datetime

# 1️⃣ Create a timestamped log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2️⃣ Define logs directory
logs_path = os.path.join(os.getcwd(), "logs")

# 3️⃣ Create the directory if it doesn’t exist
os.makedirs(logs_path, exist_ok=True)

# 4️⃣ Define full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# 5️⃣ Configure the global logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s %(levelname)s %(message)s",
    level=logging.INFO,
)

# Optional: print path so you know where logs are stored
print(f"✅ Logs will be saved to: {LOG_FILE_PATH}")
