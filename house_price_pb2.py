# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: house_price.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11house_price.proto\x12\nhouseprice\"\xa1\x01\n\rHouseFeatures\x12\x0e\n\x06MedInc\x18\x01 \x01(\x02\x12\x10\n\x08HouseAge\x18\x02 \x01(\x02\x12\x10\n\x08\x41veRooms\x18\x03 \x01(\x02\x12\x11\n\tAveBedrms\x18\x04 \x01(\x02\x12\x12\n\nPopulation\x18\x05 \x01(\x02\x12\x10\n\x08\x41veOccup\x18\x06 \x01(\x02\x12\x10\n\x08Latitude\x18\x07 \x01(\x02\x12\x11\n\tLongitude\x18\x08 \x01(\x02\")\n\x0fPricePrediction\x12\x16\n\x0epredictedPrice\x18\x01 \x01(\x02\x32_\n\x13HousePricePredictor\x12H\n\x0cPredictPrice\x12\x19.houseprice.HouseFeatures\x1a\x1b.houseprice.PricePrediction\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'house_price_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HOUSEFEATURES']._serialized_start=34
  _globals['_HOUSEFEATURES']._serialized_end=195
  _globals['_PRICEPREDICTION']._serialized_start=197
  _globals['_PRICEPREDICTION']._serialized_end=238
  _globals['_HOUSEPRICEPREDICTOR']._serialized_start=240
  _globals['_HOUSEPRICEPREDICTOR']._serialized_end=335
# @@protoc_insertion_point(module_scope)
