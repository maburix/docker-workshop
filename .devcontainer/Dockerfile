FROM python:3.7

# Copy default endpoint specific user settings overrides into container to specify Python path
COPY .devcontainer/settings.vscode.json /root/.vscode-remote/data/Machine/settings.json


RUN pip install pylint

ENV PYTHONUNBUFFERED 1

RUN mkdir /workspace
WORKDIR /workspace

# Install git, process tools
RUN apt-get update && apt-get -y install git procps

# Install Python dependencies from requirements.txt if it exists
COPY .devcontainer/requirements.txt.temp requirements.txt* /workspace/

RUN if [ -f "requirements.txt" ]; then pip install -r requirements.txt && rm requirements.txt; fi

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
&& rm -rf /var/lib/apt/lists/*