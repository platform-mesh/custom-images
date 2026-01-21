# Contributing to platform-mesh
We want to make contributing to this project as easy and transparent as possible.

## Repository Structure

This repository contains custom container images used by the platform-mesh project.

### Images

| Image | Description | Location |
|-------|-------------|----------|
| `ocmbuilder` | Development environment with Go, kubectl, Helm, yq, and OCM CLI for Open Component Model workflows | `images/ocmbuilder/` |

### Workflows

| Workflow | Trigger | Description |
|----------|---------|-------------|
| `build-ocmbuilder.yml` | Push/PR to `main` affecting `images/ocmbuilder/**`, or manual dispatch | Builds and pushes multi-arch (amd64, arm64) image to `ghcr.io` |

### Adding a New Image

1. Create a directory under `images/<image-name>/`
2. Add a `Dockerfile` with multi-architecture support using `$BUILDPLATFORM` and `$TARGETARCH` build arguments
3. Create a GitHub Actions workflow in `.github/workflows/build-<image-name>.yml`
4. Use pinned action versions with commit SHAs (see existing workflows for reference)

## Our development process
We use GitHub to track issues and feature requests, as well as accept pull requests.

## Pull requests
You are welcome to contribute with your pull requests. These steps explain the contribution process:

1. Fork the repository and create your branch from `main`.
1. Add tests for your code.
1. If you've changed APIs, update the documentation. 
1. Make sure the tests pass. Our github actions pipeline is running the unit and e2e tests for your PR and will indicate any issues.
1. Sign the Developer Certificate of Origin (DCO).

## Issues
We use GitHub issues to track bugs. Please ensure your description is
clear and includes sufficient instructions to reproduce the issue.

## License
By contributing to platform-mesh, you agree that your contributions will be licensed
under its [Apache-2.0 license](LICENSE).
