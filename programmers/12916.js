function solution(s){
    let p = 0, y = 0;
    for (const i of s.toLowerCase()) {
        if (i === "p") p++;
        else if (i === "y") y++;
    }
    return p === y;
}