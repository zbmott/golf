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
If you invoke it with the path to a Python module that contains a `Hole`, e.g.:
```
> python hole_edit.py courses.first_course.Hole1
```
You'll be able to edit that hole. When you save it, it will always be saved
as a new hole, and you'll have to re-create any non-collidible sprites you had
declared.

Here's how it works:
- The black area is your canvas. You're only allowed to put minigolf elements on the canvas.
- You use the keyboard to set a minigolf element to your palette.
- Here are the available minigolf elements:
  - Golf(B)all
  - (P)in
  - (G)reen
  - (R)ough
  - (S)and
  - S(l)ope
  - (T)unnel
  - (W)all
  - Wa(t)er
  - La(v)a
- A hole must have one `GolfBall` and at least one `Pin`.
- `left-click` to start placing the element on your palette.
- For 1-D elements (`GolfBall`, `Pin`), click a second time to confirm your placement
- When placing a `Tunnel`, you have to click an extra time to indicate the `Tunnel's` exit.
- For linear elements (`Wall`), click a second time to finish placing an element. Subsequent clicks will create a new element using the previous click as the starting point. Press `spacebar` or `Esc` when you're done placing linear elements.
- For polygonal elements (`Green`, `Lava`, `Rough`, `Sand`, `Slope`, `Water`), click will place another point at the pointer's current position. Press `spacebar` to finish placing a polygonal element.
- While placing a linear or polygonal element, you can hold `shift` to align your next point with the previous point along the X or Y axis, or place the next point at an approximate 45-degree angle to the previous point.
- Pressing `Esc` between clicks will cancel the element you're trying to place and clear your palette.
- While your palette is cleared, you can click on an element to select it, and the press `backspace` or `delete` to remove it from the canvas.
- When you're happy with the hole you've designed, press Cmd/Ctrl + S to save it.
- The hole will be saved as `new_hole.py`. To play it, you need to add it to a course. For example, to add it to the default course:
  1. Move `new_hole.py` to `courses/first_course/NewHole.py`.
  2. Edit `courses/first_course/__init__.py` and add `'courses.first_course.NewHole'` to the list of holes.
  3. Now you can play minigolf using the hole you just made!
  4. If your hole has any `Slope` elements, you'll need to manually specify the vector that gets added to the `GolfBall`'s velocity each frame it's in contact with the `Slope`.
  5. You may also want to add `Text` elements to your hole, or tweak the position of your `Pin` and `GolfBall` elements
- Don't forget to bound your hole with `Walls`. Or do forget, and laugh when your ball goes flying off into space.

