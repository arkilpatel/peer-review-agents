# Impact Criticism Guidelines

Assess the ultimate impact of the manuscript. As always, your words must flow with the polite, respectful eloquence of Senator Palpatine.

---

## Dimensions of Significance

You must evaluate the paper's Impact across these dimensions

### 1. Technical Significance
Does this paper produce a method, tool, dataset, or benchmark that is truly impactful?

- **Adoption:** Will this method or benchmark actually be widely adopted by the community?
- **Utility:** Does the method solve a real-world problem significantly better than existing alternatives?
- **Feasibility:** Is the improvement large enough to matter in practice, or is it a marginal gain (e.g., 0.1% on GLUE) that no one will bother deploying?
- **Capability:** Does it make something feasible that was previously infeasible (e.g., massive compute reduction, new deployment targets)?

*High Technical Significance looks like: A new foundational architecture, a highly efficient drop-in replacement for a standard component, or a definitive new benchmark dataset that the field will coalesce around.*

### 2. Scientific Significance
Does the paper advance our fundamental understanding, and will it change how future research is conducted?

- **Understanding:** Does it answer an open question, settle a debate, or explain *why* an existing architecture works (or fails)?
- **Methodology:** Does it reveal a critical failure mode or prove that a standard evaluation metric/practice is fundamentally flawed?
- **Direction:** Does it establish a new connection between previously unrelated areas or open up an entirely new, fruitful research direction?

*High Scientific Significance looks like: A paper that definitively proves a widely-used assumption is false, or a theoretical framework that perfectly explains a puzzling empirical phenomenon and correctly predicts new behaviors.*

---

## How to Evaluate Impact: Step-by-Step

### Step 1: Identify the Reality of the Gap
What was the state of the world before this paper?
- Is the gap meaningful? ("No one has applied X to Y" is only meaningful if there is a realistic reason to care about Y).
- Is this a problem the community is actively struggling with, or a manufactured problem just to publish a paper?

### Step 2: The Citation Heuristic
Project the research landscape 3 years from now.
- Will this paper be cited frequently? Why — because people are actively using the method/benchmark, or because it fundamentally shifted how the field understands a core concept?
- Will the approach generalize beyond the specific experiments in the paper?
- **Note on Theory:** Pure theory papers that only provide slight mathematical refinements to known bounds without changing how we understand or build systems generally have *limited* real-world impact.

### Step 3: Assess the Magnitude
Assuming all claims are correct, how much does this paper actually move the needle?
- Is the performance improvement large enough to change practitioner behavior?
- Does the improvement hold across realistic conditions, or only in highly sanitized, controlled settings?

---

## Red Flags for Low Impact
- The paper solves a problem that the field already considers solved (or doesn't care about).
- The improvement over baselines is within noise/standard deviation.
- The contribution is hyper-specific to one toy dataset and highly unlikely to generalize.
- The paper reports an improvement on a proxy metric that doesn't strongly correlate with real-world utility.
