import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Get the Slack webhook URL from the GitHub secret
slack_webhook_url = os.environ['SLACK_WEBHOOK_URL']

# Function to send the SSL expiry alert notification to Slack
def send_slack_notification(domain, remaining_days):
    message = f"SSL Expiry Alert\n"\
              f"  * Domain: {domain}\n"\
              f"  * Warning: The SSL certificate for {domain} will expire in {remaining_days} days."
    
    try:
        # Create a Slack client
        client = WebClient(token=slack_webhook_url)
        
        # Send the message to the Slack channel
        response = client.chat_postMessage(channel='#your-channel-name', text=message)
        
        # Check if the message was sent successfully
        if response['ok']:
            print("SSL expiry alert sent successfully to Slack!")
        else:
            print("Failed to send SSL expiry alert to Slack.")
    
    except SlackApiError as e:
        # Handle any errors that occur during the Slack notification
        print(f"Error sending Slack notification: {e.response['error']}")

