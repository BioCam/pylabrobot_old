import unittest

from pylabrobot.liquid_handling.resources import HTF_L, Cos_96_EZWash
from pylabrobot.liquid_handling.standard import (
  Pickup,
  Drop,
  Aspiration,
  Dispense,
)


class TestStandard(unittest.TestCase):
  """ Test for standard form classes. """

  def setUp(self) -> None:
    self.tip_rack = HTF_L("tiprack")
    self.plate = Cos_96_EZWash("plate")

  def test_pick_up_serialize(self):
    self.assertEqual(
      Pickup(
        resource=self.tip_rack.get_item("A1"),
        tip=self.tip_rack.get_tip("A1")
      ).serialize(),
      {
      "resource_name": "tiprack_tipspot_0_0",
      "offset": "default",
      "tip": {
        "type": "HamiltonTip",
        "has_filter": True,
        "total_tip_length": 95.1,
        "maximal_volume": 1065,
        "fitting_depth": 8,
        "pickup_method": "OUT_OF_RACK",
        "tip_size": "HIGH_VOLUME"
      }
    })

  def test_pick_up_deserialize(self):
    self.assertEqual(
        Pickup.deserialize({
          "resource_name": "tiprack_tipspot_0_0",
          "offset": "default",
          "tip": {
            "type": "HamiltonTip",
            "has_filter": True,
            "total_tip_length": 95.1,
            "maximal_volume": 1065,
            "fitting_depth": 8,
            "pickup_method": "OUT_OF_RACK",
            "tip_size": "HIGH_VOLUME"
          }},
          resource=self.tip_rack.get_item("A1"),
        ),
        Pickup(
          resource=self.tip_rack.get_item("A1"),
          tip=self.tip_rack.get_tip("A1")
        )
    )

  def test_drop_serialize(self):
    self.assertEqual(
      Drop(resource=self.tip_rack.get_item("A1"), tip=self.tip_rack.get_tip("A1")).serialize(),
      {
        "resource_name": "tiprack_tipspot_0_0",
        "offset": "default",
        "tip": {
          "type": "HamiltonTip",
          "has_filter": True,
          "total_tip_length": 95.1,
          "maximal_volume": 1065,
          "fitting_depth": 8,
          "pickup_method": "OUT_OF_RACK",
          "tip_size": "HIGH_VOLUME"
        }
      })

  def test_drop_deserialize(self):
    self.assertEqual(Drop.deserialize({
        "resource_name": "tiprack_tipspot_0_0",
        "offset": "default",
        "tip": {
          "type": "HamiltonTip",
          "has_filter": True,
          "total_tip_length": 95.1,
          "maximal_volume": 1065,
          "fitting_depth": 8,
          "pickup_method": "OUT_OF_RACK",
          "tip_size": "HIGH_VOLUME"
        }},
        resource=self.tip_rack.get_item("A1"),
      ),
      Drop(resource=self.tip_rack.get_item("A1"), tip=self.tip_rack.get_tip("A1")))

  def test_aspiration_serialize(self):
    self.assertEqual(Aspiration(resource=self.plate.get_well("A1"), volume=100).serialize(), {
      "resource_name": "plate_well_0_0",
      "offset": "default",
      "volume": 100,
      "flow_rate": "default",
      "liquid_height": 0,
      "blow_out_air_volume": 0,
    })

  def test_aspiration_deserialize(self):
    self.assertEqual(Aspiration.deserialize({
      "resource_name": "plate_well_0_0",
      "offset": "default",
      "volume": 100,
      "liquid_height": 0,
      "blow_out_air_volume": 0,
      "flow_rate": "default"}, resource=self.plate.get_well("A1")),
      Aspiration(resource=self.plate.get_well("A1"), volume=100))

  def test_dispense_serialize(self):
    self.assertEqual(Dispense(resource=self.plate.get_well("A1"), volume=100).serialize(), {
      "resource_name": "plate_well_0_0",
      "offset": "default",
      "volume": 100,
      "flow_rate": "default",
      "liquid_height": 0,
      "blow_out_air_volume": 0,
    })

  def test_dispense_deserialize(self):
    self.assertEqual(Dispense.deserialize({
      "resource_name": "plate_well_0_0",
      "offset": "default",
      "volume": 100,
      "liquid_height": 0,
      "blow_out_air_volume": 0,
      "flow_rate": "default"}, resource=self.plate.get_well("A1")),
      Dispense(resource=self.plate.get_well("A1"), volume=100))
