import numpy as np
import pandas as pd
import xarray as xr

def generate_synthetic_data(
    tile_ids: np.ndarray,
    start_date: str = "2000-01-01",
    days: int = 365,
    trajectories: int = 128,
    seed: int = 42
) -> xr.Dataset:
    np.random.seed(seed)
    time_index = pd.date_range(start=start_date, periods=days, freq='D')
    shape = (trajectories, days, tile_ids.size)
    data = {}
    base = {
        'population_total': 1e6,
        'food_calorie_pc': 2500,
        'freshwater_l_pc': 100,
        'energy_mj_pc': 100
    }
    noise = {
        'population_total': 0.01,
        'food_calorie_pc': 0.05,
        'freshwater_l_pc': 0.1,
        'energy_mj_pc': 0.1
    }
    for var, mu in base.items():
        arr = mu * (1 + noise[var] * np.random.randn(*shape))
        data[var] = np.clip(arr, 0, None)
    ds = xr.Dataset(
        {var: (('trajectory','time','tile'), data[var]) for var in data},
        coords={
            'trajectory': np.arange(trajectories),
            'time': time_index,
            'tile': tile_ids
        }
    )
    return ds
