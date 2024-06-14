#define _GNU_SOURCE
#include <sched.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    cpu_set_t mask;
    CPU_ZERO(&mask);        // 初始化 CPU 集合
    CPU_SET(3, &mask);      // 将 CPU 编号为 3 的 CPU 加入集合

    // 设置当前进程的 CPU 亲和性
    if (sched_setaffinity(0, sizeof(mask), &mask) == -1) {
        perror("sched_setaffinity");
        return 1;
    }

    // 检查当前进程绑核状况
    if (sched_getaffinity(0, sizeof(mask), &mask) == -1) {
        perror("sched_getaffinity");
        return 1;
    }

    if (CPU_ISSET(3, &mask)) {
        printf("Current process is affined to CPU 3\n");
    } else {
        printf("Current process is NOT affined to CPU 3\n");
    }

    sleep(1233);
    return 0;
}


#include <sys/types.h>
#include <sched.h>
#include <stdio.h>

int sched_setaffinity(pid_t pid, size_t cpusetsize, const cpu_set_t *mask)
{
        // do nothing
        return 0;
}


test: main.c hook.so
        gcc -o test main.c

hook.so: hook.c
        gcc -fPIC -shared -o hook.so hook.c -ldl
