import time
import grpc
import house_price_pb2
import house_price_pb2_grpc
import asyncio
import random

async def predict_price(stub, features, index):
    response = await stub.PredictPrice(house_price_pb2.HouseFeatures(
        MedInc=features[0],
        HouseAge=features[1],
        AveRooms=features[2],
        AveBedrms=features[3],
        Population=features[4],
        AveOccup=features[5],
        Latitude=features[6],
        Longitude=features[7]
    ))
    # print(f"Index #{index} --> Predicted House Price: ${response.predictedPrice}")


async def run():
    start_time = time.time()
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = house_price_pb2_grpc.HousePricePredictorStub(channel)

        # Generate 15 sets of random features
        features_list = [
            [random.uniform(1.0, 10.0),  # MedInc
             random.uniform(1.0, 50.0),  # HouseAge
             random.uniform(1.0, 10.0),  # AveRooms
             random.uniform(1.0, 5.0),   # AveBedrms
             random.uniform(100.0, 1000.0),  # Population
             random.uniform(1.0, 5.0),   # AveOccup
             random.uniform(32.0, 42.0),  # Latitude
             random.uniform(-124.0, -114.0)]  # Longitude
            for _ in range(pow(10, 4))
        ]

        # Create a list of asyncio tasks for concurrent requests
        tasks = [predict_price(stub, features, index) for index, features in enumerate(features_list)]

        # Wait for all tasks to complete
        await asyncio.gather(*tasks)
    end_time = time.time()
    print(f"Elapsed Time", (end_time-start_time))

if __name__ == '__main__':
    asyncio.run(run())


# pow(10, 4)
# - MaxWorker=10 --> 13.097135066986084
