from parentnode import ParentNode
from leafnode import LeafNode

# Test 1: Basic nesting
print("Test 1: Basic nesting")
basic_nest = ParentNode(
    "div",
    [LeafNode("p", "Hello")]
)
print(basic_nest.to_html())  # Should print: <div><p>Hello</p></div>

# Test 2: Properties
print("\nTest 2: With properties")
with_props = ParentNode(
    "div",
    [LeafNode("p", "Hello")],
    {"class": "container", "id": "main"}
)
print(with_props.to_html())  # Should print: <div class="container" id="main"><p>Hello</p></div>

# Test 3: Deep nesting
print("\nTest 3: Deep nesting")
deep_nest = ParentNode(
    "div",
    [
        ParentNode(
            "p",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " and "),
                LeafNode("i", "italic"),
            ]
        )
    ]
)
print(deep_nest.to_html())  # Should print: <div><p><b>Bold</b> and <i>italic</i></p></div>

# Test 4: Error cases
print("\nTest 4: Error cases")
try:
    bad_node = ParentNode(None, [LeafNode("p", "Hello")])
    print(bad_node.to_html())
except ValueError as e:
    print(f"Caught expected error: {e}")

try:
    bad_node2 = ParentNode("div", None)
    print(bad_node2.to_html())
except ValueError as e:
    print(f"Caught expected error: {e}")