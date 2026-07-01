# 02 — Azure Functions queue trigger overview
# Run: python 02_azure_queue_trigger.py

if __name__ == "__main__":
    print("Queue trigger runs when message arrives in Azure Storage Queue / Service Bus.")
    print("Use for async processing without managing workers yourself.")
    print("\nPair with: HTTP function enqueues -> Queue function processes")
