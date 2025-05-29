"""geometry_toolkit.py
A lightweight 2-D computational-geometry helper for educational or utility use-cases.

Classes
-------
GeometryToolkit
    Collects static-like helpers for distance calculation, triangle area
    evaluation, and point-in-polygon tests.

The implementation is dependency-free and targets Python≥3.11.
"""
from __future__ import annotations

import math
from typing import Iterable, List, Tuple

Point = Tuple[float, float]


class GeometryToolkit:
    """A tiny toolkit of 2-D geometry helpers.

    Methods
    -------
    distance(p1, p2)
        Euclidean distance between two points.

    triangle_area(p1, p2, p3)
        Absolute area of the triangle formed by three points; raises
        ``ValueError`` if the points are colinear.

    point_in_polygon(pt, poly)
        Ray-casting test for *simple* polygons (non-self-intersecting);
        boundary points are considered **inside**.
    """

    # ---------------------------------------------------------------------
    # Public API
    # ---------------------------------------------------------------------

    def distance(self, p1: Point, p2: Point) -> float:
        """Return the Euclidean distance between *p1* and *p2*.

        Parameters
        ----------
        p1, p2 : tuple[float, float]
            2-D points.

        Returns
        -------
        float
            ``sqrt((x2 - x1)**2 + (y2 - y1)**2)``.

        Raises
        ------
        TypeError
            If *p1* or *p2* is not a 2-tuple of int/float.
        """
        self._validate_point(p1)
        self._validate_point(p2)
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        return math.hypot(dx, dy)

    # ------------------------------------------------------------------
    def triangle_area(self, p1: Point, p2: Point, p3: Point) -> float:
        """Return the absolute area of the triangle defined by *p1*, *p2*, *p3*.

        Uses the shoelace formula (½|x₁(y₂ - y₃) + x₂(y₃ - y₁) + x₃(y₁ - y₂)|).

        Raises
        ------
        ValueError
            If the three points are colinear (area ≈ 0).
        TypeError
            If any argument is not a valid point.
        """
        self._validate_point(p1)
        self._validate_point(p2)
        self._validate_point(p3)

        area_times_two = (
            p1[0] * (p2[1] - p3[1])
            + p2[0] * (p3[1] - p1[1])
            + p3[0] * (p1[1] - p2[1])
        )
        area = abs(area_times_two) * 0.5
        if math.isclose(area, 0.0, abs_tol=1e-12):
            raise ValueError("Triangle area is zero - points are colinear.")
        return area

    # ------------------------------------------------------------------
    def point_in_polygon(self, pt: Point, poly: List[Point]) -> bool:
        """Return *True* if *pt* lies inside or *on* the boundary of *poly*.

        Implements the *even-odd* (ray-casting) rule.  A horizontal ray is cast
        from *pt* towards positive x; the parity of intersections decides the
        result.  Boundary points (on edges or vertices) are treated as inside.

        Parameters
        ----------
        pt : tuple[float, float]
            The test point.
        poly : list[tuple[float, float]]
            Vertices of a *simple* (non-self-intersecting) polygon, ordered
            clockwise or counter-clockwise.  The list **must not** repeat the
            first vertex at the end.

        Returns
        -------
        bool
            ``True`` if the point is inside or on the boundary.

        Raises
        ------
        ValueError
            For malformed polygons (fewer than three vertices or duplicate
            consecutive vertices).
        TypeError
            If *pt* or any vertex is not a valid point.
        """
        self._validate_point(pt)
        self._validate_polygon(poly)

        px, py = pt
        inside = False
        n = len(poly)

        for i in range(n):
            a = poly[i]
            b = poly[(i + 1) % n]

            # Boundary check first.
            if self._point_on_segment(pt, a, b):
                return True

            ax, ay = a
            bx, by = b

            intersects = ((ay > py) != (by > py)) and (
                px < (bx - ax) * (py - ay) / (by - ay) + ax
            )
            if intersects:
                inside = not inside

        return inside

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _validate_point(pt: tuple[float, float]) -> None:
        """Ensure *pt* is a 2-tuple of int/float; raise *TypeError* otherwise."""
        if not (
            isinstance(pt, tuple)
            and len(pt) == 2
            and all(isinstance(c, (int, float)) for c in pt)
        ):
            raise TypeError(
                "Point must be a tuple[float, float]; got: {!r}".format(pt)
            )

    # ------------------------------------------------------------------
    @classmethod
    def _validate_polygon(cls, poly: Iterable[Point]) -> None:
        """Basic sanity checks for a polygon argument."""
        if not isinstance(poly, list):
            raise TypeError("Polygon must be a list of points.")
        if len(poly) < 3:
            raise ValueError("Polygon must contain at least three vertices.")
        for pt in poly:
            cls._validate_point(pt)
        # Disallow consecutive duplicate vertices.
        for i in range(len(poly)):
            if poly[i] == poly[(i + 1) % len(poly)]:
                raise ValueError("Polygon has duplicate consecutive vertices.")

    # ------------------------------------------------------------------
    @staticmethod
    def _point_on_segment(p: Point, a: Point, b: Point) -> bool:
        """Return *True* if point *p* lies on segment AB (inclusive)."""
        (px, py), (ax, ay), (bx, by) = p, a, b
        # Check colinearity via cross‑product ≈ 0.
        cross = (bx - ax) * (py - ay) - (by - ay) * (px - ax)
        if not math.isclose(cross, 0.0, abs_tol=1e-12):
            return False
        # Check bounding‑box.
        min_x, max_x = sorted((ax, bx))
        min_y, max_y = sorted((ay, by))
        return (min_x - 1e-12) <= px <= (max_x + 1e-12) and (
            (min_y - 1e-12) <= py <= (max_y + 1e-12)
        )


# -------------------------------------------------------------------------
# Minimal usage examples
# -------------------------------------------------------------------------
if __name__ == "__main__":
    tk = GeometryToolkit()

    # 1. Distance
    print("Distance:", tk.distance((0, 0), (3, 4)))  # 5.0

    # 2. Triangle area
    print("Triangle area:", tk.triangle_area((0, 0), (4, 0), (0, 3)))  # 6.0

    # 3. Point‑in‑polygon
    square = [(0, 0), (5, 0), (5, 5), (0, 5)]
    print("Inside square:", tk.point_in_polygon((3, 3), square))  # True
