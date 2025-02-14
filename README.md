# PDPInsight

Partial Dependence Plots (PDPs) are useful for interpreting machine learning models by showing how a feature affects predictions. Here's an AWS-based architecture to generate PDPs:

## **Solution Overview**

We'll use AWS services to train a machine learning model, analyze feature dependencies, and generate PDPs.

## **Architecture**

1. **Amazon S3** - Store dataset and generated plots.
2. **Amazon SageMaker** - Train the model and generate PDPs using Jupyter notebooks or processing jobs.
3. **AWS Lambda** (Optional) - Trigger PDP computation.
4. **Amazon EventBridge** (Optional) - Automate retraining and PDP updates.

## **Steps to Implement**

### **1. Store Dataset in S3**

- Upload your dataset (CSV, Parquet, etc.) to an S3 bucket.

### **2. Train a Model in SageMaker**

- Use SageMaker's built-in algorithms or a custom model in a Jupyter notebook.
- Train with Amazon SageMaker Training Jobs or Autopilot.

### **3. Compute Partial Dependence Plots**

- Use Python libraries like **SHAP** or **Scikit-learn**:

  ```python
  from sklearn.inspection import partial_dependence, plot_partial_dependence
  plot_partial_dependence(model, X_train, features=[0, 1])
  ```

- If using SHAP:

  ```python
  import shap
  explainer = shap.TreeExplainer(model)
  shap_values = explainer.shap_values(X_train)
  shap.dependence_plot(0, shap_values, X_train)
  ```

- Store PDP images in S3.

### **4. Automate PDP Generation** (Optional)

- Use **AWS Lambda** to trigger PDP computation when a new model is trained.
- Use **EventBridge** to run periodic updates.

## **Enhancements**

- Deploy an **API (AWS Lambda + API Gateway)** to dynamically generate PDPs.
- Use **AWS Glue** for data preprocessing.
- Store insights in **Amazon DynamoDB** for tracking model performance.

## pip install using virtual environment

```bash
source .venv/bin/activate && pip install numpy
```
