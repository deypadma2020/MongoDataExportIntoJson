import os
import json
from db.connection import client
from dotenv import load_dotenv
from bson import json_util

load_dotenv()

def export_coll_to_json(output_dir: str = "production_data/raw_data_dump"):
    output_dir = os.path.abspath(output_dir)
    os.makedirs(output_dir, exist_ok=True)
    print(f"Folder created successfully at {output_dir}")

    db = client['db_name']
    collection_names = db.list_collection_names()
    print("Collections found:", collection_names)

    for coll_name in collection_names:
        collection = db[coll_name]
        documents = list(collection.find({}))

        print(f"Checking {coll_name}: {len(documents)} docs found")

        if not documents:
            continue

        output_path = os.path.join(output_dir, f"{coll_name}.json")

        # Use bson.json_util to handle ObjectId, datetime, etc.
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(json_util.dumps(documents, indent=4))

        print(f"Exported {coll_name} to {output_path}")


if __name__ == "__main__":
    export_coll_to_json()
