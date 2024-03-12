from concurrent import futures
from grpc_health.v1 import health
from grpc_health.v1 import health_pb2
from grpc_health.v1 import health_pb2_grpc
import grpc
import house_price_pb2
import house_price_pb2_grpc
import pickle
import numpy as np
import logging

class HousePricePredictorServicer(house_price_pb2_grpc.HousePricePredictorServicer):
    def __init__(self):
        logging.info("Loading model...")
        with open('model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        logging.info("Model loaded...")

    def PredictPrice(self, request, context):
        # Extract features from the request
        logging.info("Request recieved...")
        
        features = np.array([
            request.MedInc,
            request.HouseAge,
            request.AveRooms,
            request.AveBedrms,
            request.Population,
            request.AveOccup,
            request.Latitude,
            request.Longitude
        ]).reshape(1, -1)  # Reshape for a single sample

        logging.info(f"Request: {features}")

        logging.info("Model evaluating...")

        # Use the loaded model to make a prediction
        predicted_price = self.model.predict(features)[0]
        
        logging.info("Model evaluated...")
        
        return house_price_pb2.PricePrediction(predictedPrice=predicted_price)

def _configure_health_server(server):
    health_servicer = health.HealthServicer(
        experimental_non_blocking=True,
        experimental_thread_pool=futures.ThreadPoolExecutor(max_workers=10),
    )
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    house_price_pb2_grpc.add_HousePricePredictorServicer_to_server(HousePricePredictorServicer(), server)
    server.add_insecure_port('[::]:50051')
    _configure_health_server(server)
    logging.info("Starting server...")
    server.start()

    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] | %(message)s",
        handlers=[logging.StreamHandler()]
    )
    logging.info("App starting...")
    serve()
