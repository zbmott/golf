# Golf
Golf is a bad Python implementation of minigolf. 
Part of the fun is that it's not very good and weird things happen.

## Installation and Usage
1. Clone the repository.
2. Install the dependencies:
```
> pipenv install
```
3. Activate the pipenv shell and play golf:
```
> pipenv shell
> python golf.py
```

## Editing levels
`golf` comes with a bad level editor, `hole_edit.py`. You can run it with
```
> python hole_edit.py
```
Here's how it works:
- The black area is your canvas. You're only allowed to put minigolf elements on the canvas.
- You use the keyboard to switch between minigolf elements, and you use left-click to place them.
- Here are the available minigolf elements:
  - Golf(B)all
  - (P)in
  - (G)reen
  - (R)ough
  - (S)and
  - S(l)ope
  - (W)all
- A hole must have one `GolfBall` and at least one `Pin`.
- Left click to start placing an element, and left click again when you're satisfied with its position.
- Pressing Esc between clicks will cancel the element you're trying to place.
- You can't delete an element once it's been placed.
- When you're happy with the hole you've designed, press Cmd/Ctrl + S to save it.
- The hole will be saved as `new_hole.py`. To play it, you need to add it to a course. For example, to add it to the default course:
  1. Move `new_hole.py` to `courses/first_course/NewHole.py`.
  2. Edit `courses/first_course/__init__.py` and add `'courses.first_course.NewHole'` to the list of holes.
  3. Now you can play minigolf using the hole you just made!
- Don't forget to bound your hole with `Walls`. Or do forget, and laugh when your ball goes flying off into space.

