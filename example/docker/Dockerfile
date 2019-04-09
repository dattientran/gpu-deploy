# Intermediate Container for private github repositories

FROM mudphudwang/pytorch-jupyter:bionic-pytorch1.0-cuda10.0-v3 as intermediate

ARG ssh_prv_key
ARG ssh_pub_key
ARG nsearch_branch

# Authorize SSH Host
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan github.com > /root/.ssh/known_hosts

# Add the keys and set permissions
RUN echo "$ssh_prv_key" > /root/.ssh/id_rsa && \
    echo "$ssh_pub_key" > /root/.ssh/id_rsa.pub && \
    chmod 600 /root/.ssh/id_rsa && \
    chmod 600 /root/.ssh/id_rsa.pub

# Clone Repositories
WORKDIR /src
RUN git clone https://github.com/atlab/attorch.git -b pytorch0.4.0 --single-branch
RUN git clone https://github.com/cajal/neuro_data.git -b master --single-branch
#RUN git clone https://github.com/cajal/static-networks.git -b master --single-branch

#RUN git clone git@github.com:atlab/attorch.git -b pytorch0.4.0 --single-branch
#RUN git clone git@github.com:cajal/neuro_data.git -b master --single-branch
RUN git clone git@github.com:cajal/static-networks -b master --single-branch


# Final Container (without priavte SSH keys) with installed python packages

FROM mudphudwang/pytorch-jupyter:bionic-pytorch1.0-cuda10.0-v3

COPY --from=intermediate /src/attorch /src/attorch
COPY --from=intermediate /src/neuro_data /src/neuro_data
COPY --from=intermediate /src/static-networks /src/static-networks

RUN pip install -e /src/attorch
RUN pip install -e /src/neuro_data
RUN pip install -e /src/static-networks
