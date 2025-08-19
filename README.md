
# MongoDataExportIntoJson

A simple and efficient Python utility to export MongoDB collections into JSON files.  
This project is designed to make it easier to back up MongoDB data or use it for analytics, data migration, or sharing.

---

## 🚀 Features
- Export entire MongoDB collections into JSON format.
- Configure MongoDB connection via `.env` file.
- Lightweight and easy-to-use script.
- Ideal for backups, migrations, and data processing workflows.

---

## 📂 Project Structure
```

├── app/                  # Main application code
├── .env.example          # Example environment variables
├── .gitignore            # Ignore unnecessary files
├── LICENSE               # License file
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies

````

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/deypadma2020/MongoDataExportIntoJson.git
   cd MongoDataExportIntoJson
````
````
2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Copy `.env.example` to `.env` and update with your MongoDB connection string:

   ```ini
   MONGO_URI=mongodb://localhost:27017
   DATABASE_NAME=my_database
   COLLECTION_NAME=my_collection
   OUTPUT_FILE=output.json
   ```

---

## ▶️ Usage

Run the export script:

```bash
python app/main.py
```

This will export the specified MongoDB collection into a JSON file (`output.json` by default).

---

## 📌 Example Output

```json
[
  {
    "_id": "64a7d0e12345abc67890",
    "name": "John Doe",
    "email": "john@example.com",
    "age": 29
  },
  {
    "_id": "64a7d0e12345abc67891",
    "name": "Jane Smith",
    "email": "jane@example.com",
    "age": 34
  }
]
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a PR or raise an issue.

---

## ⭐ Support

If you find this project helpful, don’t forget to **star ⭐ the repo**!
