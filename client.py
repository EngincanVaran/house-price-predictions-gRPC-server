import grpc
from time import sleep

from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
import house_price_pb2
import house_price_pb2_grpc

def health_check_call(stub: health_pb2_grpc.HealthStub):
    request = health_pb2.HealthCheckRequest(service="")
    resp = stub.Check(request)
    if resp.status == health_pb2.HealthCheckResponse.SERVING:
        print("server is serving")
    elif resp.status == health_pb2.HealthCheckResponse.NOT_SERVING:
        print("server stopped serving")

def run():
    with grpc.insecure_channel('[::]:50051') as channel:
        stub = house_price_pb2_grpc.HousePricePredictorStub(channel)
        health_stub = health_pb2_grpc.HealthStub(channel)
        response = stub.PredictPrice(house_price_pb2.HouseFeatures(
            MedInc=5.0,
            HouseAge=10.0,
            AveRooms=5.0,
            AveBedrms=2.0,
            Population=300.0,
            AveOccup=2.0,
            Latitude=37.0,
            Longitude=-122.0
        ))
        print("Predicted house price: ${}".format(response.predictedPrice))

        for _ in range(30):
            health_check_call(health_stub)
            sleep(1)

if __name__ == '__main__':
    run()
