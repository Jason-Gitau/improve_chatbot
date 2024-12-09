print("Hello, I am Mason,your trusted ai assistant.Press 'EXIT' to stop")



while True:
    user_input= input("you ").lower()
    
    if user_input=="exit":
        break

    if 'hello' in user_input:
        print(" hey there how can i help you today?")

    if 'name' in user_input:
        print(" am Mason,you ai bot assistant")
    
    if 'how are you' in user_input:
        print("well, am just a bot, but am doing great ")
        reply= input(",how are you ? ").lower()

        if 'good' in reply:
            print("perfect!")
           
        else:
            print('sorry')
          
