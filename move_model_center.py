import bpy
import mathutils
from mathutils import Vector

if __name__=='__main__':
    obj = bpy.context.object
    bound_box = obj.bound_box
    world_bound_box = [\
        obj.matrix_world @ mathutils.Vector(corner) \
        for corner in bound_box]
    min_x, min_y, min_z = world_bound_box[0]
    max_x, max_y, max_Z = world_bound_box[6]
    
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    center_z = min_z
    
    bpy.context.scene.cursor.location = Vector((center_x, center_y, center_z))
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.context.scene.cursor.location = Vector((0, 0, 0))
    