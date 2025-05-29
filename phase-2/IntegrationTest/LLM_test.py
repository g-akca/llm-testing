"""test_geometry_toolkit.py
Integration‑style unit tests for *geometry_toolkit.py* using the builtin
``unittest`` framework.

Each test combines multiple calls where sensible to ensure interactions work
as expected, and it probes both nominal behaviour and edge‑case handling.

Run with::

    python -m unittest test_geometry_toolkit.py
"""
from __future__ import annotations

import math
import unittest

from geometry_toolkit import GeometryToolkit, Point  # type: ignore  # local import


class TestGeometryToolkitIntegration(unittest.TestCase):
    """Integration‑style tests exercising the public API of *GeometryToolkit*."""

    def setUp(self) -> None:
        # Fresh instance for each test (state‑free but explicit).
        self.tk = GeometryToolkit()

    # ------------------------------------------------------------------
    def test_nominal_flow_distance_area_and_inclusion(self) -> None:
        """Happy‑path: distance → area → point‑in‑polygon pipeline."""
        # A right‑triangle inside a unit square
        p1: Point = (0.0, 0.0)
        p2: Point = (3.0, 4.0)
        p3: Point = (3.0, 0.0)
        square = [(0.0, 0.0), (5.0, 0.0), (5.0, 5.0), (0.0, 5.0)]

        # Distance (classic 3‑4‑5 triangle)
        self.assertAlmostEqual(self.tk.distance(p1, p2), 5.0)

        # Area
        self.assertAlmostEqual(self.tk.triangle_area(p1, p2, p3), 6.0)

        # All triangle vertices should lie inside the square
        for pt in (p1, p2, p3):
            with self.subTest(pt=pt):
                self.assertTrue(self.tk.point_in_polygon(pt, square))

    # ------------------------------------------------------------------
    def test_triangle_area_colinear_raises(self) -> None:
        """Colinear points must trigger *ValueError* in *triangle_area*."""
        colinear = [(0.0, 0.0), (1.0, 1.0), (2.0, 2.0)]  # y = x line
        with self.assertRaises(ValueError):
            self.tk.triangle_area(*colinear)

    # ------------------------------------------------------------------
    def test_point_in_polygon_boundary_counts_as_inside(self) -> None:
        """A point exactly on an edge is considered inside."""
        triangle = [(0.0, 0.0), (4.0, 0.0), (2.0, 3.0)]
        pt_on_edge: Point = (1.0, 0.0)  # lies on base edge
        self.assertTrue(self.tk.point_in_polygon(pt_on_edge, triangle))

    # ------------------------------------------------------------------
    def test_malformed_polygon_duplicate_vertices_raises(self) -> None:
        """Duplicate consecutive vertices must raise *ValueError*."""
        bad_poly = [(0.0, 0.0), (1.0, 0.0), (1.0, 0.0), (0.0, 1.0)]  # dup vertex
        with self.assertRaises(ValueError):
            self.tk.point_in_polygon((0.5, 0.5), bad_poly)


# -------------------------------------------------------------------------
if __name__ == "__main__":  # pragma: no cover – executed only when run directly
    unittest.main()
