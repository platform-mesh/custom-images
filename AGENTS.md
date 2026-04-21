## Repository Description
- `custom-images` contains custom utility container images used by Platform Mesh.
- The main moving parts are image definitions under `images/` and GitHub Actions workflows under `.github/workflows/` that build and publish those images.
- Read the org-wide [AGENTS.md](https://github.com/platform-mesh/.github/blob/main/AGENTS.md) for general conventions.

## Core Principles
- Keep image changes small, deterministic, and easy to review.
- Preserve multi-architecture build behavior and reproducible tool installation where possible.
- Prefer extending existing image and workflow patterns over inventing one-off build logic.
- Keep this file focused on agent execution and repository-specific constraints.

## Project Structure
- `images/httpbin/`: image definition and helper script for the custom httpbin image.
- `images/ocmbuilder/`: toolbox image for OCM-related workflows and local development support.
- `.github/workflows/`: image build and publish automation.
- `README.md` and `CONTRIBUTING.md`: high-level maintainer guidance.

## Architecture
This is an image-build repo, not an application runtime.

### Build model
- Each image lives in its own directory under `images/`.
- GitHub Actions workflows are the supported path for building and publishing multi-arch images.
- Utility scripts under an image directory are part of that image's build contract and should stay in sync with the Dockerfile.

### Risk areas
- Small Dockerfile or helper-script changes can break build reproducibility, runtime behavior, or architecture-specific installs.
- Be careful when changing base images, download sources, or tool installation logic.

## Commands
- `docker build images/httpbin` — local fallback for validating the httpbin image.
- `docker build images/ocmbuilder` — local fallback for validating the ocmbuilder image.
- Review `.github/workflows/build-*.yml` together with the corresponding `images/<name>/` directory when changing image behavior.

## Code Conventions
- Keep Dockerfiles readable and explicit about installed tools and versions.
- Prefer helper scripts inside the image directory when logic is too large for a clean Dockerfile step.
- Update contribution docs when image layout or workflow expectations change.

## Generated Artifacts
- Published container images are workflow outputs; avoid treating the repo as a place for generated binary artifacts.

## Do Not
- Introduce unpinned or opaque downloads without a clear reason.
- Change image names, tags, or workflow triggers casually.
- Commit secrets or credentials.

## Hard Boundaries
- Ask before making changes that alter published image naming, supported architectures, or registry targets.
- Be especially careful with tool installation scripts in `images/ocmbuilder/`.

## Human-Facing Guidance
- Use `README.md` for local certificate setup, startup arguments, and service context.
- Use `CONTRIBUTING.md` for contribution process, DCO, and broader developer workflow expectations.
