import streamlit as st
import math


def calculate_desired_replicas(current_replicas, current_metric, desired_metric):
    """Calculate desired replicas based on HPA formula"""
    return math.ceil(current_replicas * (current_metric / desired_metric))


# Set page title and description
st.markdown("### K8s HPA 計算機")
st.markdown(
    """
這個計算機可幫助您了解 K8s HPA 如何根據當前指標計算所需 replicas (pod) 數量。

**[計算公式](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details):**
"""
)
st.latex(
    r"""
desiredReplicas = \text{ceil} \left( \text{currentReplicas} \times \left( \frac{\text{currentMetricValue}}{\text{desiredMetricValue}} \right) \right)
"""
)

# Input section
# st.markdown("### 輸入數值")

# First row for current_replicas
current_replicas = st.number_input("當前副本數 (currentReplicas)", min_value=1, value=1)

# Second row with two columns for metrics
metric_col1, metric_col2 = st.columns(2)

with metric_col1:
    current_metric = st.number_input(
        "當前指標值 (currentMetricValue)",
        # min_value=0.0,
        value=80,
        help="當前資源使用率（CPU % 或記憶體 %）",
    )

with metric_col2:
    desired_metric = st.number_input(
        "目標指標值 (desiredMetricValue)",
        # min_value=0.1,
        value=50,
        help="目標資源使用率（CPU % 或記憶體 %）",
    )

# Calculate and show results
if st.button("計算所需副本數 (desiredReplicas)"):
    desired_replicas = calculate_desired_replicas(
        current_replicas, current_metric, desired_metric
    )

    st.markdown(f"**所需副本數：** {desired_replicas}")

    # Show calculation steps
    st.markdown(
        f"""
       ```
       所需副本數
       = ceil[當前副本數 * (當前指標值 / 目標指標值)]
       = ceil[{current_replicas} * ({current_metric} / {desired_metric})]
       = ceil[{current_replicas} * {current_metric/desired_metric:.2f}]
       = ceil[{current_replicas * (current_metric/desired_metric):.2f}]
       = {desired_replicas}
       ```
    """
    )
