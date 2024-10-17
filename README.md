
# Arrow Flight Simple Server and Client

## Overview

This project demonstrates a simple implementation of a server-client architecture using Apache Arrow Flight, a framework designed for high-performance data transfer. The project consists of a Flight server (`server.py`) that stores uploaded data and a Flight client (`client.py`) that can upload, download, and list available datasets.

## Requirements

- Python 3.x
- `poetry`

You can install the required packages using pip:

```bash
pip install poetry
poetry install
```

## Server

### `server.py`

The server allows clients to upload data and retrieve it using a unique ticket. The server implements three main methods:

- **do_put**: Receives data from clients and stores it.
- **do_get**: Returns stored data based on a provided ticket.
- **list_flights**: Lists all available datasets on the server.

### Usage

To run the server, execute the following command:

```bash
python server.py
```

The server will start and listen for incoming connections on `grpc://0.0.0.0:5005`.

## Client

### `client.py`

The client provides functionality to interact with the server. It can upload CSV files, download datasets, and list available flights. The client implements the following functions:

- **put_data(client, file_path)**: Reads a CSV file, converts it to an Arrow table, and uploads it to the server.
- **get_data(client, file_path)**: Requests data from the server using a ticket and converts it back to a Pandas DataFrame.
- **list_flights(client)**: Lists all datasets available on the server.

### Usage

To run the client, execute the following command after the server is running:

```bash
python client.py
```

Make sure to update the `file_path` variable in `client.py` to point to a valid CSV file that you want to upload.

## Example

1. Start the server by running `python server.py`.
2. In another terminal, run the client with `python client.py`.

The client will:
- Upload the specified CSV file to the server.
- Download the uploaded data and print it to the console.
- List all available datasets on the server.

## Conclusion

This project provides a straightforward example of using Apache Arrow Flight for high-performance data transfer between a server and client. It can be extended to support more advanced features such as data querying, error handling, and authentication.

Feel free to explore and modify the code to suit your needs!

--- 

This README includes sections to describe the purpose, installation requirements, server and client functionalities, usage instructions, and an example of how to run the server and client. You can adapt it further to include any additional information or usage scenarios relevant to your project!