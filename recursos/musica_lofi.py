import numpy as np, wave
sr=44100; bpm=82; beat=60/bpm; bars=8; T=bars*4*beat+1.0
n=int(sr*T); L=np.zeros(n); R=np.zeros(n)
rng=np.random.default_rng(7)
def mtof(m): return 440*2**((m-69)/12)
def ep(f,dur,vel):  # suave tipo piano eléctrico
    t=np.arange(int(sr*dur))/sr
    env=np.exp(-t*2.2)*(1-np.exp(-t*80))
    s=np.sin(2*np.pi*f*t)+0.35*np.sin(2*np.pi*2*f*t)*np.exp(-t*4)+0.12*np.sin(2*np.pi*3*f*t)*np.exp(-t*7)
    s*= (1+0.004*np.sin(2*np.pi*5*t))
    return s*env*vel
def add(buf,s,start,pan=0.5):
    i=int(start*sr); e=min(n,i+len(s)); L[i:e]+=s[:e-i]*(1-pan); R[i:e]+=s[:e-i]*pan
chords=[[53,57,60,64],[52,55,59,62],[50,53,57,60],[48,52,55,59]]  # Fmaj7 Em7 Dm7 Cmaj7
for b in range(bars):
    c=chords[b%4]; t0=b*4*beat
    for k,m in enumerate(c):
        add(L,ep(mtof(m),4*beat+0.8,0.13),t0+k*0.025+rng.uniform(0,0.01),0.35+0.1*k)
    add(L,ep(mtof(c[0]-12),4*beat,0.22),t0,0.5)
    mel=[c[3]+12,c[2]+12,c[1]+12,c[2]+12]
    for j,m in enumerate(mel):
        if (b+j)%3!=2: add(L,ep(mtof(m),1.2,0.06),t0+j*beat+0.5*beat,0.65)
    for q in range(4):
        tq=t0+q*beat
        if q in (0,2):
            t=np.arange(int(sr*0.35))/sr; f=55*np.exp(-t*18)+45
            add(L,np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-t*9)*0.35,tq,0.5)
        if q in (1,3):
            t=np.arange(int(sr*0.2))/sr
            add(L,rng.normal(0,1,len(t))*np.exp(-t*25)*0.06,tq,0.5)
        for h in (0,0.5):
            t=np.arange(int(sr*0.05))/sr
            hh=np.diff(rng.normal(0,1,len(t)+1))*np.exp(-t*90)*0.025
            add(L,hh,tq+h*beat+rng.uniform(0,0.012),0.6)
noise=rng.normal(0,0.004,n); L+=noise; R+=noise
crk=(rng.random(n)<0.0003)*rng.normal(0,0.05,n); L+=crk; R+=crk
# filtro paso bajo simple (cálido)
def lp(x,a=0.35):
    y=np.copy(x)
    for i in range(1,len(x)): y[i]=y[i-1]+a*(x[i]-y[i-1])
    return y
L=lp(L); R=lp(R)
m=max(abs(L).max(),abs(R).max()); L=L/m*0.8; R=R/m*0.8
data=(np.stack([L,R],1)*32767).astype('<i2')
w=wave.open('lofi.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes(data.tobytes()); w.close()
print(T)
