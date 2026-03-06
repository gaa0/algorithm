class EventEmitter {
    events = new Map();
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        let arr = this.events.get(eventName)
        if (!arr) {
            arr = []
            this.events.set(eventName, arr);
        }

        const i = arr.length;
        arr.push(callback);

        return {
            unsubscribe: () => {
                arr[i] = null;
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const arr = this.events.get(eventName);
        if (!arr) return [];
        const r = [];
        for (const event of arr) {
            if (event) r.push(event(...args));
        }
        return r;
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */