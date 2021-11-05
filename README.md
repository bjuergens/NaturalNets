

# Training using GPU

1. Uninstall `deap`
2. Run `pip install git+https://github.com/neuroevolution-ai/deap@eigenvalues-on-gpu` 
3. Run `pip install cupy-cuda101` if you have a GPU with CUDA 10.1 (if you have another version check the [CuPy website](https://cupy.dev/))
4. Then the eigenvalue calculation should happen on the GPU


# quickstart (ubuntu 21.04, anaconda)

1. install anaconda https://www.anaconda.com/products/individual#Downloads
2. create/activate env `conda create -n nn python=3.7 numpy` && `conda activate nn`
3. install all conda packages `conda install -c conda-forge cupy cudatoolkit=10.1` (optional: test if cupy actually works)
4. install all pip packages `pip install -r requirements.txt`
5. optional: install deap with GPU (see note above)
5. install natural nets `pip install -e .`
6. prepare `Configuration.json` (i.e. by copying it from an older experiment)

# troubleshooting

if you get the message `error in deap setup command: use_2to3 is invalid.`, you need install an older version of setuptools:

    pip install -U 'setuptools<58'


if you get the message `ImportError: libcublas.so.10: cannot open shared object file`, you may need to install cudo `pip install cuda` or cuda toolkit `sudo apt install nvidia-cuda-toolkit` or  https://developer.nvidia.com/cuda-toolkit
