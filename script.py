import bpy, glob
step = 1

for filename in sorted(glob.glob("c:\\temp\\Fito\\*.wrl")):
	bpy.ops.import_scene.x3d(filepath=filename, axis_forward='Z', axis_up='Y') #import vrml
	bpy.ops.object.select_all(action='TOGGLE') #deselect everything to isolate wrl light and camera 
	bpy.ops.object.select_pattern(pattern="TODO")#select light TODO
	bpy.ops.object.delete(use_global=False) #delete selected as objects
	bpy.data.lamps.remove(bpy.data.lamps['DirectLight']) #delete lamp as data
	bpy.ops.object.select_pattern(pattern="ShapeIndexedFaceSet") #select wrl mesh 
	bpy.context.scene.objects.active = bpy.data.objects["ShapeIndexedFaceSet"] #set mesh as active
	bpy.ops.object.editmode_toggle() #go to edit mode
	bpy.ops.mesh.remove_doubles()	#remove doubles
	bpy.ops.object.editmode_toggle() #get out of edit mode
	bpy.ops.object.shade_smooth() #smooth mesh
	bpy.ops.object.modifier_add(type='EDGE_SPLIT')#agregar edge modifier
	bpy.context.object.modifiers["EdgeSplit"].split_angle = 1.15192 #ángulo set at 66º
	bpy.context.object.pass_index = 1 #index pass to be used in compositor
	bpy.context.object.active_material.use_nodes = True
	bpy.ops.object.material_slot_remove() #remove material slot that comes with wrl
	serpentina = bpy.data.objects['ShapeIndexedFaceSet'] #assign mesh to var serpentina
	mat = bpy.data.materials["Material"] #assign Material to var mat 
	serpentina.data.materials.append(mat) #assign material mat to mesh serpentina
	bpy.data.scenes["Scene"].render.filepath = 'c:\\temp\\Fito\\shot_%s.png' %format(step, '03d') #set png names with trailing 0's
	bpy.ops.render.render( write_still=True ) #RENDER
	bpy.ops.object.mode_set(mode='OBJECT') #por siaka
	bpy.ops.object.select_by_type(type='MESH') #select mesh objects
	bpy.ops.object.delete(use_global=False) #delete mesh objects
	step = step +1

	for item in bpy.data.meshes: #delete mesh data
		bpy.data.meshes.remove(item)

	