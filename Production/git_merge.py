def git_merge_union(bfrom, bto, filesunion, delet=True):
    print("-------------------------------------------------------------------------------------------------")
    print("")
    print("git checkout",bto)
    print("git merge",bfrom)
    print("")
    print("")
    print("")
    print("")
    for file in filesunion:
        print("git show :1:"+str(file),">",str(file)+".base")
        print("git show :2:"+str(file),">",str(file)+".ours")
        print("git show :3:"+str(file),">",str(file)+"."+str(bfrom))
        print("mv", str(file)+".ours",file)
        print("git merge-file --union",file,str(file)+"."+str(bfrom),str(file)+".base")
        if delet:
            print("rm",str(file)+".base",str(file)+"."+str(bfrom))
        print("git add", file)
    print('git commit -m"merge',bfrom,'"')
    print("")
    print("")
    print("")
    print("")
    print("git push origin ",bto)
    return

git_merge_union("ica", ["fonctionCommune.py"])
git_merge_union("cth", ["fonctionCommune.py"])