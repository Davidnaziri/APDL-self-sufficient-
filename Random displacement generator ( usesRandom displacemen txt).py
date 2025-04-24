import os
import random

# Absolute path to the APDL template
template_path = "E:/Master thesis 2 (Automation)/Python/Random displacement.txt"

# Load APDL template content
with open(template_path, "r") as f:
    template = f.read()

# Markers to identify the displacement block and results filename
disp_start_marker = "! Apply displacement boundary condition (randomized, 16-digit precision)"
disp_end_marker = "FINISH"
cfopen_marker = "*CFOPEN, stress_results_00, txt"

# Output directory for generated scripts
output_dir = "E:/Master thesis 2 (Automation)/Python/generated_apdl_scripts"
os.makedirs(output_dir, exist_ok=True)

# Generate files from 1001 to 2001
for file_num in range(1001, 2002):
    # Generate 16-digit precision displacements for nodes 35–110
    disp_lines = [f"D, {node}, UX, {random.uniform(0.0, 0.0001):.16f}" for node in range(35, 111)]
    displacement_block = disp_start_marker + "\n" + "\n".join(disp_lines) + "\n" + disp_end_marker

    # Replace the displacement block in the template
    start_idx = template.find(disp_start_marker)
    end_idx = template.find(disp_end_marker, start_idx) + len(disp_end_marker)
    script_body = template[:start_idx] + displacement_block + template[end_idx:]

    # Update the result file name
    script_body = script_body.replace(cfopen_marker, f"*CFOPEN, stress_results_{file_num}, txt")

    # Write the new APDL script
    output_path = os.path.join(output_dir, f"{file_num}.txt")
    with open(output_path, "w") as out_file:
        out_file.write(script_body)

print(f"Generated 1001 APDL scripts in: {output_dir}")
