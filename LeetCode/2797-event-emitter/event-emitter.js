class EventEmitter {
    events = new Map();
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        let i;
        const arr = this.events.get(eventName)
        if (arr) {
            i = arr.length;
            arr.push(callback);
        } else {
            i = 0;
            this.events.set(eventName, [callback]);
        }

        return {
            unsubscribe: () => {
                this.events.get(eventName)[i] = null;
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        if (!this.events.has(eventName)) return [];
        const r = [];
        for (const event of this.events.get(eventName)) {
            if (event === null) continue;
            r.push(event(...args));
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