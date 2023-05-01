<div align="center">

<h1>Template | Worker</h1>

[![Docker Image](https://github.com/runpod-workers/worker-template/actions/workflows/CD-docker_dev.yml/badge.svg)](https://github.com/runpod-workers/worker-template/actions/workflows/CD-docker_dev.yml)

🚀 | A simple worker that can be used as a starting point to build your own custom RunPod Endpoint API worker.
</div>

## 📖 | Getting Started

1. Clone this repository.
2. Add your code to the `src` directory.
3. Update the `handler.py` file to load models and process requests.
4. Add any dependencies to the `requirements.txt` file.
5. Add any other build time scripts to the`builder` directory, for example, downloading models.
6. Update the `Dockerfile` to include any additional dependencies.

### CI/CD

This repository is setup to automatically build and push a docker image to the GitHub Container Registry. You will need to add the following to the GitHub Secrets for this repository to enable this functionality:

- `DOCKERHUB_USERNAME` | Your DockerHub username for logging in.
- `DOCKERHUB_TOKEN` | Your DockerHub token for logging in.
- `DOCKERHUB_REPO` | The name of the repository you want to push to.
- `DOCKERHUB_IMG` | The name of the image you want to push to.

The `CD-docker_dev.yml` file will build the image and push it to the `dev` tag, while the `CD-docker_release.yml` file will build the image on releases and tag it with the release version.

## Best Practices

Models should be part of your docker image, this can be accomplished by either copying them into the image or downloading them during the build process.

If using the input validation utility from the runpod python package, create a `schemas` python file where you can define the schemas, then import that file into your `handler.py` file.
