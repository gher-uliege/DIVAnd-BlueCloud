[![Build Status](https://travis-ci.org/gher-ulg/DIVAnd-BlueCloud.svg?branch=master)](https://travis-ci.org/gher-ulg/DIVAnd-BlueCloud)

# Docker image

The image is available from the [Docker hub](https://hub.docker.com/repository/docker/abarth/divand-bluecloud):

```julia
docker pull abarth/divand-bluecloud:latest
```

## Run a script

To execute a script `script.jl` inside the folder e.g. `~/src/DIVAnd-BlueCloud` on the host use:

```bash
docker run -it -v ~/src/DIVAnd-BlueCloud:/data:rw abarth/divand-bluecloud:latest julia --eval 'include("/data/script.jl")'
```

All results written to `/data` in the docker container will be available in `~/src/DIVAnd-BlueCloud` on the host.

## Run a notebook

To execute a Jupyter notebook `myfile.ipynb` (in non-interactively, i.e. in batch-mode) use:

```bash
docker run -it -v ~/src/DIVAnd-BlueCloud:/data:rw abarth/divand-bluecloud:latest julia --eval 'using NBInclude; @nbinclude("myfile.ipynb")'
```


# Precompiled DIVAnd with `PackageCompiler`



Load-time of DIVAnd and simple analysis without precompiled image:

```julia
julia> @time using DIVAnd
@time include(joinpath(dirname(pathof(DIVAnd)),"..","test","test_product.jl"))
  6.423211 seconds (11.08 M allocations: 549.436 MiB, 2.36% gc time)

julia> @time include(joinpath(dirname(pathof(DIVAnd)),"..","test","test_product.jl"))
[ Info: download bathymetry /home/jovyan/.julia/packages/DIVAnd/gsgEt/test/../../DIVAnd-example-data/Global/Bathymetry/gebco_30sec_16.nc
[ Info: download observations /home/jovyan/.julia/packages/DIVAnd/gsgEt/test/../../DIVAnd-example-data/Provencal/WOD-Salinity.nc
188.275971 seconds (754.34 M allocations: 49.429 GiB, 7.16% gc time)
```

When you first load and run a package in a session, Julia needs to compile it first. This creates some overhead on first use with can be removed by using a precompiled image.


```julia
julia> @time using DIVAnd
  0.000500 seconds (226 allocations: 12.203 KiB)

julia> @time include(joinpath(dirname(pathof(DIVAnd)),"..","test","test_product.jl"))
[ Info: download bathymetry /home/jovyan/.julia/packages/DIVAnd/gsgEt/test/../../DIVAnd-example-data/Global/Bathymetry/gebco_30sec_16.nc
[ Info: download observations /home/jovyan/.julia/packages/DIVAnd/gsgEt/test/../../DIVAnd-example-data/Provencal/WOD-Salinity.nc
 80.839016 seconds (472.02 M allocations: 35.777 GiB, 11.47% gc time)
```

The load time of DIVAnd is reduces from 6 s to 0.0005 s and a make a sample analysis is reduced from 188 s to 80 s.
