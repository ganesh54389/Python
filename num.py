#--------------------------creation of array-------------------------------------
import numpy as np
a=np.array([1,2,3,4,5,"kishor"])
print(a)
#-------------------------dimension of array------------------------------------
a=np.array(10)
b=np.array([1,2,3])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[7,4,1]]])
print(a)
print(a.ndim)
print(a.shape)
print(a.dtype)

print("------------")
print(b)
print(b.ndim)
print(b.shape)
print(b.dtype)
print(len(b))
print(type(b))
print("--------------")
print(c)
print(c.ndim)
print(c.shape)
print(c.dtype)
print(len(c))
print(type(c))
print("--------------")
print(d)
print(d.ndim)
print(d.shape)
print(d.dtype)
print(len(d))
print(type(d))
#-----------------------------------creating of array in number of ways ------------------------
#arange function
a=np.arange(1,11)
print(a)
b=np.arange(0,11,2)
print(b)
#eyes function
a=np.eye(3,dtype=int)
print(a)
#ones function
a=np.ones((6,3),dtype=int)
print(a) 
#zeros function 
a=np.zeros((3,5),dtype=int)
print(a)
#full function
a=np.full((3,5),10,dtype=int)
print(a)
#diagonal function
x=[1,2,3,4,5,6]
a=np.diag(x)
print(a)
#-----------------------------------array reshape----------------------------
x=np.arange(1,17)
print(x)
print(x.ndim)
n=x.reshape((8,2))
print(n)
print(n.ndim)
c=n.reshape((4,4))
print(c)
print(c.ndim)

#ravel
d=c.ravel()
print(d)
e=d.flatten()
print(e)
#----------------------numpy array indexing and slicingn--------
a=np.arange(2,17,2)
print(a)
print(a[5])
print(a[ :3])

c=np.array([[1,2,3],[4,5,6]])
print(c[0][1])
print(c[1][1])

d=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[7,4,1]]])
print(d[0][0][1])
print(d[1][0][1])

#conditions
c=np.array([[1,2,3],[4,5,6],[7,8,9]])
d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c)
print(c>3)
print(c[c>3])
print(c.T)#transpose
#hstack and vstack
print(np.hstack((c,d)))
print(np.vstack((c,d)))


c=np.array([1,2,3,4,5,6,7,8,9])
d=np.array([1,2,3,4,5,6,7,8,9])
print(np.insert(c,4,d))


print(np.delete(c,2))
#--------------------mathematicl operation on numpy array -------------------------
a=np.array([[1,2,3],[4,5,6],[7,4,4]])
print(a)
print(np.sin(a))
print("-"*20)
print(np.cos(a))
print("-"*20)
print(np.tan(a))
print("-"*20)
ki=np.sin(a)/np.cos(a)
print(ki)
print(np.exp(a))
print(np.sum(a))
print(np.mean(a))
print(np.median(a))
k=np.array([1,2,3,4,5,4,7,8,9])
print(np.std(k))
print(np.max(a))
print(np.sort(a))
print(dir(list))
print("----"*30)
print(dir(set))
print("--"*30)
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))













