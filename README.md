# django_chatbot

OpenAI API Key: Ensure your environment variable for the OpenAI API key is set correctly.
Login Required: The login_required decorator ensures only authenticated users can access the chatbot. Make sure your authentication system is working correctly.
Database Migrations: Ensure your Message model is migrated and the necessary tables are created in the database.

Ensure that the URL pattern for the chatbot view is defined and named home.
Make sure your project's main urls.py includes the app's URLs.
Use the correct URL pattern name in your template.

Container and Layout:

The #chat-container holds the entire chat interface and centers it on the page.
The #chat-history has a fixed height with scrollable content, allowing users to see previous messages.
Message Styling:

Messages from the user have a green background (.user class) and messages from the bot have a red background (.bot class).
Messages are padded and have a slight margin for better readability.
Form Styling:

The input and button in the form are styled for better usability and aesthetics.
The input field expands to fill the available space.
Responsive Design:

Media queries ensure the chat interface is responsive and adjusts for smaller screen sizes.

Welcome Message: Added a welcome message in the #chat-history div.
Modern UI Enhancements:
Fonts and Colors: Updated fonts and colors for a cleaner, more modern look.
Rounded Corners: Added rounded corners to prompts, messages, and form elements for a softer appearance.
Transitions: Added transitions to buttons and prompts for a smoother hover effect.
Layout Adjustments: Improved padding, margins, and flexbox properties for a more polished layout.