"""
Execute notebook cell by cell and collect all errors.
Uses nbclient with raise_on_ename=False to continue past errors.
"""
import json
import sys
import nbformat
import nbclient
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

# Load notebook
nb_path = "c:/Users/ETU/Documents/projet-chlordecone-martinique/notebooks/projet_chlordecone.ipynb"
with open(nb_path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

print(f"Notebook loaded. Number of cells: {len(nb.cells)}")
sys.stdout.flush()

errors = []

# Create client with raise_on_error=False
client = NotebookClient(
    nb,
    timeout=120,
    kernel_name="python3",
    resources={"metadata": {"path": "c:/Users/ETU/Documents/projet-chlordecone-martinique/"}},
    raise_on_ename=None,  # don't raise
)

# We'll execute manually cell by cell
import nest_asyncio
nest_asyncio.apply()

import asyncio

async def execute_cells():
    async with client.async_setup_kernel():
        for idx, cell in enumerate(nb.cells):
            if cell.cell_type != "code":
                continue
            src_lines = cell.source.splitlines()
            first_2_lines = "\n".join(src_lines[:2]) if src_lines else ""
            cell_id = cell.get("id", f"cell_{idx}")

            print(f"\n--- Executing cell {idx} (id={cell_id}) ---")
            print(f"  First lines: {first_2_lines[:120]}")
            sys.stdout.flush()

            try:
                await client.async_execute_cell(cell, idx)
                # Check outputs for errors
                for output in cell.get("outputs", []):
                    if output.get("output_type") == "error":
                        ename = output.get("ename", "")
                        evalue = output.get("evalue", "")
                        traceback = output.get("traceback", [])
                        # Strip ANSI codes from traceback for readability
                        import re
                        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
                        clean_tb = [ansi_escape.sub('', line) for line in traceback[-5:]]
                        errors.append({
                            "cell_index": idx,
                            "cell_id": cell_id,
                            "ename": ename,
                            "evalue": evalue,
                            "traceback_tail": clean_tb,
                            "first_2_lines": first_2_lines[:200],
                        })
                        print(f"  ERROR in cell {idx}: {ename}: {evalue}")
            except CellExecutionError as e:
                import re
                ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
                tb_str = ansi_escape.sub('', str(e))[:500]
                errors.append({
                    "cell_index": idx,
                    "cell_id": cell_id,
                    "ename": type(e).__name__,
                    "evalue": str(e)[:300],
                    "traceback_tail": [tb_str],
                    "first_2_lines": first_2_lines[:200],
                })
                print(f"  CellExecutionError in cell {idx}: {e!s:.200}")
            except Exception as e:
                errors.append({
                    "cell_index": idx,
                    "cell_id": cell_id,
                    "ename": type(e).__name__,
                    "evalue": str(e)[:300],
                    "traceback_tail": [],
                    "first_2_lines": first_2_lines[:200],
                })
                print(f"  Exception in cell {idx}: {type(e).__name__}: {e!s:.200}")

asyncio.run(execute_cells())

# Save results
out_path = "c:/Users/ETU/Documents/projet-chlordecone-martinique/notebook_errors.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(errors, f, ensure_ascii=False, indent=2)

print(f"\n\n=== SUMMARY: {len(errors)} errors found ===")
for err in errors:
    print(f"\nCell #{err['cell_index']} (id={err['cell_id']})")
    print(f"  Error: {err['ename']}: {err['evalue'][:150]}")
    print(f"  Code:  {err['first_2_lines'][:150]}")
    if err['traceback_tail']:
        print(f"  Traceback tail:")
        for line in err['traceback_tail']:
            print(f"    {line[:200]}")
print(f"\nErrors saved to: {out_path}")
