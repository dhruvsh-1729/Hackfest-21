GlowScript 3.1 VPython
#Please refresh the webpage each time before you run the program for better simulation

h=7   #only controls the scaling distances of the simulation
robo_velocity=4  #mention the robo's velocity
bed_height=10/h
bottle_radius=5/h
#scene.camera.pos=vector(-150/h,30/h,0)
#scene.camera.axis=vector(1,0,0)
robo=box(pos=vector(0,0,0),size=vector(20/h,15/h,20/h),color=color.red,velocity=vector(robo_velocity,0,0),make_trail=False,trail_color=color.white)

gas1=cylinder(pos=vector(-0.5*robo.size.x,robo.size.y*0.5+0.5*bottle_radius,0.25*robo.size.z),axis=vector(1,0,0),size=vector(0.6*robo.size.x,bottle_radius,bottle_radius),color=color.orange)
gas2=cylinder(pos=vector(-0.5*robo.size.x,robo.size.y*0.5+0.5*bottle_radius,-0.25*robo.size.z),axis=vector(1,0,0),size=vector(0.6*robo.size.x,bottle_radius,bottle_radius),color=color.orange)

rodheight=30/h

sanitizer=box(pos=vector(0.5*robo.size.x -0.5,0.5*robo.size.y+0.7*rodheight,0),size=vector(8/h,4/h,4/h),color=color.cyan)
rod=cylinder(pos=vector(0.5*robo.size.x -0.5,0.5*robo.size.y,0),axis=vector(0,1,0),size=vector(rodheight,0.4,0.4))

rodfull=compound([sanitizer,rod])

rider_wheel_l=cylinder(pos=vector(0.5*robo.size.x-0.5,0.5*robo.size.y,0.2),axis=vector(0,0,1),size=vector(0.2,5/h,5/h),color=color.green)
rider_wheel_r=cylinder(pos=vector(0.5*robo.size.x-0.5,0.5*robo.size.y,-0.2),axis=vector(0,0,-1),size=vector(0.2,5/h,5/h),color=color.green)

wheel_fl=cylinder(axis=vector(0,0,-1),size=vector(0.5,7.5/h,7.5/h),color=color.yellow)
wheel_fr=cylinder(axis=vector(0,0,1),size=vector(0.5,7.5/h,7.5/h),color=color.yellow)
wheel_bl=cylinder(axis=vector(0,0,-1),size=vector(0.5,7.5/h,7.5/h),color=color.yellow)
wheel_br=cylinder(axis=vector(0,0,1),size=vector(0.5,7.5/h,7.5/h),color=color.yellow)

inward_length=0.2*robo.size.x

wheel_fl.pos=0.5*vector(robo.size.x-inward_length, -robo.size.y,-robo.size.z)
wheel_fr.pos=0.5*vector(robo.size.x-inward_length, -robo.size.y,robo.size.z)
wheel_bl.pos=0.5*vector(-robo.size.x+inward_length, -robo.size.y,-robo.size.z)
wheel_br.pos=0.5*vector(-robo.size.x+inward_length, -robo.size.y,robo.size.z)

connect=cylinder(pos=vector(0.5*robo.size.x-0.5,-0.5*robo.size.y-0.5,0),axis=vector(0,1,0),size=vector(5/h,2/h,2/h))

mop=cylinder(pos=vector(0.5*robo.size.x,-0.5*robo.size.y-0.5*wheel_fl.size.y,0),axis=vector(0,1,0),size=vector(2/h,15/h,15/h))

wall=box(pos=vector(160/h,35/h,0),size=vector(5/h,100/h,100/h))
wall.visible=True

support_height=30/h
bed=box(pos=vector(120/h,robo.size.y*0.5+bed_height,-2.4*robo.size.z),size=vector(60/h,5/h,40/h))
support_fl=cylinder(pos=vector(118/h+0.5*bed.size.x,bed.pos.y-support_height,bed.pos.z-0.5*bed.size.z+2/h),axis=vector(0,1,0),size=vector(support_height,2/h,2/h))
support_fr=cylinder(pos=vector(118/h+0.5*bed.size.x,bed.pos.y-support_height,bed.pos.z+0.5*bed.size.z-2/h),axis=vector(0,1,0),size=vector(support_height,2/h,2/h))
support_bl=cylinder(pos=vector(122/h-0.5*bed.size.x,bed.pos.y-support_height,bed.pos.z-0.5*bed.size.z+2/h),axis=vector(0,1,0),size=vector(support_height,2/h,2/h))
support_br=cylinder(pos=vector(122/h-0.5*bed.size.x,bed.pos.y-support_height,bed.pos.z+0.5*bed.size.z-2/h),axis=vector(0,1,0),size=vector(support_height,2/h,2/h))

