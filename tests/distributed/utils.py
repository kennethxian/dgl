
import socket
import os

def get_local_usable_addr():
    """Get local usable IP and port

    Returns
    -------
    str
        IP address, e.g., '192.168.8.12:50051'
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        sock.connect(('10.255.255.255', 1))
        ip_addr = sock.getsockname()[0]
    except ValueError:
        ip_addr = '127.0.0.1'
    finally:
        sock.close()
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", 0))
    sock.listen(1)
    port = sock.getsockname()[1]
    sock.close()

    return ip_addr + ' ' + str(port)


def reset_envs():
    """Reset common environment variable which are set in tests. """
    for key in ['DGL_ROLE', 'DGL_NUM_SAMPLER', 'DGL_NUM_SERVER', 'DGL_DIST_MODE', 'DGL_NUM_CLIENT']:
        if key in os.environ:
            os.environ.pop(key)
