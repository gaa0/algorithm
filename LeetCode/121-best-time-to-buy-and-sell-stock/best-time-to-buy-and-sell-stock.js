/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let buy;
    let profit = 0;

    for (let i = 0; i < prices.length; i++) {
        price = prices[i];
        if (i == 0) {
            buy = price;
        } else {
            const thisProfit = price - buy;
            if (thisProfit > profit) profit = thisProfit;
            if (price < buy) buy = price;
        }
    }

    return profit;
};