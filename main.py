"""

    """

import json
from pathlib import Path

import pandas as pd
from mirutil.pathes import get_all_subdirs
from mirutil.pathes import has_subdir
from mirutil.df_utils import read_data_according_to_type as read_data
from mirutil.df_utils import save_df_as_a_nice_xl as sxl


class Params :
    _pth = '/Users/mahdi/Library/CloudStorage/OneDrive-khatam.ac.ir/Datasets/Heidari Data/V2'
    root_dir = Path(_pth)

p = Params()

class ColName :
    path = 'path'
    sfp = 'sfp'
    dfp = 'dfp'

c = ColName()

def find_sample_sfp(pth) :
    ls = list(pth.glob('Sample-*.xlsx'))
    if ls :
        return ls[0]

def find_data_fp(pth) :
    lo = list(pth.glob('*'))
    lo = [i for i in lo if i.name not in ['.DS_Store' , 'meta.json']]
    assert len(lo) == 1
    return lo[0]

def make_sample_xl(dfp) :
    df = read_data(dfp)
    smpl_size = min(100 , len(df))
    df = df.sample(smpl_size)
    sfp = dfp.parent / f'Sample-{dfp.stem}.xlsx'
    sxl(df , sfp)

def main() :
    pass

    ##
    # 1. get all subdirs
    subs = get_all_subdirs(p.root_dir)
    ##
    df = pd.DataFrame()
    df[c.path] = list(subs)
    ##
    msk = ~ df[c.path].apply(has_subdir)
    df = df[msk]
    ##
    df[c.sfp] = df[c.path].apply(find_sample_sfp)
    ##
    msk = df[c.sfp].isna()
    len(df[msk])
    ##
    df.loc[msk , c.dfp] = df.loc[msk , c.path].apply(find_data_fp)
    _ = df.loc[msk , c.dfp].apply(make_sample_xl)

    ##

    ##

##
if __name__ == "__main__" :
    main()
    print("Done!")