tmax,t=5,0
dt=0.001
#scene.camera.follow(robo)
angular_velocity=robo.velocity.x/wheel_fl.size.y

while(t<tmax):
  rate(1/dt)
  wheel_fl.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  wheel_fr.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  wheel_bl.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  wheel_br.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  robo.pos.x+=robo.velocity.x*dt
  wheel_fl.pos.x=wheel_fl.pos.x+robo.velocity.x*dt
  wheel_fr.pos.x=wheel_fr.pos.x+robo.velocity.x*dt
  wheel_bl.pos.x=wheel_bl.pos.x+robo.velocity.x*dt
  wheel_br.pos.x=wheel_br.pos.x+robo.velocity.x*dt
  gas1.pos.x+=robo.velocity.x*dt
  gas2.pos.x+=robo.velocity.x*dt
  rider_wheel_l.pos.x+=robo.velocity.x*dt
  rider_wheel_r.pos.x+=robo.velocity.x*dt
  rodfull.pos.x+=robo.velocity.x*dt
  #rod.pos.x+=robo.velocity.x*dt
  #sanitizer.pos.x+=robo.velocity.x*dt
  connect.pos.x+=robo.velocity.x*dt
  mop.pos.x+=robo.velocity.x*dt
  #scene.camera.pos.x+=robo.velocity.x*dt
  
  # robo.rotate(axis=vector(0,1,0),angle=angular_velocity*dt)
  if(abs(wall.pos.x-robo.pos.x)<50/h):
    robo.velocity=0
    break
  
  t+=dt

theta=0
dtheta=0.001

while(theta<=pi/2):
  rate(1000)
  #sanitizer.rotate(angle=dtheta,axis=vector(0,0,1))
  rodfull.rotate(angle=dtheta,axis=vector(0,0,-1),origin=vector(robo.pos.x+0.5*robo.size.x-0.5,0.5*robo.size.y,0))
  theta+=dtheta
  
theta=0
dtheta=0.001

while(theta<=pi/2):
  rate(1000)
  #sanitizer.rotate(angle=dtheta,axis=vector(0,0,1))
  rodfull.rotate(angle=dtheta,axis=vector(0,1,0),origin=vector(robo.pos.x+0.5*robo.size.x-0.5,0.5*robo.size.y,0))
  rider_wheel_l.rotate(angle=dtheta,axis=vector(0,1,0))
  rider_wheel_r.rotate(angle=dtheta,axis=vector(0,1,0))
  theta+=dtheta  

  
t=0
dt=.001
tmax=5
while(t<tmax):
  rate(300)
  wheel_fl.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  wheel_fr.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  wheel_bl.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  wheel_br.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  robo.pos.x+=robo_velocity*dt
  wheel_fl.pos.x=wheel_fl.pos.x+robo_velocity*dt
  wheel_fr.pos.x=wheel_fr.pos.x+robo_velocity*dt
  wheel_bl.pos.x=wheel_bl.pos.x+robo_velocity*dt
  wheel_br.pos.x=wheel_br.pos.x+robo_velocity*dt
  gas1.pos.x+=robo_velocity*dt
  gas2.pos.x+=robo_velocity*dt
  
  rider_wheel_l.pos.x+=robo_velocity*dt
  rider_wheel_r.pos.x+=robo_velocity*dt
  rodfull.pos.x+=robo_velocity*dt
  #rod.pos.x+=robo.velocity.x*dt
  #sanitizer.pos.x+=robo.velocity.x*dt
  connect.pos.x+=robo_velocity*dt
  mop.pos.x+=robo_velocity*dt
  
  if(abs(robo.pos.x-wall.pos.x)<25/h):
    robo_velocity=0
    break
  
  t+=dt
