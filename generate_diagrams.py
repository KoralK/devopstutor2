import os

# Define the DOT content for each diagram
ci_pipeline_dot = """
digraph G {
    rankdir=LR; // Left-to-right layout
    node [shape=box, style=rounded, fillcolor="#dae8fc", color="#6c8ebf"];

    CodeCheckin [label="Code Check-in\\n(Cloud Source Repositories)"];
    AutomatedTesting [label="Automated Testing\\n(Unit Tests, Linting)"];
    Build [label="Build\\n(Cloud Build)"];
    ArtifactStorage [label="Artifact Storage\\n(Artifact Registry)"];

    CodeCheckin -> AutomatedTesting [label="Trigger", color="#333", fontcolor="#333"];
    AutomatedTesting -> Build [label="Tests Pass", color="#333", fontcolor="#333"];
    Build -> ArtifactStorage [label="Store Artifact", color="#333", fontcolor="#333"];
}
"""

terraform_workflow_dot = """
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded, fillcolor="#dae8fc", color="#6c8ebf"];

    CodeRepo [label="Code Repository\\n(Cloud Source Repositories)"];
    Terraform [label="Terraform Configuration"];
    CloudResources [label="Google Cloud Resources\\n(Compute, Storage, Networking)"];

    CodeRepo -> Terraform [label="Terraform Plan/Apply", color="#333", fontcolor="#333"];
    Terraform -> CloudResources [label="Provision Resources", color="#333", fontcolor="#333"];
}
"""

devops_pipeline_dot = """
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded, fillcolor="#dae8fc", color="#6c8ebf"];

    CodeRepo [label="Code Repository\\n(Cloud Source Repositories)"];
    CloudBuild [label="Cloud Build"];
    ArtifactRegistry [label="Artifact Registry"];
    Deployment [label="Deployment\\n(GKE, Cloud Run, etc.)"];

    CodeRepo -> CloudBuild [label="Trigger", color="#333", fontcolor="#333"];
    CloudBuild -> ArtifactRegistry [label="Store Artifact", color="#333", fontcolor="#333"];
    ArtifactRegistry -> Deployment [label="Deploy", color="#333", fontcolor="#333"];
}
"""

binary_authorization_dot = """
digraph G {
    rankdir=LR;
    node [shape=box, style=rounded, fillcolor="#dae8fc", color="#6c8ebf"];

    CloudBuild [label="Cloud Build"];
    ArtifactRegistry [label="Artifact Registry"];
    VulnerabilityScan [label="Vulnerability Scan"];
    BinaryAuth [label="Binary Authorization"];
    GKE [label="Google Kubernetes Engine (GKE)"];

    CloudBuild -> ArtifactRegistry [label="Push Image", color="#333", fontcolor="#333"];
    ArtifactRegistry -> VulnerabilityScan [label="Scan Image", color="#333", fontcolor="#333"];
    VulnerabilityScan -> BinaryAuth [label="Verify", color="#333", fontcolor="#333"];
    BinaryAuth -> GKE [label="Deploy", color="#333", fontcolor="#333"];
}
"""

# Save the DOT content to files
def save_dot_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
    print(f"DOT file saved: {filename}")

# Generate SVG files from DOT files using Graphviz
def generate_svg(dot_filename, svg_filename):
    try:
        os.system(f"dot -Tsvg {dot_filename} -o {svg_filename}")
        print(f"SVG file generated: {svg_filename}")
    except Exception as e:
        print(f"Error generating SVG: {e}")

# Generate the DOT and SVG files
dot_files = {
    "ci-pipeline.dot": ci_pipeline_dot,
    "terraform-workflow.dot": terraform_workflow_dot,
    "devops-pipeline.dot": devops_pipeline_dot,
    "binary-authorization.dot": binary_authorization_dot,
}

for dot_filename, content in dot_files.items():
    # Save the DOT file
    save_dot_file(dot_filename, content)

    # Generate the corresponding SVG file
    svg_filename = dot_filename.replace(".dot", ".svg")
    generate_svg(dot_filename, svg_filename)

print("All DOT and SVG files generated successfully!")