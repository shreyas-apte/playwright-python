# Define custom function directory
ARG FUNCTION_DIR="/function"

FROM python:3.12-slim AS build-image

# Include global arg in this stage of the build
ARG FUNCTION_DIR

# Copy function code
RUN mkdir -p ${FUNCTION_DIR}
COPY . ${FUNCTION_DIR}

# Copy requirements
COPY ./requirements.txt .

# Set the PLAYWRIGHT_BROWSERS_PATH environment variable
ENV PLAYWRIGHT_BROWSERS_PATH=/opt/playwright-browsers

# RUN pip cache purge

RUN pip install --no-cache-dir --upgrade pip

# Install the function's dependencies
# RUN pip install --target ${FUNCTION_DIR} awslambdaric
# RUN pip --no-cache-dir install -r requirements.txt --target ${FUNCTION_DIR}

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR ${FUNCTION_DIR}

RUN rm -rf ~/.cache/ms-playwright
# RUN playwright install-deps
# RUN playwright install
RUN playwright install --with-deps --only-shell chromium

# Set runtime interface client as default command for the container runtime
ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
# Pass the name of the function handler as an argument to the runtime
CMD [ "lambda_function.lambda_handler" ]
