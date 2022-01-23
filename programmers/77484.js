function solution(lottos, win_nums) {
    var answer = [0, 7];
    let zero_cnt = 0;
    
    const win_nums_set = new Set(win_nums);
    
    for (let item of lottos) {
        if (item == 0) {
            zero_cnt++;
        } else {
            if (win_nums_set.has(item)) {
                answer[1]--;
            }
        }
    }
    
    answer[0] = answer[1] - zero_cnt;
    if (answer[1] == 7) answer[1] = 6;
    if (answer[0] == 7) answer[0] = 6;
    
    return answer;
}