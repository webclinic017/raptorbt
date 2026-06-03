"""
RaptorBT - High-performance Rust backtesting engine.

Provides Python bindings for a Rust-based backtesting engine built for
production quantitative trading:
- Sub-millisecond execution on thousands of bars
- Disk footprint: <10MB, startup latency: <10ms
- 100% deterministic execution (no JIT cache)
- Native parallelism via Rayon + explicit SIMD
- Full tick-level simulation (no bar resampling required)
"""

from raptorbt._raptorbt import (
    # Config classes
    PyBacktestConfig,
    PyInstrumentConfig,
    PyStopConfig,
    PyTargetConfig,
    # Result classes
    PyBacktestResult,
    PyBacktestMetrics,
    PyTrade,
    # Backtest functions
    run_single_backtest,
    run_basket_backtest,
    run_options_backtest,
    run_pairs_backtest,
    run_multi_backtest,
    run_spread_backtest,
    run_tick_backtest,
    # Batch backtest
    PyBatchSpreadItem,
    batch_spread_backtest,
    # Monte Carlo simulation
    simulate_portfolio_mc,
    # Tick signal functions
    compute_tick_entry_signals,
    compute_tick_exit_signals,
    # Tick feature functions
    tick_spread_pct,
    buy_sell_imbalance_delta,
    return_window,
    realized_vol_rolling,
    oi_position_pct,
    tick_velocity,
    # Indicator functions
    sma,
    ema,
    rsi,
    macd,
    stochastic,
    atr,
    bollinger_bands,
    adx,
    vwap,
    supertrend,
    rolling_min,
    rolling_max,
)

__version__ = "0.4.0"

__all__ = [
    # Config classes
    "PyBacktestConfig",
    "PyInstrumentConfig",
    "PyStopConfig",
    "PyTargetConfig",
    # Result classes
    "PyBacktestResult",
    "PyBacktestMetrics",
    "PyTrade",
    # Backtest functions
    "run_single_backtest",
    "run_basket_backtest",
    "run_options_backtest",
    "run_pairs_backtest",
    "run_multi_backtest",
    "run_spread_backtest",
    "run_tick_backtest",
    # Batch backtest
    "PyBatchSpreadItem",
    "batch_spread_backtest",
    # Monte Carlo simulation
    "simulate_portfolio_mc",
    # Tick signal functions
    "compute_tick_entry_signals",
    "compute_tick_exit_signals",
    # Tick feature functions
    "tick_spread_pct",
    "buy_sell_imbalance_delta",
    "return_window",
    "realized_vol_rolling",
    "oi_position_pct",
    "tick_velocity",
    # Indicator functions
    "sma",
    "ema",
    "rsi",
    "macd",
    "stochastic",
    "atr",
    "bollinger_bands",
    "adx",
    "vwap",
    "supertrend",
    "rolling_min",
    "rolling_max",
]
