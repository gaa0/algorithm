function solution(strings, n) {
    const myMap = new Map();
    for (const string of strings) {
        myMap.set(string[n], myMap.get(string[n]) ? [...myMap.get(string[n]), string].sort() : [string]);
    }
    
    const answer = [];
    
    for (const k of [...myMap.keys()].sort()) {
        answer.push(...myMap.get(k));
    }
    
    return answer;
}