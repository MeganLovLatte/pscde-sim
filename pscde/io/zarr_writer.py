# pscde/io/zarr_writer.py

import xarray as xr

try:
    import numcodecs
    blosc = numcodecs.Blosc(
        cname="zstd",
        clevel=5,
        shuffle=numcodecs.Blosc.SHUFFLE
    )
    compressors = [blosc]
except ImportError:
    compressors = None
    print("⚠️ numcodecs missing: writing uncompressed Zarr")

def write_zarr(ds: xr.Dataset, path: str):
    """
    Write an xarray.Dataset to Zarr using v2 metadata (default in older Xarray).
    Uses Blosc–Zstd if available; otherwise writes uncompressed.
    """
    if compressors:
        encoding = {var: {"compressor": blosc} for var in ds.data_vars}
    else:
        encoding = {}

    # Explicitly request Zarr v2 metadata format
    ds.to_zarr(
        store=path,
        mode="w",
        encoding=encoding,
        zarr_version=2,
        consolidated=True  # optional but speeds up reads
    )
