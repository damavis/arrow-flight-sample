import pyarrow as pa
import pyarrow.flight as flight
import pandas as pd


def put_data(client, file_path):
    df = pd.read_csv(file_path)
    table = pa.Table.from_pandas(df)

    descriptor = flight.FlightDescriptor.for_path(file_path)

    writer, _ = client.do_put(descriptor, table.schema)
    writer.write_table(table)
    writer.close()
    print(f"Uploaded {file_path} to the server.")


def get_data(client, file_path):
    ticket = flight.Ticket(file_path.encode('utf-8'))
    reader = client.do_get(ticket)

    table = reader.read_all()
    df = table.to_pandas()

    print(f"Downloaded data for {file_path}:")
    print(df)


def list_flights(client):
    print("Listing:")
    for flight_info in client.list_flights():
        print(f"Descriptor: {flight_info.descriptor.path[0].decode('utf-8')}")


def main():
    client = flight.FlightClient("grpc://127.0.0.1:5005")

    file_path = "sample.csv"

    put_data(client, file_path)
    get_data(client, file_path)
    list_flights(client)


if __name__ == "__main__":
    main()
