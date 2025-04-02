from characterai import aiocai
import asyncio
import serial

async def main():
    char = "YntB_ZeqRq2l_aVf2gWDCZl4oBttQzDvhj9cXafWcF8"

    client = aiocai.Client('API_KEY')

    arduino = serial.Serial('COM7', 9600, timeout=1)  # Replace with correct port

    me = await client.get_me()  # Fetch the user object

    async with await client.connect() as chat:
        new, answer = await chat.new_chat(char, me.id)  # Now me.id is defined

        print(f'{answer.name}: {answer.text}')
        
        while True:
            if arduino.in_waiting:  # Check if data is available
                text = arduino.readline().decode('utf-8').strip()
                
                if text:  # Only send a message if text is received
                    message = await chat.send_message(char, new.chat_id, text)
                    print(f'{message.name}: {message.text}')
            
            await asyncio.sleep(0.1)  # Prevent CPU overload

asyncio.run(main())
