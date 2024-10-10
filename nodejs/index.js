const yahooFinance = require("yahoo-finance2").default;

function formatDateToCST(isoTime) {
  // 将 ISO 8601 时间转换为 Date 对象
  const date = new Date(isoTime);

  // 使用 toLocaleString() 方法将时间转换为中国标准时间
  const options = {
    timeZone: "Asia/Shanghai",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  };
  return date.toLocaleString("zh-CN", options);
}

async function getStockData(tickerSymbol) {
  try {
    const result = await yahooFinance.quoteSummary(tickerSymbol, {
      modules: ["price"],
    });
    if (result.price) {
      const latestData = result.price;
      const translatedData = {
        开盘价: parseFloat(latestData.regularMarketOpen.toFixed(2)),
        最高价: parseFloat(latestData.regularMarketDayHigh.toFixed(2)),
        最低价: parseFloat(latestData.regularMarketDayLow.toFixed(2)),
        收盘价: parseFloat(latestData.regularMarketPreviousClose.toFixed(2)),
        成交量: latestData.regularMarketVolume,
      };

      // 使用 formatDateToCST 函数将 UTC 时间转换为中国标准时间
      const latestDate = formatDateToCST(latestData.regularMarketTime);
      return { latestDate, translatedData };
    } else {
      console.log(`未能获取 ${tickerSymbol} 的最新数据。`);
      return null;
    }
  } catch (error) {
    console.error(`获取 ${tickerSymbol} 数据时发生错误: ${error}`);
    return null;
  }
}

async function getCryptoData(tickerSymbol) {
  try {
    const result = await yahooFinance.quoteSummary(tickerSymbol, {
      modules: ["price"],
    });
    if (result.price) {
      const latestData = result.price;
      const latestPrice = parseFloat(latestData.regularMarketPrice.toFixed(2));

      // 使用 formatDateToCST 函数将 UTC 时间转换为中国标准时间
      const latestDate = formatDateToCST(latestData.regularMarketTime);
      return { latestDate, latestPrice };
    } else {
      console.log(`未能获取 ${tickerSymbol} 的最新价格。`);
      return null;
    }
  } catch (error) {
    console.error(`获取 ${tickerSymbol} 数据时发生错误: ${error}`);
    return null;
  }
}

async function getSSEData(tickerSymbol) {
  return getStockData(tickerSymbol);
}

async function main() {
  // 获取 SP500 指数数据，使用 SPY ETF
  const sp500Data = await getStockData("SPY");
  if (sp500Data) {
    const { latestDate, translatedData } = sp500Data;
    console.log(`SP500 (SPY) 最新数据 (${latestDate}):`);
    console.log(`  开盘价: ${translatedData["开盘价"]}`);
    console.log(`  最高价: ${translatedData["最高价"]}`);
    console.log(`  最低价: ${translatedData["最低价"]}`);
    console.log(`  收盘价: ${translatedData["收盘价"]}`);
    console.log(`  成交量: ${translatedData["成交量"]}\n`);
  }

  // 获取纳斯达克指数数据，使用 QQQ ETF
  const nasdaqData = await getStockData("QQQ");
  if (nasdaqData) {
    const { latestDate, translatedData } = nasdaqData;
    console.log(`纳斯达克 (QQQ) 最新数据 (${latestDate}):`);
    console.log(`  开盘价: ${translatedData["开盘价"]}`);
    console.log(`  最高价: ${translatedData["最高价"]}`);
    console.log(`  最低价: ${translatedData["最低价"]}`);
    console.log(`  收盘价: ${translatedData["收盘价"]}`);
    console.log(`  成交量: ${translatedData["成交量"]}\n`);
  }

  // 获取比特币价格
  const btcData = await getCryptoData("BTC-USD");
  if (btcData) {
    const { latestDate, latestPrice } = btcData;
    console.log(`比特币价格 (USD) 最新数据 (${latestDate}): ${latestPrice}\n`);
  }

  // 获取上证指数数据
  const sseData = await getSSEData("000001.SS");
  if (sseData) {
    const { latestDate, translatedData } = sseData;
    console.log(`上证指数 最新数据 (${latestDate}):`);
    console.log(`  开盘价: ${translatedData["开盘价"]}`);
    console.log(`  最高价: ${translatedData["最高价"]}`);
    console.log(`  最低价: ${translatedData["最低价"]}`);
    console.log(`  收盘价: ${translatedData["收盘价"]}`);
    console.log(`  成交量: ${translatedData["成交量"]}\n`);
  }
}

main();
