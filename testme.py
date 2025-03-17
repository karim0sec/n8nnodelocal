from datetime import datetime, UTC

timestamp = datetime.now(UTC).isoformat()+ "Z"
print(timestamp)

