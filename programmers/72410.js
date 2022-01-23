function solution(new_id) {
    new_id = new_id.toLowerCase();
    
    var pattern1 = /[0-9]/;
    var pattern2 = /[a-z]/;
    var pattern3 = /[-_.]/;
    var tmp_id = ''
    for (let item of new_id) {
        if (pattern1.test(item) || pattern2.test(item) || pattern3.test(item)) tmp_id += item;
    }
    
    new_id = tmp_id;
    tmp_id = '';
    
    for (let item of new_id) {
        if (item == '.') {
            if (tmp_id && tmp_id[tmp_id.length - 1] != '.') tmp_id += item;
        } else {
            tmp_id += item;
        }
    }
    if (tmp_id[tmp_id.length - 1] == '.') tmp_id = tmp_id.slice(0, -1);
    
    if (tmp_id == '') tmp_id = 'a';
    
    if (tmp_id.length >= 16) {
        tmp_id = tmp_id.slice(0, 15);
    }
    if (tmp_id[tmp_id.length - 1] == '.') tmp_id = tmp_id.slice(0, -1);
    
    if (tmp_id.length <= 2) {
        const N = tmp_id.length;
        for (var i = 0; i < 3 - N; i++) {
            tmp_id += tmp_id[tmp_id.length - 1];
        }
    };
    
    return tmp_id;
}