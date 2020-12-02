import numpy as np
import glob, os

class CPMKGReader(object):
    def __init__(self, distmult_path, num_entity=84752481, num_relation=1228, vec_per_file=100000, cache_size=40):
        files = [ self.__parse_files(fname) for fname in glob.glob(os.path.join(distmult_path, "*.npy")) ]
        self.file_map = {
            idx: fname for idx, fname in files
        }
        assert ((num_entity + num_relation + vec_per_file - 1) // vec_per_file == len(self.file_map)), "文件数量不匹配"
        self.pageid = [None] * cache_size
        self.pagevec = [None] * cache_size
        self.pagevis = np.array([0] * cache_size)
        self.req_cnt = 0

        self.num_entity = num_entity
        self.vec_per_file = vec_per_file
        
    
    def __parse_files(self, fname):
        return int(os.path.basename(fname)[:-4]), fname
    
    def get_entity(self, idx):
        return self._get_vec(idx)
    
    def get_relation(self, idx):
        return self._get_vec(self.num_entity + idx)

    def _swapin(self, pageid):
        idx = self.pagevis.argmin()
        self.pageid[idx] = pageid
        self.pagevec[idx] = np.load( self.file_map[pageid] )
        return idx

    def _get_vec(self, idx):
        pageid = idx // self.vec_per_file
        if pageid not in self.pageid:
            pageid = self._swapin(pageid)
        else:
            pageid = self.pageid.index(pageid)
        self.req_cnt += 1
        self.pagevis[pageid] = self.req_cnt
        return self.pagevec[pageid][idx % self.vec_per_file]

    
    
