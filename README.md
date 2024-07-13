kperf采集命令（perfstudio分析）：/root/kperf --rawdata --hotfunc --topdown --cache --tlb --imix --uncore --spe --duration 1 --interval 15 --pid 32777 > kperf.out 
                                ./kperf --rawdata --hotfunc --topdown --cache --tlb --imix --uncore --spe --duration 1 --interval 15 --pid PID --excel kperf
命令行topdown分析：/root/kperf --topdown --cache --pid <pid> --duration 1 --interval 5
