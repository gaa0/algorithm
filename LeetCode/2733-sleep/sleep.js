/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    function a(millis) {
        return new Promise(resolve => setTimeout(() => resolve({}), millis));
    }
    return await a(millis);
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */