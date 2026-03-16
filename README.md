# Iris-Flower-Classification
# 🌸 Iris Flower Classification

A beginner-friendly Machine Learning project that classifies iris flowers into three species using the K-Nearest Neighbors (KNN) algorithm.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?style=flat-square&logo=scikit-learn)
![Status](https://img.shields.io/badge/Status-Complete-green?style=flat-square)

---

## 📌 Project Overview

This project uses the classic **Iris dataset** to build a classification model that predicts the species of an iris flower based on its physical measurements. It covers the full ML workflow from data exploration to making predictions.

### 🌼 Flower Species
| Species | Description |
|---|---|
| Setosa | Small petals, easily distinguishable |
| Versicolor | Medium-sized, overlaps with Virginica |
| Virginica | Largest petals and sepals |

---

## 📊 Features Used

| Feature | Description |
|---|---|
| Sepal Length | Length of the sepal (cm) |
| Sepal Width | Width of the sepal (cm) |
| Petal Length | Length of the petal (cm) |
| Petal Width | Width of the petal (cm) |

---

## 🛠️ Tech Stack

- **Python 3.11**
- **scikit-learn** — ML model and dataset
- **Pandas** — data manipulation
- **NumPy** — numerical operations
- **Matplotlib & Seaborn** — data visualization

---

---

## 📁 Project Structure

```
iris-classification/
│
├── iris.py               # Main ML script
├── iris.ipynb            # Jupyter Notebook version
├── README.md             # Project documentation
└── ml_env/               # Virtual environment (not committed)
```

---

## 🔄 ML Workflow

```
Load Data → Explore & Visualize → Split Data → Train Model → Evaluate → Predict
```

1. **Load Data** — Load the built-in Iris dataset from scikit-learn
2. **Explore** — Visualize species distributions using pairplots
3. **Split** — 80% training / 20% testing
4. **Train** — K-Nearest Neighbors classifier (k=3)
5. **Evaluate** — Measure accuracy and classification report
6. **Predict** — Classify new flower measurements

---

## 📈 Results

The KNN model achieves approximately **95–100% accuracy** on the test set.

```
Accuracy: 0.97

              precision    recall  f1-score
    setosa       1.00      1.00      1.00
versicolor       0.94      1.00      0.97
 virginica       1.00      0.94      0.97
```

---

## 🌱 What I Learned

- The core ML workflow: load → explore → split → train → evaluate → predict
- How K-Nearest Neighbors classification works
- Data visualization with Seaborn pairplots
- Setting up Python virtual environments for ML projects
- Evaluating models with accuracy scores and classification reports

---

## 🔮 Future Improvements

- [ ] Try other algorithms (Decision Tree, Random Forest, SVM)
- [ ] Add a confusion matrix visualization
- [ ] Build a simple UI to input flower measurements
- [ ] Deploy the model as a web app using Flask or Streamlit

---

## 📚 Resources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Iris Dataset Info](https://archive.ics.uci.edu/ml/datasets/iris)
- [KNN Algorithm Explained](https://scikit-learn.org/stable/modules/neighbors.html)

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)

---

*This project was built as part of my Machine Learning learning journey. 🚀*
