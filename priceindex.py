import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import yfinance as yf

def get_stock_data(ticker_symbol):
    """
    获取指定股票或ETF的最新交易数据。
    
    :param ticker_symbol: 股票或ETF的符号（如 SPY, QQQ）
    :return: 最新交易日期和数据字典
    """
    try:
        ticker = yf.Ticker(ticker_symbol)
        hist = ticker.history(period="1d")
        
        if not hist.empty:
            latest_date = hist.index[-1].strftime('%Y-%m-%d')
            latest_data = hist.iloc[-1].to_dict()
            # 将键名转换为中文以匹配原始输出格式
            translated_data = {
                "开盘价": round(latest_data['Open'], 2),
                "最高价": round(latest_data['High'], 2),
                "最低价": round(latest_data['Low'], 2),
                "收盘价": round(latest_data['Close'], 2),
                "成交量": int(latest_data['Volume'])
            }
            return latest_date, translated_data
        else:
            print(f"未能获取 {ticker_symbol} 的最新数据。")
            return None, None
    except Exception as e:
        print(f"获取 {ticker_symbol} 数据时发生错误: {e}")
        return None, None

def get_crypto_data(ticker_symbol):
    """
    获取指定加密货币的最新交易数据。
    
    :param ticker_symbol: 加密货币的符号（如 BTC-USD）
    :return: 最新交易日期和价格
    """
    try:
        ticker = yf.Ticker(ticker_symbol)
        hist = ticker.history(period="1d")
        
        if not hist.empty:
            latest_date = hist.index[-1].strftime('%Y-%m-%d')
            latest_price = round(hist['Close'][-1], 2)
            return latest_date, latest_price
        else:
            print(f"未能获取 {ticker_symbol} 的最新价格。")
            return None, None
    except Exception as e:
        print(f"获取 {ticker_symbol} 数据时发生错误: {e}")
        return None, None

def get_sse_data(ticker_symbol):
    """
    获取指定指数的最新交易数据。
    
    :param ticker_symbol: 指数的符号（如 000001.SS）
    :return: 最新交易日期和数据字典
    """
    try:
        ticker = yf.Ticker(ticker_symbol)
        hist = ticker.history(period="1d")
        
        if not hist.empty:
            latest_date = hist.index[-1].strftime('%Y-%m-%d')
            latest_data = hist.iloc[-1].to_dict()
            translated_data = {
                "开盘价": round(latest_data['Open'], 2),
                "最高价": round(latest_data['High'], 2),
                "最低价": round(latest_data['Low'], 2),
                "收盘价": round(latest_data['Close'], 2),
                "成交量": int(latest_data['Volume'])
            }
            return latest_date, translated_data
        else:
            print(f"未能获取 {ticker_symbol} 的最新数据。")
            return None, None
    except Exception as e:
        print(f"获取 {ticker_symbol} 数据时发生错误: {e}")
        return None, None

def main():
    # 获取 SP500 指数数据，使用 SPY ETF
    sp500_date, sp500_data = get_stock_data("SPY")
    if sp500_data:
        print(f"SP500 (SPY) 最新数据 ({sp500_date}):")
        print(f"  开盘价: {sp500_data['开盘价']}")
        print(f"  最高价: {sp500_data['最高价']}")
        print(f"  最低价: {sp500_data['最低价']}")
        print(f"  收盘价: {sp500_data['收盘价']}")
        print(f"  成交量: {sp500_data['成交量']}\n")
    else:
        print("未能获取 SP500 (SPY) 的最新数据。\n")
    
    # 获取纳斯达克指数数据，使用 QQQ ETF
    nasdaq_date, nasdaq_data = get_stock_data("QQQ")
    if nasdaq_data:
        print(f"纳斯达克 (QQQ) 最新数据 ({nasdaq_date}):")
        print(f"  开盘价: {nasdaq_data['开盘价']}")
        print(f"  最高价: {nasdaq_data['最高价']}")
        print(f"  最低价: {nasdaq_data['最低价']}")
        print(f"  收盘价: {nasdaq_data['收盘价']}")
        print(f"  成交量: {nasdaq_data['成交量']}\n")
    else:
        print("未能获取纳斯达克 (QQQ) 的最新数据。\n")
    
    # 获取比特币价格
    btc_date, btc_price = get_crypto_data("BTC-USD")
    if btc_price:
        print(f"比特币价格 (USD) 最新数据 ({btc_date}): {btc_price}\n")
    else:
        print("未能获取比特币 (BTC-USD) 的最新价格。\n")
    
    # 获取上证指数数据
    sse_date, sse_data = get_sse_data("000001.SS")
    if sse_data is not None:
        print(f"上证指数 最新数据 ({sse_date}):")
        print(f"  开盘价: {sse_data['开盘价']}")
        print(f"  最高价: {sse_data['最高价']}")
        print(f"  最低价: {sse_data['最低价']}")
        print(f"  收盘价: {sse_data['收盘价']}")
        print(f"  成交量: {sse_data['成交量']}\n")
    else:
        print("未能获取上证指数的最新数据。\n")

if __name__ == "__main__":
    main()