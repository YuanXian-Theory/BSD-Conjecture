import "T64_Topology"

/-- Elliptic Curve Lift to T64 -/
def T64.lift (E : EllipticCurve) : T64Cycle := by
  -- Explicit construction via Weierstrass model embedding into T64
  exact lift_weierstrass E

theorem lift_preserves_rank (E : EllipticCurve) :
  rank (E.at ℚ) = topologicalCharge (T64.lift E) := by
  apply topological_charge_projection
  exact TCSC_closed E
