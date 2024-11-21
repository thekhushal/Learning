import pywhatkit as kit
import time

# Function to send the same message multiple times
def spam_whatsapp(phone_number, message, count):
    for i in range(count):
        kit.sendwhatmsg_instantly(phone_number, message)
        time.sleep(5)  # Wait for 5 seconds to avoid spamming too fast

# Example usage
phone_number = "+919828012393"  # Replace with recipient's phone number (with country code)
message = "TOe Whatsapp dekh na"  # Replace with your message
spam_whatsapp(phone_number, message, 100)  # Send the message 100 times
