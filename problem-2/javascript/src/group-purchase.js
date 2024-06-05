const fs = require('fs');
const csvParser = require('csv-parser');
const fastCsv = require('fast-csv');

if (process.argv.length < 4) {
    console.log("usage: node group-purchase <input-orders.csv> <output-purchase.csv>");
    process.exit();
}

const inputFilePath = process.argv[2];
const outputFilePath = process.argv[3];

const purchases = {};
let ordersShipping = 0.0;
let ordersTotal = 0.0;
let ordersGrandTotal = 0.0;

fs.createReadStream(inputFilePath)
    .pipe(csvParser())
    .on('data', (row) => {
        const label = row['label'].trim();
        const amount = parseFloat(row['total']);
        if (label.startsWith('~')) {
            if (label === '~ total') {
                ordersTotal = amount;
            } else if (label === '~ shipping') {
                ordersShipping = amount;
            } else if (label === '~ grand total') {
                ordersGrandTotal = amount;
            }
        } else {
            const buyer = row['buyer'].trim();
            if (!purchases[buyer]) {
                purchases[buyer] = 0.0;
            }
            purchases[buyer] += amount;
            ordersTotal += amount;
        }
    })
    .on('end', () => {
        const outputStream = fs.createWriteStream(outputFilePath);
        const csvStream = fastCsv.format({ headers: ['buyer', 'amount', 'shipping', 'total'] });
        csvStream.pipe(outputStream);

        let totalAmount = 0.0;
        let totalShipping = 0.0;
        let grandTotal = 0.0;

        for (const [buyer, amount] of Object.entries(purchases)) {
            const shipping = parseFloat(((amount / ordersTotal) * ordersShipping).toFixed(2));
            const total = amount + shipping;
            csvStream.write({ buyer, amount, shipping, total });
            totalAmount += amount;
            totalShipping += shipping;
            grandTotal += total;
        }

        csvStream.write({ buyer: '~ total', amount: totalAmount.toFixed(2), shipping: totalShipping.toFixed(2), total: grandTotal.toFixed(2) });

        csvStream.end();
    });

