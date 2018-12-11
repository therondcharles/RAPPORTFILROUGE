def git_merge_conbine(mabranche,filesunion,delet=True):
    print("-------------------------------------------------------------------------------------------------")
    print("")
    print("git checkout master")
    print("git merge",mabranche)
    print("")
    print("")
    print("")
    print("")
    for file in filesunion:
        print("git show :1:"+str(file),">",str(file)+".base")
        print("git show :2:"+str(file),">",str(file)+".ours")
        print("git show :3:"+str(file),">",str(file)+"."+str(mabranche))
        print("mv", str(file)+".ours",file)
        print("git merge-file --union",file,str(file)+".base",str(file)+"."+str(mabranche))
        if delet:
            print("rm",str(file)+".base",str(file)+"."+str(mabranche))
        print("git add", file)
    print('git commit -m"merge',mabranche,'"')
    print("")
    print("")
    print("")
    print("")
    print("git push origin master")
    return

git_merge_conbine("ica",["fonctionCommune.py"])
git_merge_conbine("cth",["fonctionCommune.py"])