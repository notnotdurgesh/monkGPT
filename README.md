# monkGPT - Philosophical Monk Chatbot

**monkGPT** is a unique web-based chatbot designed to provide heartfelt quotes and philosophical responses like a wise Buddhist monk. Powered by OpenAI's GPT-3.5-Turbo model, this chatbot offers insights and thoughtful reflections on various topics. It also comes with a calming and serene user interface to enhance the monk-like experience.

![monkGPT Screenshot](./monkGPT/demo.png)

## Features

- **Wise Responses:** Receive profound and philosophical quotes and responses reminiscent of a Buddhist monk.
- **GPT-3.5 Integration:** Utilize OpenAI's GPT-3.5-Turbo model for generating insightful and contextually relevant content.
- **Interactive Interface:** Engage with the chatbot through a serene and calming user interface.
- **Inspirational Wisdom:** Seek guidance and thoughtful perspectives on a wide range of topics.

## Live Demo

🚀 **[Experience the Live Demo](https://monkgpt.pythonanywhere.com/)** - monkGPT is currently online and proudly sponsored by PythonAnywhere. Please note that this version is still in beta testing and may have some minor issues as we continue to refine its performance.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/notnotdurgesh/monkGPT.git
   ```

2. Navigate to the project directory:
   ```sh
   cd monkGPT
   ```

3. Install the required Python packages:
   ```sh
   pip install Flask openai
   ```

4. Set up your OpenAI API key:
   - Sign up for an OpenAI account and obtain an API key.
   - Replace `'your-openai-key'` in `app.py` with your actual API key.

## Usage

1. Run the Flask app:
   ```sh
   python app.py
   ```

2. Open a web browser and go to `http://localhost:5000` to access the monkGPT interface.

3. Enter your questions and queries to receive wise and philosophical responses.

## Customization

- **UI Customization:** Modify the chat interface by editing the HTML and CSS files in the `templates` and `static` directories.

- **Bot Responses:** Adjust the monk's wisdom and personality by modifying the `sys_content` in the `app.py` file.

## Contributing

Contributions are welcome! If you have ideas for improvements or find any issues, feel free to open a pull request or submit an issue.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
