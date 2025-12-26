import progressbar
import time

import snake
import exw
import compteur

# Au début de ton programme
executions = compteur.compter_executions()
print(f"Exécution n°{executions}")


agent = snake.ia.DQNAgent(snake.ia.input_dim, snake.action_dim)
score_mean = []
score_temp = 0

modulo = (snake.ia.nb_loop_train-1) // 100  # Pour le logging graphique
save_interval = 100  # Sauvegarder tous les 100 épisodes

fichier, wb, ws = exw.create("donnees3", "entrainement" + str(executions), "X", "Y")

model_name = "models4" # "models" + str(executions)

if snake.ia.os.path.exists(model_name + "/snake_dqn_model.pth"):
    agent.load_model(model_name + "/snake_dqn_model.pth")
    print("Model loaded : " + model_name + "/snake_dqn_model.pth")
else:
    snake.ia.os.makedirs(model_name, exist_ok=True)
    print("Model created")


try:
    for episode in progressbar.progressbar(range(snake.ia.nb_loop_train)):
        # state = [250, 353.5533905932738, 500, 424.26406871192853, 300, 353.5533905932738, 250, 353.5533905932738, 0, 0, 200, 0, 0, 0, 0, 0]

        score_temp += snake.game_loop(snake.rect_width, snake.rect_height, snake.display, agent)
        # print(f'longeur du buffer : {len(agent.replay_buffer.buffer)}')
        agent.train_step(batch_size=64)


        # while not done:
        #     action = agent.select_action(state, snake.action_dim)
        #     next_state, reward, done, _ = env.step(action)
        #
        #     # Stocke l'expérience
        #     agent.replay_buffer.push(state, action, reward, next_state, done)
        #
        #     # Entraîne le réseau
        #     agent.train_step(batch_size=64)
        #
        #     state = next_state

        # Mise à jour du réseau cible toutes les 10 itérations (au lieu de tous les modulo)
        if episode % 10 == 0 and episode != 0:
            agent.update_target()

        # Sauvegarde du modèle tous les save_interval épisodes
        if episode % save_interval == 0 and episode != 0:
            agent.save_model(model_name + '/snake_dqn_model.pth')
            print(f"\n💾 Modèle sauvegardé à l'épisode {episode}")

        # Logging graphique tous les modulo épisodes
        if episode % modulo == 0 and episode != 0:
            score_mean.append(score_temp/modulo)
            exw.ajouter_donnee(fichier, wb, ws, episode, score_temp/modulo, "Graphe de l'évolution des scores", "Episode", "Score")
            score_temp = 0

except KeyboardInterrupt:
    print("\n\n⚠️  Entraînement interrompu par l'utilisateur (Ctrl+C)")
    print("💾 Sauvegarde du modèle en cours...")
    agent.save_model(model_name + '/snake_dqn_model.pth')
    print("✅ Modèle sauvegardé avec succès!")

# Sauvegarde finale
print("\n💾 Sauvegarde finale du modèle...")
agent.save_model(model_name + '/snake_dqn_model.pth')
print("✅ Entraînement terminé!")

# print (score_mean)