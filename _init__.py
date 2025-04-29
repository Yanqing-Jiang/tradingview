import logging
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Received TradingView webhook")

    try:
        data = req.get_json()

        # Forward to your local server or Azure VM
        target_url = "http://<YOUR_PUBLIC_ENDPOINT>:5000/webhook"
        response = requests.post(target_url, json=data)

        return func.HttpResponse(f"Forwarded: {response.status_code}", status_code=200)
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse("Error processing request", status_code=500)
