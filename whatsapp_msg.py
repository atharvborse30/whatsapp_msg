import pywhatkit

def send_whatsapp_message():
    try:
        # Get input from user
        phone_number = input("Enter the recipient's phone number (including country code): ")
        message = input("Enter the message you want to send: ")
        time_hour = int(input("Enter the hour (in 24-hour format) at which you want to send the message: "))
        time_minute = int(input("Enter the minute at which you want to send the message: "))

        # Send the message
        pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute)
        print("WhatsApp message sent successfully!")
    except Exception as e:
        print("An error occurred while sending the WhatsApp message.")
        print(e)

send_whatsapp_message()
