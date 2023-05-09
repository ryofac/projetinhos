extends "res://assets/source/Actors/Actors.gd"
class_name Enemy

func _ready():
	set_physics_process(false)
	_velocity.x = -speed.x
	
func _physics_process(delta):
	_velocity.y += gravity * delta
	if is_on_wall():
		_velocity.x *= -1.0
	_velocity.y = move_and_slide(_velocity, floor_normal).y

func _on_isStomp_body_entered(body):
	if body.global_position.y > get_node("isStomp").global_position.y:
		return
	queue_free()

