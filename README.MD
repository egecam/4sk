# 4SK

### Free & Open Source AI Assistance CLI for Everyone

4SK is a free and open source AI assistance CLI that can help you with your daily tasks. It is designed to be simple and easy to use. 4SK is built using Python and the GPT4All library. The CLI uses Mistral 7b as the default model, but you can change it to any other GPT4All compatible model that you want.
4SK is still in development and we are constantly adding new features and improving the existing ones.

### Features

- **Simple and easy to use**
  Just type `4sk` in your terminal and you are ready to ask daily questions.
- **Free and open source**
  4SK is free and open source. You can use it for free and you can also contribute to the project.
- **Secure and private**
  4SK does not store any of your data. Your data is safe and secure in your hands.

### Installation

1. Clone the repository
   ```sh
   git clone
   ```
2. Install the dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Run the CLI

   ```sh
   python main.py
   ```

   1. If you want to run the CLI with a specific keyword, you may want to add the following line to your `.bashrc` or `.zshrc` file by `nano ~/.bashrc` or `nano ~/.zshrc`

   ```sh
    4sk() {
        python /path/to/4sk/main.py
    }
   ```

   > Note: Don't forget to replace `/path/to/4sk` with the actual path to the 4SK directory. Use python3 if you are using Python 3 instead of Python or on MacOs.

   2. Then you can run the CLI by typing `4sk` in your terminal

   ```sh
   4sk
   ```

4. Enjoy!

### Usage

- **Ask a question**
  You can ask any question to 4SK and it will try to answer it for you.
- **Get help**
  You can get all commands by typing `/help`.
- **Save a conversation**
  You can save a conversation by typing `/save`. Saved conversations will be stored in the application directory.
- **Load a conversation**
  You can load a conversation by typing `/load {filepath}`. You should replace `{filepath}` with the actual path to the conversation file.
- **Clear the conversation history**
  You can clear the conversation history by typing `/clear`.
- **Reload 4SK**
  You can reload 4SK by typing `/reload`. This will reload the application and clear the conversation history. So, be careful when using this command. It is useful after you change the model.
- **Show the current model**
  You can see the current model that 4SK uses by typing `/model`.
- **Change the model**
  You can change the model that 4SK uses by typing `/model {modelname}` and writing a model name compatible with GPT4All.
- **Exit the CLI**
  You can exit the CLI by typing `quit` _(no slash before!)_ or pressing `Ctrl + C`.

### Changelog

- **Version 0.1.0**
  - Initial release

### Roadmap

- **Version 0.2.0**
  - Redesign the CLI with Click
  - Fix current bugs and issues
  - Add confirmation for reloading the application
  - Add confirmation for clearing the conversation history
  - Add performance metrics
  - Implement user preferences
  - Implement user feedback system
  - Implement model list for changing the model

### Contributing

We welcome contributions to 4SK. If you want to contribute to the project, please read the [CONTRIBUTING](CONTRIBUTING.md) file.

### License

4SK is licensed under GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more information.

### Contact

If you have any questions, suggestions or feedbacks please feel free to contact me at my [e-mail](mailto:egecam000@gmail.com) or on [Twitter](https://twitter.com/egecamdev).

### Acknowledgements

- [GPT4All](https://gpt4all.com)
- [Mistral 7b](https://gpt4all.com/models/mistral-7b)
- [Python](https://www.python.org)

### Disclaimer

4SK is a free and open source project. It is not affiliated with GPT4All or any other company. It is an independent project created by Ege Çam. The project is still in development and there may be bugs or issues. If you encounter any issues, please report them on the [GitHub Issues](https://github.com/egecam/4sk/issues) page.
