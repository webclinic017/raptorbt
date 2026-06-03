//! Signal processing for RaptorBT.
//!
//! This module handles signal cleaning, synchronization, and expression evaluation.

pub mod expression;
pub mod processor;
pub mod synchronizer;
pub mod tick_signals;

pub use processor::SignalProcessor;
pub use synchronizer::{SignalSynchronizer, SyncMode};
pub use tick_signals::{tick_momentum_entry, tick_momentum_exit};
