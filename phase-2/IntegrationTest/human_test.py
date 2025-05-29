# @Authors
# Student Names: Barış Türker, Gökçe Akca, Necip Baha Sağıroğlu
# Student IDs: 150170113, 150210046, 150220727

from __future__ import annotations

import unittest

from geometry_toolkit import GeometryToolkit, Point


class TestGeometryToolkitIntegration(unittest.TestCase):

    def setUp(self) -> None:
        self.tk = GeometryToolkit()

    # ------------------------------------------------------------------
    def test_nominal_flow_distance_area_and_inclusion(self) -> None:
        # 5‑12‑13 right triangle wholly inside an ample bounding box
        p1: Point = (0.0, 0.0)
        p2: Point = (5.0, 12.0)
        p3: Point = (5.0, 0.0)
        box = [(-1.0, -1.0), (10.0, -1.0), (10.0, 20.0), (-1.0, 20.0)]

        self.assertAlmostEqual(self.tk.distance(p1, p2), 13.0)
        self.assertAlmostEqual(self.tk.triangle_area(p1, p2, p3), 30.0)

        for pt in (p1, p2, p3):
            with self.subTest(pt=pt):
                self.assertTrue(self.tk.point_in_polygon(pt, box))

    # ------------------------------------------------------------------
    def test_triangle_area_colinear_raises(self) -> None:
        colinear = [(0.0, 1.0), (2.0, 1.0), (4.0, 1.0)]  # horizontal line
        with self.assertRaises(ValueError):
            self.tk.triangle_area(*colinear)

    # ------------------------------------------------------------------
    def test_point_in_polygon_boundary_counts_as_inside(self) -> None:
        rectangle = [(0.0, 0.0), (6.0, 0.0), (6.0, 2.0), (0.0, 2.0)]
        pt_on_edge: Point = (3.0, 0.0)  # midpoint of the bottom edge
        self.assertTrue(self.tk.point_in_polygon(pt_on_edge, rectangle))

    # ------------------------------------------------------------------
    def test_malformed_polygon_duplicate_vertices_raises(self) -> None:
        bad_poly = [(-2.0, 0.0), (-1.0, 0.0), (-1.0, 0.0), (-2.0, 1.0)]
        with self.assertRaises(ValueError):
            self.tk.point_in_polygon((-1.5, 0.5), bad_poly)

    # ------------------------------------------------------------------
    def test_smoke_varied_numbers_and_concave_polygon(self) -> None:
        # Distance using a (10, 24, 26) triple.
        self.assertAlmostEqual(self.tk.distance((-5, -1), (5, 23)), 26.0)

        concave_poly = [
            (-3.0, -2.0),  # base left
            (3.0, -2.0),   # base right
            (3.0, 3.0),    # top right
            (0.0, 0.0),    # inward dent (concavity)
            (-3.0, 3.0),   # top left
        ]

        # Inside body.
        self.assertTrue(self.tk.point_in_polygon((-1.0, -1.0), concave_poly))

        # Inside the dent (still inside for even‑odd rule).
        self.assertTrue(self.tk.point_in_polygon((0.5, 0.5), concave_poly))

        # Outside point.
        self.assertFalse(self.tk.point_in_polygon((4.0, 0.0), concave_poly))

        # Triangle area with fresh coordinates.
        area = self.tk.triangle_area(concave_poly[0], concave_poly[1], (-1.0, -1.0))
        self.assertGreater(area, 0.0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
