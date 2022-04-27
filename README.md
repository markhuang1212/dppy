# dppy

Repository for the FYT project

## Installation

For the first step, download the file `Books.csv` by doing

```bash
wget -O Books.csv https://hmpg.dev/books.csv
```

# Run in docker

You need

* Docker
* VSCode
* VSCode - Remote Container Extension

VSCode will prompt you to open the project in a docker container. All dependencies will be installed automatically upon first run.

# Install Dependencies Manually

Refer to the `.devcontainer` folder to see what dependencies are needed to run the project.

## Project Structure

The experiment and graph generation is in the `main.ipynb`. 

The experiment related to the `discussion` part of the thesis is in `discussion.ipynb`.

The implementation of the algorithms are in `.py` files.
