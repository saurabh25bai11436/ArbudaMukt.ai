# 🤝 Contributing to ArbudaMukt.ai

First off, thank you for considering contributing to ArbudaMukt! It is people like you who make this a universal solution for breast cancer care.

By contributing, you help us refine the bridge between screening, diagnosis, and mitigation.

---

## 📜 Code of Conduct
This project and everyone participating in it is governed by our Ethical AI Framework. By participating, you are expected to uphold these standards. Please report unacceptable behavior to `ethics@arbudamukt.ai`.

## 🏗️ Technical Standards

### 1. Code Quality
* **Linting:** We follow `PEP 8` for Python code. Please run `flake8` before submitting a Pull Request.
* **Type Hinting:** All new functions in the `models/` and `api/` directories must include Python type hints.
* **Documentation:** Every new feature requires an update to the relevant `.md` files in the `docs/` folder.

### 2. Clinical Rigor
* **Validation:** Any changes to model architecture must be accompanied by a validation report showing no drop in **Sensitivity** or **C-Index**.
* **Bias Check:** Ensure your contributions do not introduce demographic bias as outlined in our `BIAS_REPORT.md`.

---

## 🛠️ How to Contribute

### 1. Report Bugs
Use the GitHub "Issues" tab. Please include:
* A clear, descriptive title.
* Steps to reproduce the issue.
* Expected vs. actual behavior.

### 2. Suggest Enhancements
We are particularly interested in:
* New data augmentations for the `dicom_processor.py`.
* Improved survival analysis algorithms for the `prognostic_surv/` module.
* Enhancements to the Clinician/Patient UIs.

### 3. Pull Request Process
1. **Fork** the repo and create your branch from `main`.
2. If you've added code that should be tested, **add tests**.
3. Ensure the test suite passes using `pytest`.
4. Update the **`README.md`** or **`Directory Structure`** if you added new folders.
5. Submit the PR with a detailed description of the changes.

---

## 🧪 Testing Protocol
Before submitting a PR, ensure your local environment matches our production stack:

# Run full suite via Docker
docker-compose up --build
pytest tests/


## ⚖️ Clinical Disclaimer
Contributions involving medical logic or diagnostic weights must be reviewed by the Clinical Oversight Committee. We prioritize patient safety and "Human-in-the-Loop" decision-making above all else.

**Questions?** Reach out to the maintainers or open a "Discussion" thread on GitHub. Let's make the world ArbudaMukt!
