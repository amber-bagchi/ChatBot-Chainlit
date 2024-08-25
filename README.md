# 🍕 Zomato Chatbot
Welcome to the Zomato Chatbot project! This chatbot is designed to enhance your food ordering experience by providing restaurant recommendations, helping you build your order, and guiding you through the checkout process—all through a conversational interface.

## 🌟 Features
- 🧠 LLM-Powered Responses
The chatbot leverages advanced language models to understand your queries and respond accurately.

- 🎤 Voice Input
Interact with the chatbot using your voice for a hands-free experience.

- 🛍️ Order Management
Easily add food items to your cart and review your order before checkout.

- 🌍 Restaurant Search
Find the best restaurants based on your location and preferences.

- 🍽️ Cuisine Recommendations
Discover popular dishes and cuisines tailored to your taste.

- 🛒 Cart Management
Add, remove, and review items in your cart before confirming your order.

## 🚀 Getting Started
Prerequisites
Make sure you have the following installed:

- Python 3.7+
- ChainLit
- Google Generative AI API Key
  
### Clone the Repository:
```bash
git clone https://github.com/yourusername/zomato-chatbot.git
```

```bash
cd zomato-chatbot
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables:

Create a .env file in the root directory and add your API keys:

```bash
GOOGLE_API_KEY=your_google_api_key
```

### Run the Application:

```bash
chainlit run app.py
```

### Access the Chatbot:

Open your browser and go to http://localhost:5000 to start interacting with the chatbot.

## 📚 How It Works
- User Interaction: The chatbot greets the user and collects the order details.
- Order Summary: The bot summarizes the order, asks for any additional items, and confirms whether it's a pickup or delivery.
- Final Steps: The bot collects the delivery address (if required) and processes the payment.
  
## 🤖 Example Interactions
User: "I want to order a pizza."

Chatbot: "Great choice! We have Cheese Pizza, Pepperoni Pizza, and more. Which one would you like?"

User: "Cheese Pizza, please."

Chatbot: "Cheese Pizza has been added to your cart. Would you like to add anything else?"

User: "No, that's all."

Chatbot: "Would you like this order for pickup or delivery?"

## 📸 Video

Here is a Video of the application:
![Zomato_Chatbot-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/af576158-16cf-4423-bbc7-55510a074ea8)


## 🛠️ Built With
- Chainlit - For building and deploying conversational AI.
- Google Generative AI - For natural language understanding and response generation.
  
## 🤝 Contributing
We welcome contributions! Please feel free to fork this repository, make improvements, and submit pull requests.

## 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
