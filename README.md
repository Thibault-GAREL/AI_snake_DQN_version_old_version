# 🐍 Snake AI with Deep Q-learning

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)
![PyTorch](https://img.shields.io/badge/Pytorch-2.7.1%2Bcu118-red.svg)
![Numpy](https://img.shields.io/badge/Numpy-2.2.6-red.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.6.1-red.svg)
![OpenPyxl](https://img.shields.io/badge/OpenPyxl-3.1.5-red.svg)  

![License](https://img.shields.io/badge/license-MIT-green.svg)  
![Contributions](https://img.shields.io/badge/contributions-welcome-orange.svg)  

## 📝 Project Description - Old Version
This project showcases an AI that learns to play [my snake game](https://github.com/Thibault-GAREL/snake_game) using the deep Q-learning algorithm. No hardcoded strategy — the agent improves by trial, error, and reward-based learning. 🧠📈

Attention ! 🚧 **This project is the old version** 🚧  
- 🎛️ **Hyperparameters** (learning rate, epsilon decay, reward shaping) have a **huge impact** on learning performance.  
- **Problem** 😵‍💫 : I can find good hyperparameter ! Maybe, it is something else 😥.

**Here is the new version that works :**
- [AI Snake - DQL - New Version](https://github.com/Thibault-GAREL/AI_snake_DQN_version)

---

## 🚀 Features
  🤖 Uses Deep Q-Learning with experience replay and epsilon-greedy exploration

  🧱 Neural network approximates Q-values for discrete actions (e.g., accelerate, turn left/right)

<!-- 
## Example Outputs
Here is an image of what it looks like :

![Image_snake](Images/Img.png)


### 📝 Notes & Observations
⏳ Training is unstable at first — the car often spins out or crashes quickly — but over time, it learns to stabilize, turn properly, and sometimes follow simple roads or avoid walls.

🎛️ **Hyperparameters** (learning rate, epsilon decay, reward shaping) have a **huge impact** on learning performance.

Here, we can see that over 100 steps, the best path have been found (in just more than 5 min).

It is more **hesitant** for the borrowed path but **adapts better** to different circuits than **Genetic algorithm** such as [AI_driving_genetic_version](https://github.com/Thibault-GAREL/AI_driving_genetic_version) !
-->
---

## ⚙️ How it works
🎮 The AI controls the snake in a Pygame environment with basic physics and obstacles.

🧠 It uses a Deep Q-Network to estimate the best action to take from any given state.

🧾 Inputs include the distance to the border, food, and tail in all 8 cardinal directions.

🎯 Rewards are given based on food eaten and are also negative when the snake hits a wall.
---

## 📂 Repository structure  
```bash
├── Images/                     # Images for the README
│
├── models1/                    
│   └── snake_dqn_model.pth     # Saved model checkpoint
├── models2/                    
├── models3/                    
│
├── compteur.py                 # Counter script
├── compteur_executions.txt     # Execution log for the counter
├── donnees1.xlsx               # Visualization the score for the training
├── donnees2.xlsx
│
├── exw.py                      # Excel writer script
├── ia.py                       # AI logic
├── main.py                     # Project entry point
├── snake.py                    # Snake game implementation
│
├── LICENSE                     # Project license
├── README.md                   # Main documentation
```

---

## 💻 Run it on Your PC  
Clone the repository and install dependencies:  
```bash
git clone https://github.com/Thibault-GAREL/AI_snake_DQN_version.git
cd AI_snake_DQN_version

python -m venv .venv #if you don't have a virtual environnement
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows

pip install neat-python numpy pygame openpyxl progressbar2

python main.py
```
---

## 📖 Inspiration / Sources  
I code it without any help 😆 !

Code created by me 😎, Thibault GAREL - [Github](https://github.com/Thibault-GAREL)




