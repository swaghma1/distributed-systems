#!/usr/bin/python
import sys, glob

from sys import platform
if platform == "linux" or platform == "linux2":
    sys.path.insert(0, glob.glob('/home/yaoliu/src_code/local/lib/lib/python2.7/site-packages/')[0])

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from thrift.Thrift import TProcessor
from thrift.protocol import TProtocol

try:
    from thrift.protocol import fastbinary
except:
    fastbinary = None

import re
import hashlib


class NodeID:
    """
  Attributes:
   - id
   - ip
   - port
  """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'id', None, None,),  # 1
        (2, TType.STRING, 'ip', None, None,),  # 2
        (3, TType.I32, 'port', None, None,),  # 3
    )

    def __init__(self, id=None, ip=None, port=None, ):
        self.id = id
        self.ip = ip
        self.port = port

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans,
                                                                                        TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.ip = iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I32:
                    self.port = iprot.readI32()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('NodeID')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id)
            oprot.writeFieldEnd()
        if self.ip is not None:
            oprot.writeFieldBegin('ip', TType.STRING, 2)
            oprot.writeString(self.ip)
            oprot.writeFieldEnd()
        if self.port is not None:
            oprot.writeFieldBegin('port', TType.I32, 3)
            oprot.writeI32(self.port)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Iface:
    def setReplicationtable(self, node_list):
        """
        Parameters:
         - node_list
        """
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def setReplicationtable(self, node_list):
        """
        Parameters:
         - node_list
        """
        self.send_setReplicationtable(node_list)
        self.recv_setReplicationtable()

    def send_setReplicationtable(self, node_list):
        self._oprot.writeMessageBegin('setReplicationtable', TMessageType.CALL, self._seqid)
        args = setReplicationtable_args()
        args.node_list = node_list
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_setReplicationtable(self):
        (fname, mtype, rseqid) = self._iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(self._iprot)
            self._iprot.readMessageEnd()
            raise x
        result = setReplicationtable_result()
        result.read(self._iprot)
        self._iprot.readMessageEnd()
        return

class setReplicationtable_args:
    """
  Attributes:
   - node_list
  """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'node_list', (TType.STRUCT, (NodeID, NodeID.thrift_spec)), None,),  # 1
    )

    def __init__(self, node_list=None, ):
        self.node_list = node_list

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans,
                                                                                        TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.node_list = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = NodeID()
                        _elem5.read(iprot)
                        self.node_list.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('setReplicationtable_args')
        if self.node_list is not None:
            oprot.writeFieldBegin('node_list', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.node_list))
            for iter6 in self.node_list:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class setReplicationtable_result:
    thrift_spec = (
    )

    def read(self, iprot):
        if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans,
                                                                                        TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
            fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
            oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('setReplicationtable_result')
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

def create_node(s):
    sha256 = hashlib.sha256()
    sha256.update(s.encode())
    k = sha256.hexdigest()

    m = re.match('([^:]+):([^:]+)', s)
    return NodeID(k, m.group(1), int(m.group(2)))

def createReplicas(nid, lst):
    print('Creation replica for', nid)
    index = lst.index(nid) // 4
    start = 4 * index
    end = 4 * (index + 1) if 4 * (index + 1) < len(lst) else len(lst)
    replicas = lst[start:end]
    # print(replicas)
    return replicas


def init_replicatiom(nid, lst, cdct=None):
    replicaTable = createReplicas(nid, lst)

    if cdct == None:
        transport = TSocket.TSocket(nid.ip, nid.port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = Client(protocol)
        transport.open()
        try:
            client.setReplicationtable(replicaTable)
        finally:
            transport.close()
    else:
        # buffered clients
        client = cdct['%s:%d' % (nid.ip, nid.port)]
        client.setReplicationtable(replicaTable)


if __name__ == '__main__':
    fn = sys.argv[1]
    lst = sorted([create_node(l[:-1]) for l in open(fn)], key=lambda x: x.id)

    print ('starting replicas')
    for l in lst:
        print('replica for' , l.port)
        init_replicatiom(l, lst)
