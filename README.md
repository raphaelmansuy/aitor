# AITor 🛐 

aitor is a Python package designed to provide a collection of tools and utilities for AI-related tasks. 

This includes functionalities for model handling, downloading, and management. The project is organized following Python packaging conventions and uses Poetry for dependency management.

![logo aitor](./assets/logo128x128.png)

## Table of Contents

- [Building the Project](#building-the-project)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Building the Project

Install with poetry

```bash
poetry install
```

## Build and install using pipx 

```bash
poetry build
pipx install . --force
```


## Usage

```bash
Usage: aitor [OPTIONS] COMMAND [ARGS]...

  An AI toolbox for working with Hugging Face Hub.

  Tor stands for Torii 🛐, a Japanese gate, suggesting a gateway to AI.

Options:
  --help  Show this message and exit.

Commands:
  download  Downloads a specific version of a model from Hugging Face Hub.
  list      Lists all the files for a specific version of a model from...
```

### Examples


#### List all the files of a model on HuggingFace 🤗
```bash
aitor list --model stabilityai/stablelm-2-1_6b-zephyr 
```

Result:

```bash
.gitattributes
LICENSE
README.md
config.json
configuration_stablelm.py
generation_config.json
merges.txt
model.safetensors
modeling_stablelm.py
special_tokens_map.json
stablelm-2-zephyr-1_6b-OpenVINO-4bit.bin
stablelm-2-zephyr-1_6b-OpenVINO-4bit.xml
stablelm-2-zephyr-1_6b-Q4_0.gguf
stablelm-2-zephyr-1_6b-Q4_1.gguf
stablelm-2-zephyr-1_6b-Q5_K_M.gguf
stablelm-2-zephyr-1_6b-Q8_0.gguf
stablelm-2-zephyr-1_6b.gguf
tokenizer.json
tokenizer_config.json
vocab.json
```

#### Download a specific file

```bash
aitor download --model stabilityai/stablelm-2-1_6b-zephyr --file stablelm-2-zephyr-1_6b-Q4_0.gguf
```

By default files are downloaded in the current directory under "model".

### Download a full model

```bash
aitor download --model stabilityai/stablelm-2-1_6b-zephyr
```


## Licence

[MIT](./LICENCE.md)