robo_velocity=-5  
t=0
dt=.001
tmax=5
while(t<tmax):
  rate(300)
  wheel_fl.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  wheel_fr.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  wheel_bl.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  wheel_br.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  robo.pos.x+=robo_velocity*dt
  wheel_fl.pos.x=wheel_fl.pos.x+robo_velocity*dt
  wheel_fr.pos.x=wheel_fr.pos.x+robo_velocity*dt
  wheel_bl.pos.x=wheel_bl.pos.x+robo_velocity*dt
  wheel_br.pos.x=wheel_br.pos.x+robo_velocity*dt
  gas1.pos.x+=robo_velocity*dt
  gas2.pos.x+=robo_velocity*dt
  rider_wheel_l.pos.x+=robo_velocity*dt
  rider_wheel_r.pos.x+=robo_velocity*dt
  rodfull.pos.x+=robo_velocity*dt
  #rod.pos.x+=robo.velocity.x*dt
  #sanitizer.pos.x+=robo.velocity.x*dt
  connect.pos.x+=robo_velocity*dt
  mop.pos.x+=robo_velocity*dt
  
  if(abs(robo.pos.x-wall.pos.x)>65/h):
    robo_velocity=0
    break
  
  t+=dt  
  
theta=0
dtheta=0.001

while(theta<=pi/2):
  rate(1000)
  #sanitizer.rotate(angle=dtheta,axis=vector(0,0,1))
  rodfull.rotate(angle=dtheta,axis=vector(0,-1,0),origin=vector(robo.pos.x+0.5*robo.size.x-0.5,0.5*robo.size.y,0))
  rider_wheel_l.rotate(angle=dtheta,axis=vector(0,-1,0))
  rider_wheel_r.rotate(angle=dtheta,axis=vector(0,-1,0))
  theta+=dtheta    
  
theta=0
dtheta=0.001

while(theta<=pi/2):
  rate(1000)
  #sanitizer.rotate(angle=dtheta,axis=vector(0,0,1))
  rodfull.rotate(angle=dtheta,axis=vector(0,0,1),origin=vector(robo.pos.x+0.5*robo.size.x-0.5,0.5*robo.size.y,0))
  theta+=dtheta  
  
tmax,t=5,0
dt=0.001
#scene.camera.follow(robo)

robo_velocity=-5
while(t<tmax):
  rate(500)
  # wheel_fl.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  # wheel_fr.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  # wheel_bl.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  # wheel_br.rotate(axis=vector(0,0,1),angle=angular_velocity*dt)
  robo.pos.x+=robo_velocity*dt
  wheel_fl.pos.x=wheel_fl.pos.x+robo_velocity*dt
  wheel_fr.pos.x=wheel_fr.pos.x+robo_velocity*dt
  wheel_bl.pos.x=wheel_bl.pos.x+robo_velocity*dt
  wheel_br.pos.x=wheel_br.pos.x+robo_velocity*dt
  gas1.pos.x+=robo_velocity*dt
  gas2.pos.x+=robo_velocity*dt
  rider_wheel_l.pos.x+=robo_velocity*dt
  rider_wheel_r.pos.x+=robo_velocity*dt
  rodfull.pos.x+=robo_velocity*dt
  #rod.pos.x+=robo.velocity.x*dt
  #sanitizer.pos.x+=robo.velocity.x*dt
  connect.pos.x+=robo_velocity*dt
  mop.pos.x+=robo_velocity*dt
  #scene.camera.pos.x+=robo.velocity.x*dt
  
  # robo.rotate(axis=vector(0,1,0),angle=angular_velocity*dt)
  if(abs(wall.pos.x-robo.pos.x)>130/h):
    robo.velocity=0
    break
  
  t+=dt
  
# robo.visible=False
# wheel_fl.visible=False
# wheel_bl.visible=False
# wheel_fr.visible=False  
# wheel_br.visible=False
# connect.visible=False
# sanitizer.visible=False
# rod.visible=False
# rider_wheel_l.visible=False
# rider_wheel_r.visible=False
# mop.visible=False
# bed.visible=False
# support_fl.visible=False

# support_bl.visible=False

# support_fr.visible=False  

# support_br.visible=False

# full_robot=compound([robo,wheel_fl,wheel_bl,wheel_fr,wheel_br,rod,connect,sanitizer,mop,rider_wheel_l, rider_wheel_r,gas1,gas2])

# theta=0
# dtheta=0.001

# while(theta<=pi):
#   rate(300)
#   full_robot.rotate(axis=vector(0,1,0), angle=-dtheta)
#   theta+=dtheta

  
  
