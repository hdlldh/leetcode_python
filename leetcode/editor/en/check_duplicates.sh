 ls|awk -F'.' '{a[$1]+=1}END{for(x in a) {if (a[x]!=2) print x}}'|sort
