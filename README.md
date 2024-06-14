#define _GNU_SOURCE
#include <sched.h>
#include <unistd.h>
#include <stdio.h>
 
int main() {
    cpu_set_t mask;
    CPU_ZERO(&mask);        // 初始化 CPU 集合
    CPU_SET(2, &mask);      // 将 CPU 编号为 2 的 CPU 加入集合
 
    // 设置当前进程的 CPU 亲和性
    if (sched_setaffinity(0, sizeof(mask), &mask) == -1) {
        perror("sched_setaffinity");
        return 1;
    }
 
    printf("Current process is now affined to CPU 2\n");
    sleep(1233);
    return 0;
}
