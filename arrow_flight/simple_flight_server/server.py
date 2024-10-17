import pyarrow as pa
import pyarrow.flight as flight


class SimpleFlightServer(flight.FlightServerBase):
    def __init__(self, location):
        super().__init__(location)
        self.data = {}

    def do_put(self, context, descriptor, reader, writer):
        key = descriptor.path[0] if descriptor.path else descriptor.command
        print(f"Receiving data for descriptor: {key}")
        self.data[key.decode('utf-8')] = reader.read_all()

    def do_get(self, context, ticket):
        key = ticket.ticket.decode()
        print(f"Client requesting data with ticket: {key}")
        if key in self.data:
            return flight.RecordBatchStream(self.data[key])
        else:
            raise KeyError(f"No data for ticket: {key}")

    def list_flights(self, context, criteria):
        for key in self.data.keys():
            yield flight.FlightInfo(
                pa.schema([]),
                flight.FlightDescriptor.for_path(key),
                [],
                -1,
                -1
            )

def main():
    location = "grpc://0.0.0.0:5005"
    server = SimpleFlightServer(location)
    print(f"Serving on {location}")
    server.serve()


if __name__ == "__main__":
    main()
