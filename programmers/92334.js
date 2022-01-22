function solution(id_list, report, k) {
    const createZeroArray = function(len) {
        return new Array(len).fill(0);
    };
    
    var report_cnt = createZeroArray(id_list.length);
    var answer = createZeroArray(id_list.length);
    
    const report_set = new Set(report);
    
    for (let item of report_set) {
        const item_list = item.split(' ');
        report_cnt[id_list.indexOf(item_list[1])]++;
    };
    
    var stop_set = new Set();
    
    for (let i = 0; i < id_list.length; i++) {
        if (report_cnt[i] >= k) {
            stop_set.add(id_list[i]);
        };
    };
    
    for (let item of report_set) {
        const item_list = item.split(' ');
        if (stop_set.has(item_list[1])) {
            answer[id_list.indexOf(item_list[0])]++;
        };
    };
    
    return answer;
}