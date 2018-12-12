import Production.git_merge as gmerge

# from cth -> to master
gmerge.git_merge_union("cth","master",["fonctionCommune.py"])

# from master -> to cth
gmerge.git_merge_union("master","cth",["fonctionCommune.py","git_merge.py"])

