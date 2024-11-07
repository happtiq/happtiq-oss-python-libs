#!/bin/bash

# Function to prompt for confirmation with Y as the default
confirm() {
    read -p "$1 (Y/n): " choice
    choice=${choice:-y}  # Default to 'y' if no input is provided
    case "$choice" in 
        y|Y ) return 0;;
        * ) echo "Aborted."; exit 1;;
    esac
}

# Function to validate semantic versioning
validate_version() {
    if [[ ! $1 =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        echo "Error: Version must follow semantic versioning (e.g., v1.0.0)."
        exit 1
    fi
}

# Ask for the version number
read -p "Enter the version number for the release (e.g., v1.0.0): " version

# Validate the version input
validate_version "$version"

# Confirm the version input
confirm "You entered version $version. Do you want to proceed?"

# Create a Git tag
confirm "Create the Git tag $version?"
git tag -a "$version" -m "Release $version"

# Push the Git tag to the repository
confirm "Push the tag $version to the remote repository?"
git push origin "$version"

echo "Release $version has been tagged and pushed successfully."
