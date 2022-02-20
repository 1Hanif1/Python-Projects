class FlightData:
    def __init__(self, **kwargs) -> None:
        self.price = kwargs["price"],
        self.origin_city = kwargs['origin_city'],
        self.origin_airport = kwargs["origin_airport"],
        self.destination_city = kwargs["destination_city"],
        self.destination_airport = kwargs["destination_airport"],
