//! Strategy implementations for different backtest types.

pub mod basket;
pub mod multi;
pub mod options;
pub mod pairs;
pub mod single;
pub mod spreads;
pub mod tick;

pub use basket::BasketBacktest;
pub use multi::MultiStrategyBacktest;
pub use options::OptionsBacktest;
pub use pairs::PairsBacktest;
pub use single::SingleBacktest;
pub use spreads::{
    LegConfig, OptionType as SpreadOptionType, SpreadBacktest, SpreadConfig, SpreadType,
};
pub use tick::{TickBacktest, TickBacktestConfig};
