/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   run.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mathismottet <marvin@42.fr>                +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/11/04 10:52:19 by mathismottet      #+#    #+#             */
/*   Updated: 2023/11/06 18:34:07 by mathismottet     ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *run_script(void *arg) {
    char *script_name = (char *)arg;
    char command[256];

    printf("Start of API");
    snprintf(command, sizeof(command), "sh %s", script_name);
    int status = system(command);
    if (status != 0)
        fprintf(stderr, "Erreur lors de l'exécution de %s\n", script_name);
    pthread_exit(NULL);
}

void *run_python_script(void *arg) {
    char *script_name = (char *)arg;
    char command[256];

    printf("Sart Model run");
    snprintf(command, sizeof(command), "python3 %s", script_name);
    int status = system(command);
    if (status != 0)
        fprintf(stderr, "Erreur lors de l'exécution de %s\n", script_name);
    pthread_exit(NULL);
}

int main() {
    pthread_t thread1, thread2;
    char *script1 = "api_data/start_api.sh";
    char *script2 = "machin_learning/models.py";

    int rc1 = pthread_create(&thread1, NULL, run_script, (void *)script1);
    int rc2 = pthread_create(&thread2, NULL, run_python_script, (void *)script2);

    if (rc1 || rc2) {
        fprintf(stderr, "Erreur lors de la création des threads\n");
        exit(1);
    }

    // Attente de la fin des threads
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    printf("End of the programme.\n");

    return 0;
}
